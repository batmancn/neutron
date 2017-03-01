# http://www.cnblogs.com/zhutianshi/p/3898516.html

# 1. resource map
RESOURCE_ATTRIBUTE_MAP = {
    'fabricextensionss': {
        'id': {'allow_post': False, 'allow_put': False,
               'is_visible': True},
        'name': {'allow_post': True, 'allow_put': True,
                          'is_visible': True},
        'tenant_id': {'allow_post': True, 'allow_put': False,
                      'validate': {'type:string': None},
                      'required_by_policy': True,
                      'is_visible': True}
        }
    }

from neutron.api import extensions
from neutron import manager
from neutron.api.v2 import base

class Fabricextension(extensions.ExtensionDescriptor):
    # The name of this class should be the same as the file name
    # The first letter must be changed from lower case to upper case
    # There are a couple of methods and their properties defined in the
    # parent class of this class, ExtensionDescriptor you can check them

    supported_extension_aliases = ['fabric-extensions']

    @classmethod
    def get_name(cls):
        # You can coin a name for this extension
        return "Fabric Extension"

    @classmethod
    def get_alias(cls):
        # This alias will be used by your core_plugin class to load
        # the extension
        return "fabric-extensions"

    @classmethod
    def get_description(cls):
        # A small description about this extension
        return "Fabric extension description"

    @classmethod
    def get_namespace(cls):
        # The XML namespace for this extension
        return "http://docs.openstack.org/ext/fabricextensions/api/v1.0"

    @classmethod
    def get_updated(cls):
        # Specify when was this extension last updated,
        # good for management when there are changes in the design
        return "2014-08-07T00:00:00-00:00"

    @classmethod
    def get_resources(cls):
        # This method registers the URL and the dictionary  of
        # attributes on the neutron-server.
        exts = []
        plugin = manager.NeutronManager.get_plugin()
        resource_name = 'fabricextensions'
        collection_name = '%ss' % resource_name
        params = RESOURCE_ATTRIBUTE_MAP.get(collection_name, dict())
        controller = base.create_resource(collection_name, resource_name,
                                          plugin, params, allow_bulk=False)
        ex = extensions.ResourceExtension(collection_name, controller)
        exts.append(ex)
        return exts
