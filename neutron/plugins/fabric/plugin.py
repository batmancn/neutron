from neutron import neutron_plugin_base_v2
from neutron.openstack.common import log

LOG = log.getLogger(__name__)

class FabricPlugin(neutron_plugin_base_v2.NeutronPluginBaseV2):
    def __init__(self):
        LOG.info("FabricPlugin is started.")

    def create_network(self, context, network):
        # Create a network by using data from network dictionary
        # Send back a dictionary to display created network's info
        return network

    def update_network(self, context, id, network):
        # Update a created network matched by id with
        # data in the network dictionary. Send back a
        # dictionary to display the network's updated info
        return network

    def get_network(self, context, id, fields=None):
        network = {}
        # List information of a specific network matched by id
        # and return it in a form of dictionary
        return network

    def get_networks(self, context, filters=None, fields=None):
        network = {}
        # List all networks that are active
        return network

    def delete_network(self, context, id):
        # Delete a specific network matched by id
        # return back the id of the network.
        return id
