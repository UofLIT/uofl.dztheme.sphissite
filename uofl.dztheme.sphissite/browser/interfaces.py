from plone.theme.interfaces import IDefaultPloneLayer
from zope.viewlet.interfaces import IViewletManager
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletDataProvider
from Products.CMFPlone import PloneMessageFactory as _

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "UofL Base Theme" theme, this interface must be its layer
       (in p4basetheme/viewlets/configure.zcml).
    """

class IUofLHeader(IViewletManager):
    """A custom viewlet manager for the UofL Header
    """

class IUofLFooter(IViewletManager):
    """A custom viewlet manager for the UofL Footer
    """

class IUofLHero(IViewletManager):
    """A custom viewlet manager for Bootstrap rows above the content
    """

class IUofLPreFooter(IViewletManager):
    """A custom viewlet manager for Bootstrap rows below the content
    """

class IUofLPersonalTools(IViewletManager):
    """A custom viewlet manager to provide a provider for rendering the user menu within a viewlet
    """

class IUofLFooterPersonalTools(IViewletManager):
    """A custom viewlet manager to provide a provider for rendering the user menu within a viewlet in the footer
    """

class IUofLHeaderLogo(IViewletManager):
    """A custom viewlet manager to to provide a well for the logo and the ability to customize that logo
    """

class IHeroPortletManager(IPortletManager):
    """A portlet manager that will reside above the content
       For users to be able to add the html to their hero boxes
    """

class IPreFooterPortletManager(IPortletManager):
    """A portlet manager that will reside above the content
       For users to be able to add the html to their hero boxes
    """

class IBootstrapRowPortlet(IPortletDataProvider):
    """A portlet that subclasses static text but renders bootstrap rows for the new portlet managers
    """