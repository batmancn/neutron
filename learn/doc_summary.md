Service & Agent:
    - All treat as service
    - 3 kinds:
        -- neutron-server
        -- L2 Agent
        -- L3 Agent
Entry points:
    - setuptool mechanism in entry points and main function.
Eventlet: refer to LEARN.md.
Connecting with database: only neutron-server could do this.
Neutron WSGI/HTTP API layer:
    - Startup: neutron/server/* module. Of course refer to __init__.py first.
ML2 extension manager: ???
quota management and enforcement: ???
API extension(REST API):
    - Guaid Tour: The Neutron Security Group API.
        -- API extension: neutron/extesions/securitygroup.py
        -- database API: neutron/db/securitygroup_db.py
        -- Agent RPC:
            --- plugin RPC: securitygroups_rpc_base.py
Neutron plugin architecture: neutron/neutron_plugin_base_v2.py
Neutron database layer: neutron/db/model_base.py
Authorization policy exforcement: neutron/policy.py
    - request authorization: enforce()
    - response filtering:
Neutron RPC Layer: oslo.messaging(based on amqplib)
    - DHCP Agent call neutron-server:
        -- client RPC API in DHCP Agent: neutron.agent.dhcp.agent.DhcpPluginAPI.
        -- server RPC API in neutron-server: neutron.api.rpc.handlers.dhcp_rpc.DhcpRpcCallback
    - neutron-plugin call DHCP Agent:
        -- client RPC API in neutron-plugin: neutron.api.rpc.agentnotifiers.dhcp_rpc_agent_api.DhcpAgentNotifyApi
        -- server RPC API in DHCP Agent: neutron.agent.dhcp.agent.DhcpAgent
    - other RPC is the same.
Neutron Messaging Callback System: neutron.callbacks
Neutron in-process callbacks: neutron.callbacks
Neutron inter-process callbacks: neutron.api.rpc.callbacks.*
Neutrno L3:
    - architecture: file:///Z:/MyLife/nfv_sdn/nfv_openstack/neutron/doc/build/html/devref/layer3.html
    - L3 function interface: qr-YYY on br-int with vlan_tag 1; qr-XXX on br-int with vlan_tag 2; qg-VVV on br-ex with no vlan_tag. These internal port is just like br0 internal port, connect to linux IP stack.
    - vrouter: just linux IP stack.
L2 Agent Networking:
    - These L2 Agent is work to supply L2 connectivity by different mechanism.
    - VLAN segmentation: file:///Z:/MyLife/nfv_sdn/nfv_openstack/neutron/doc/build/html/devref/openvswitch_agent.html
L2 Networking with linux bridge:
    - Use linux bridge to connect with VMs on hipervisor:
        -- connectivity.
        -- L3HA, https://docs.openstack.org/kilo/networking-guide/scenario_l3ha_lb.html
TBD other L2 fundermantal.
L2 Agent Extension:
    - Manager: neutron.agent.l2.extensions.manager: This module contains a manager that allows to register multiple extensions, and passes handle_port events down to all enabled extensions.
    - Extension: consumer of message from Agent API object, This module defines an abstract extension interface, refer neutron.agent.l2.agent_extension.
    - Agent API object:
