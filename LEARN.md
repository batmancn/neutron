### Reference?

1. https://github.com/batmancn/openstack_code_Neutron.git


### Basic usage?

This is mitaka branch comment.

Same as all openstack system, neutron devide into cli and server. For both part is installed by setuptools, so all code is located in PYTHON_CODE_PATH. For cli and server wrapper command, could refer to ./setup.cfg [entry_points] section.

For architecture, refer to <1> neutron section: cli request to neutron server, server dispatch request to plugins, plugin call agent if neccerry. All communication is json rpc, which is server call plugin by json rpc, plugin call agent by json rpc.

Architecture design point:
- build/install system, using setup tool, refer to setup.cfg. Init chain is configured in etc folder as entry point.
- configure system using oslo.
- Use RPC to communicate between process. There are 3 kind of RPC: neutron-server RPC, plugin RPC, agent RPC.
- DB architecture is same as WebOVS, which is models/db.
- neutron-server is designed as REST server, and dispatch request to plugin and then call plugin by RPC.
- Kinds of plugins, all is to implement interfaces. So summary interface inherince map is OK.
- Kinds of agent???


### Configure system and oslo?

http://www.choudan.net/2013/11/27/OpenStack-Oslo.config-%E5%AD%A6%E4%B9%A0(%E4%B8%80).html
https://wiki.openstack.org/wiki/Oslo
http://git.openstack.org/cgit/openstack/oslo.config
http://docs.openstack.org/developer/oslo.config/cfg.html

oslo.config library is for command line options parse and use(cli_opts); configuration file parse and use(common_opts). For cli_opts, compare to appctl command defined in OVS code. For common_opts, it's configure system.

http://docs.openstack.org/developer/oslo.config/cfg.html This is main intruduce page, use this as reference.

DIY: oslo is used .ini files, and refer to README.txt, use command to produce *.ini.sample files, these files is configure we use. Refer to learn/oslo_learn.py.


### Rootwrap? TBD


### Neutron server?

Start call trace:
/etc/init.d/neutron-server -> ./neutron/server/__init__.py main() -> wsgi_evenlet.py eventlet_wsgi_server() -> start_api_and_rpc_workers(here start all tasks: api, rpc, all plugins).

Neutron server is to implements REST API, important call trace:
start_api_and_rpc_workers -> service.NeutronApiService -> service.WsgiService -> service._run_wsgi_service (app = ...; wsgi.Server.start(app)) -> api.router.APIRouter (plugin = ...; ext_mager = ...)

Extend API:
Refer to neutron/api/v2


### REST?

routes library:
This is Routing facilities in python web framework, which is URL mapping, refer to https://wiki.python.org/moin/Routing or https://routes.readthedocs.io/en/latest/.

URL-resource mapping:
attribute.py RESOURCE_ATTRIBUTE_MAP. And extend URL-resource mapping, use this.

How to call plugin is unknown???


### Plugin?

Neutron server call plugin by RPC??? to implement facility.

Take ml2-ovs plugin(./neutron/plugins/ml2/drivers/openvswitch) for example. Derived map is: OpenvswitchMechanismDriver -> mech_agent.SimpleAgentMechanismDriverBase -> AgentMechanismDriverBase -> api.MechanismDriver ->
