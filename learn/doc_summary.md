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
