from neutron.db import db_base_plugin_v2
from neutron.openstack.common import log

LOG = log.getLogger(__name__)

# use db_base_plugin_v2.NeutronDbPluginV2 to operate DB.
class FabricPlugin(db_base_plugin_v2.NeutronDbPluginV2):

    def __init__(self):
        LOG.info("FabricPlugin is started.")
