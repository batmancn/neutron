"""
Fabric API extension in neutron-server
"""
from neutron._i18n import _
from neutron.common import exceptions as nexception
from neutron.api.v2 import attributes as attr
from neutron.quota import resource_registry
from neutron.api.v2 import base

# define exceptions
class FabricError(nexception.Invalid):
    message = _("Fabric Normal Error")


# define resource mapping
# Each FABRIC_NETWORKS represents a fabric network.
FABRIC_NETWORKS = "fabric_networks"
RESOURCE_ATTRIBUTE_MAP = {
    FABRIC_NETWORKS = {
        'id': {'allow_post': False, 'allow_put': False,
               'validate': {'type:uuid': None},
               'is_visible': True,
               'primary_key': True},
        'name': {'allow_post': True, 'allow_put': True,
                 'is_visible': True, 'default': '',
                 'validate': {'type:name_not_default': attr.NAME_MAX_LEN}},
        'description': {'allow_post': True, 'allow_put': True,
                        'validate': {'type:string': attr.DESCRIPTION_MAX_LEN},
                        'is_visible': True, 'default': ''},
        'tenant_id': {'allow_post': True, 'allow_put': False,
                      'required_by_policy': True,
                      'validate': {'type:string': attr.TENANT_ID_MAX_LEN},
                      'is_visible': True},
    }
}


# define
class FabricNetwork(extensions.ExtensionDescriptor):
    """Fabric extension."""

    @classmethod
    def get_name(cls):
        return "fabric"

    @classmethod
    def get_alias(cls):
        return "fabric"

    @classmethod
    def get_description(cls):
        return "The fabric extension."

    @classmethod
    def get_updated(cls):
        return "2017-3-2T10:00:00-00:00"

    @classmethod
    def get_resources(cls):
        """Returns Ext Resources."""
        # get keys like 'tenant_id'
        my_plurals = [(key, key[:-1]) for key in RESOURCE_ATTRIBUTE_MAP.keys()]
        # attr is resource attribute, this is used as resource neutron
        # could operate, default is PLURALS, this is to update it by adding
        # keys into it.
        attr.PLURALS.update(dict(my_plurals))
        # define exts
        exts = []
        # get all plugins ???
        plugin = manager.NeutronManager.get_plugin()
        # for resource_name in ['fabric_networks']
        for resource_name in [FABRIC_NETWORKS]:
            # trnaslate resource_name into collection_name,
            # collection_name is what 'get_alins()' return.
            # 'fabric_network' -> 'fabric-networks'
            collection_name = resource_name.replace('_', '-') + "s"
            # params, default []. why '+ "s"' ???
            params = RESOURCE_ATTRIBUTE_MAP.get(resource_name + "s", dict())
            # register resource.
            # resource_registry is wrapper of ResourceRegistry singleton,
            # which is map contains {'ResourceName':'URL', ...} ???
            # which is used in REST app.
            resource_registry.register_resource_by_name(resource_name)
            # create resource is to create REST resource.
            # @collection_name: 'fabric-networks'
            # @resource_name: 'fabric_networks'
            # @plugin: [all plugins]
            # @params: ['id', ...]
            controller = base.create_resource(collection_name,
                                              resource_name,
                                              plugin, params, allow_bulk=True,
                                              allow_pagination=True,
                                              allow_sorting=True)

            ex = extensions.ResourceExtension(collection_name,
                                              controller,
                                              attr_map=params)
            exts.append(ex)

        return exts

    def update_attributes_map(self, attributes):
        super(Securitygroup, self).update_attributes_map(
            attributes, extension_attrs_map=RESOURCE_ATTRIBUTE_MAP)

    def get_extended_resources(self, version):
        if version == "2.0":
            return dict(list(EXTENDED_ATTRIBUTES_2_0.items()) +
                        list(RESOURCE_ATTRIBUTE_MAP.items()))
        else:
            return {}
