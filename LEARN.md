### Reference?

1. https://github.com/batmancn/openstack_code_Neutron.git


### Basic usage?

This is mitaka branch comment.

Same as all openstack system, neutron devide into cli and server. For both part is installed by setuptools, so all code is located in PYTHON_CODE_PATH. For cli and server wrapper command, could refer to ./setup.cfg [entry_points] section.

For architecture, refer to <1> neutron section: cli request to neutron server, server dispatch request to plugins, plugin call agent if neccerry. All communication is json rpc, which is server call plugin by json rpc, plugin call agent by json rpc.

Architecture design point:
- Build install system: setuptool, entry points. setup.cfg ...
- configure system: oslo.config. etc/*.
- IO and event-notifier: eventlet. neutron/cmd/eventlet/*.
- database: only neutron-server connect to database.
- Use RPC to communicate between process. There are 3 kind of RPC: neutron-server RPC, plugin RPC, agent RPC.
- DB architecture is same as WebOVS, which is models/db.
- neutron-server is designed as REST server, and dispatch request to plugin and then call plugin by RPC.
- Kinds of plugins, all is to implement interfaces. So summary interface inherince map is OK.
- Kinds of agent???


### Eventlet library and green thread

Neutron extensively utilizes the eventlet library to provide asynchronous concurrency model to its services. Refer to neutron/cmd/eventlet/__init__.py.

http://eventlet.net/
http://eventlet.net/doc/examples.html

1. use epoll as non-blocking-io; 2. C-Style thread library coding style, Refer to 'Web Crawler Example'; 3. implict dispatch, Refer to 'Web Crawler Example', all user care is just define 'fetch' method and use 'for' loop to get result.


### Configure system

1) file:///Z:/MyLife/nfv_sdn/nfv_openstack/neutron/doc/build/html/devref/api_layer.html
2) http://docs.openstack.org/developer/oslo.config/cfg.html

Architecture:
Configure system devide into 2: reading from *.ini configure files(oslo.config); reading configures and then use it(neutron/neutron/common/config.py). config.py use oslo.config.CONF to create WSGI app, refer to <1)>

oslo.config:
This library is for command line options parse and use(cli_opts); configuration file parse and use(common_opts). For cli_opts, compare to appctl command defined in OVS code. For common_opts, it's configure system.
<2)> is main intruduce page, use this as reference.

config.py:
neutron/neutron/common/config.py use values from oslo.config.CONF which is parsed from api-paste.ini

DIY:
oslo is used .ini files, and refer to README.txt, use command to produce *.ini.sample files, these files is configure we use. Refer to learn/oslo_learn.py.


### Rootwrap? TBD


### Neutron server?

Neutron's WSGI server: file:///Z:/MyLife/nfv_sdn/nfv_openstack/neutron/doc/build/html/devref/api_layer.html.
- Build and init process: entry point 'server_wsgi'.

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
