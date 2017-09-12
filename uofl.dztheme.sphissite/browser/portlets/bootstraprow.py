from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.portlet.static import PloneMessageFactory as _
from zope.component import getUtility
from plone.i18n.normalizer.interfaces import IIDNormalizer

# Import the base portlet module whose properties we will modify
from plone.portlet.static import static

class IBootstrapRowPortlet(static.IStaticPortlet):
    """ Defines a new portlet "Bootstrap Row" which takes properties of the existing static text portlet. """
    pass

class BootstrapRowRenderer(static.Renderer):
    """ Overrides static.pt in the rendering of the portlet. """
    render = ViewPageTemplateFile('bootstraprow.pt')

    def css_class(self):
        header = self.data.header
        normalizer = getUtility(IIDNormalizer)
        return "portlet-bootstraprow-%s" % normalizer.normalize(header)

    def portlet_title(self):
        return self.data.header

class BootstrapRowAssignment(static.Assignment):
    """ Assigner for bootstrap row portlet. """
    implements(IBootstrapRowPortlet)

class BootstrapRowAddForm(static.AddForm):
    """ Make sure that add form creates instances of our custom portlet instead of the base class portlet. """
    def create(self, data):
        return BootstrapRowAssignment(**data)
