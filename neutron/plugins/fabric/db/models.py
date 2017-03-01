import sqlalchemy as sa

from neutron.db import model_base
from neutron.db import models_v2

# model_base.BASEV2 is SQL base,
# refer http://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/api.html
#
# models_v2.HasId is class HasId(object) in model_base.py
# model_v2.HasTenant is class HasTenant(object) in model_base.py
class MyExtension(model_base.BASEV2, models_v2.HasId,
                  model_v2.HasTenant):
    ''' Defines the data model for my extension '''
    name = sa.Column(sa.String(255), nullable=False)
