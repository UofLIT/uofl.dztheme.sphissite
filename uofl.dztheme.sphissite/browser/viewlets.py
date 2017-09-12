from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.app.layout.viewlets import common
from zope.component import getMultiAdapter, getUtility
from Acquisition import aq_base, aq_inner
from AccessControl import getSecurityManager
from Products.CMFCore.utils import getToolByName
from uofl.p4hnfpicker.interfaces import IHNFPickerSettings
from plone.registry.interfaces import IRegistry

# Sample code for a basic viewlet (In order to use it, you'll have to):
# - Un-comment the following useable piece of code (viewlet python class).
# - Rename the viewlet template file ('browser/viewlet.pt') and edit the
#   following python code accordingly.
# - Edit the class and template to make them suit your needs.
# - Make sure your viewlet is correctly registered in 'browser/configure.zcml'.
# - If you need it to appear in a specific order inside its viewlet manager,
#   edit 'profiles/default/viewlets.xml' accordingly.
# - Restart Zope.
# - If you edited any file in 'profiles/default/', reinstall your package.
# - Once you're happy with your viewlet implementation, remove any related
#   (unwanted) inline documentation  ;-p

class UofLPersonalBarViewlet(common.PersonalBarViewlet):
    """A custom version of the Personal Bar
    """
    index = ViewPageTemplateFile('personaltools.pt')
    
    def update(self):
        super(UofLPersonalBarViewlet, self).update()
        context = aq_inner(self.context)

        context_state = getMultiAdapter((context, self.request),
                                        name=u'plone_context_state')
        self.object_url = context_state.object_url()
        sm = getSecurityManager()
        self.user_actions = context_state.actions('user')
        self.anonymous = self.portal_state.anonymous()

        if not self.anonymous:
            member = self.portal_state.member()
            userid = member.getId()

            if sm.checkPermission('Portlets: View dashboard', context):
                self.homelink_url = "%s/useractions" % self.navigation_root_url
            else:
                self.homelink_url = "%s/personalize_form" % (
                                        self.navigation_root_url)

            membership = getToolByName(context, 'portal_membership')
            member_info = membership.getMemberInfo(userid)
            # member_info is None if there's no Plone user object, as when
            # using OpenID.
            if member_info:
                fullname = member_info.get('fullname', '')
            else:
                fullname = None
            if fullname:
                self.user_name = fullname
            else:
                self.user_name = userid

class UofLFooterPersonalBarViewlet(common.PersonalBarViewlet):
    """A custom version of the Personal Bar
    """
    index = ViewPageTemplateFile('footer_personaltools.pt')
    
    def update(self):
        super(UofLFooterPersonalBarViewlet, self).update()
        context = aq_inner(self.context)

        context_state = getMultiAdapter((context, self.request),
                                        name=u'plone_context_state')
        self.object_url = context_state.object_url()
        sm = getSecurityManager()
        self.user_actions = context_state.actions('user')
        self.anonymous = self.portal_state.anonymous()

        if not self.anonymous:
            member = self.portal_state.member()
            userid = member.getId()

            if sm.checkPermission('Portlets: View dashboard', context):
                self.homelink_url = "%s/useractions" % self.navigation_root_url
            else:
                self.homelink_url = "%s/personalize_form" % (
                                        self.navigation_root_url)

            membership = getToolByName(context, 'portal_membership')
            member_info = membership.getMemberInfo(userid)
            # member_info is None if there's no Plone user object, as when
            # using OpenID.
            if member_info:
                fullname = member_info.get('fullname', '')
            else:
                fullname = None
            if fullname:
                self.user_name = fullname
            else:
                self.user_name = userid


class UofLHeaderViewlet(ViewletBase):
    """Lookup header option and make it's value available to the view
    """
    index = ViewPageTemplateFile('header.pt')

    def update(self):
        super(UofLHeaderViewlet, self).update()

        registry = getUtility(IRegistry)
        settings = registry.forInterface(IHNFPickerSettings)
        self.uofl_header = settings.site_uofl_header + " uofl"

class UofLFooterViewlet(ViewletBase):
    """Lookup footer option and make it's value available to the view
    """
    index = ViewPageTemplateFile('footer.pt')

    def update(self):
        super(UofLFooterViewlet, self).update()

        registry = getUtility(IRegistry)
        settings = registry.forInterface(IHNFPickerSettings)
        self.uofl_footer = settings.site_uofl_footer
        self.uofl_header = settings.site_uofl_header
