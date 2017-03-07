from neutron.db.fabric_db import FabricNetworkDbMixin

class TestFabricDb(object):
    def test_create_fabric_network(self):
        fdbmix = FabricNetworkDbMixin()
        fdbmix.create_fabric_network()
