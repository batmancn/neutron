#!/bin/env python

from oslo_config import cfg

OPTS = [cfg.StrOpt('opt1',
    default = 'opt1_default',
    help = 'Name opt1')]

cfg.CONF.register_opts(OPTS)

