import sqlalchemy as sa

from neutron.db import model_base
from neutron.db import models_v2
from oslo_log import log as logging

LOG = logging.getLogger(__name__)


class FabricNetwork(model_base.BASEV2, models_v2.HasId,
                  model_v2.HasTenant):
    ''' Defines the data model for FabricNetwork.
        as http://www.cnblogs.com/zhutianshi/p/3906228.html said,
        this is to define how to store sttribute(ex. 'name') in DB,
        this is used bellow.
    '''
    name = sa.Column(sa.String(255), nullable=False)


# TBD: ext_sg.FabricNetworkPlugin
# this is APIs for REST API to access DB.
class FabricNetworkDbMixin(ext_sg.FabricNetworkPlugin):
    def create_fabric_network(self):
        LOG.info("create_fabric_network")

    def delete_fabric_network(self):
        LOG.info("delete_fabric_network")

    def get_fabric_network(self):
        LOG.info("get_fabric_network")
