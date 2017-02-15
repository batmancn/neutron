from oslo_config import cfg
from oslo_config import types

# 1.
# This is to restrict PortType(1~65535)
PortType = types.Integer(1, 65535)
# This is common options of this command which must be defined, like:
# neutron-server --bind_host=1.1.1.1 --bind_port=6666
common_opts = [
    cfg.StrOpt('bind_host',
               default='0.0.0.0',
               help='IP address to listen on.'),
    cfg.Opt('bind_port',
            type=PortType,
            default=9292,
            help='Port number to listen on.')
]

# 2.
# This is command options.
# Command is the python script itself, like neutron-server.
opts = [
    cfg.StrOpt('option1', default='default_value',
                advanced=True, help='This is help '
                'text.'),
    cfg.PortOpt('option2', default='default_value',
                 help='This is help text.'),
]
# This is to register opts
CONF = cfg.CONF
CONF.register_opts(opts)

# 3.
# ListOpt is 'enabled_apis' could only in ['ec2', 'osapi_compute'].
enabled_apis_opt = cfg.ListOpt('enabled_apis',
                               default=['ec2', 'osapi_compute'],
                               help='List of APIs to enable by default.')

DEFAULT_EXTENSIONS = [
    'nova.api.openstack.compute.contrib.standard_extensions'
]
osapi_compute_extension_opt = cfg.MultiStrOpt('osapi_compute_extension',
                                              default=DEFAULT_EXTENSIONS)

# 4.
# cli_opts, register_cli_opts.
cli_opts = [
    cfg.BoolOpt('verbose',
                short='v',
                default=False,
                help='Print more verbose output.'),
    cfg.BoolOpt('debug',
                short='d',
                default=False,
                help='Print debugging output.'),
]

def add_common_opts(conf):
    conf.register_cli_opts(cli_opts)

# 5.
# The config manager has two CLI options defined by default, –config-file and –config-dir, this is inner code of oslo.config, not user code.
class ConfigOpts(object):
    def __call__(self, ...):
        opts = [
            MultiStrOpt('config-file',
                    ...),
            StrOpt('config-dir',
                   ...),
        ]
        self.register_cli_opts(opts)

# 6. opts groups:
glance-api.conf:
  [DEFAULT]
  bind_port = 9292  # this is DEFAULT grouop
  ...

  [rabbit]
  host = localhost  # this is raddit group
  port = 5672
  use_ssl = False
  userid = guest
  password = guest
  virtual_host = /

# same like these code:
rabbit_group = cfg.OptGroup(name='rabbit',
                            title='RabbitMQ options')

rabbit_host_opt = cfg.StrOpt('host',
                             default='localhost',
                             help='IP/hostname to listen on.'),
rabbit_port_opt = cfg.PortOpt('port',
                              default=5672,
                              help='Port number to listen on.')

def register_rabbit_opts(conf):
    conf.register_group(rabbit_group)
    # options can be registered under a group in either of these ways:
    conf.register_opt(rabbit_host_opt, group=rabbit_group)
    conf.register_opt(rabbit_port_opt, group='rabbit')


# 7. Access options in code, by CONF.XXXX
def start(server, app):
    server.start(app, CONF.bind_port, CONF.bind_host)
