1. first run 'tox' to prepare enviroment.



gateway@gateway-20150605:~/MyLife/nfv_sdn/nfv_openstack/neutron$ python ./setup.py build
running build
running build_py
creating build
creating build/lib.linux-i686-2.7
creating build/lib.linux-i686-2.7/neutron
creating build/lib.linux-i686-2.7/neutron/services
creating build/lib.linux-i686-2.7/neutron/services/flavors

copying neutron/services/flavors/flavors_plugin.py -> build/lib.linux-i686-2.7/neutron/services/flavors
copying neutron/services/flavors/__init__.py -> build/lib.linux-i686-2.7/neutron/services/flavors

creating build/lib.linux-i686-2.7/neutron/plugins
creating build/lib.linux-i686-2.7/neutron/plugins/ml2
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/linuxbridge

copying neutron/plugins/ml2/drivers/linuxbridge/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/linuxbridge
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/linuxbridge/agent
copying neutron/plugins/ml2/drivers/linuxbridge/agent/arp_protect.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/linuxbridge/agent
copying neutron/plugins/ml2/drivers/linuxbridge/agent/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/linuxbridge/agent
copying neutron/plugins/ml2/drivers/linuxbridge/agent/linuxbridge_neutron_agent.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/linuxbridge/agent

creating build/lib.linux-i686-2.7/neutron/api
creating build/lib.linux-i686-2.7/neutron/api/rpc
copying neutron/api/rpc/__init__.py -> build/lib.linux-i686-2.7/neutron/api/rpc

creating build/lib.linux-i686-2.7/neutron/tests
creating build/lib.linux-i686-2.7/neutron/tests/unit
creating build/lib.linux-i686-2.7/neutron/tests/unit/services
creating build/lib.linux-i686-2.7/neutron/tests/unit/services/qos

copying neutron/tests/unit/services/qos/test_qos_plugin.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/qos
copying neutron/tests/unit/services/qos/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/qos
copying neutron/tests/unit/services/qos/base.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/qos


creating build/lib.linux-i686-2.7/neutron/db
creating build/lib.linux-i686-2.7/neutron/db/migration
creating build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/nsxv_initial_opts.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/metering_init_ops.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/ovs_init_ops.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/external.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/firewall_init_ops.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/other_plugins_init_ops.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/lb_init_ops.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/agent_init_ops.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/vmware_init_ops.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/loadbalancer_init_ops.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/nuage_init_opts.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/secgroup_init_ops.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/core_init_ops.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/cisco_init_ops.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/l3_init_ops.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/vpn_init_ops.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/portsec_init_ops.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/env.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/other_extensions_init_ops.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/ml2_init_ops.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/dvr_init_opts.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/nec_init_ops.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/brocade_init_ops.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
copying neutron/db/migration/alembic_migrations/__init__.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations

creating build/lib.linux-i686-2.7/neutron/db/metering
copying neutron/db/metering/metering_rpc.py -> build/lib.linux-i686-2.7/neutron/db/metering
copying neutron/db/metering/metering_db.py -> build/lib.linux-i686-2.7/neutron/db/metering
copying neutron/db/metering/__init__.py -> build/lib.linux-i686-2.7/neutron/db/metering

creating build/lib.linux-i686-2.7/neutron/services/fabric
copying neutron/services/fabric/__init__.py -> build/lib.linux-i686-2.7/neutron/services/fabric

creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/extensions
copying neutron/tests/unit/plugins/ml2/extensions/fake_extension.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/extensions
copying neutron/tests/unit/plugins/ml2/extensions/test_port_security.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/extensions
copying neutron/tests/unit/plugins/ml2/extensions/test_dns_integration.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/extensions
copying neutron/tests/unit/plugins/ml2/extensions/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/extensions

creating build/lib.linux-i686-2.7/neutron/tests/functional
copying neutron/tests/functional/test_service.py -> build/lib.linux-i686-2.7/neutron/tests/functional
copying neutron/tests/functional/test_server.py -> build/lib.linux-i686-2.7/neutron/tests/functional
copying neutron/tests/functional/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional
copying neutron/tests/functional/base.py -> build/lib.linux-i686-2.7/neutron/tests/functional

creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/extension_drivers
copying neutron/plugins/ml2/drivers/openvswitch/agent/extension_drivers/qos_driver.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/extension_drivers
copying neutron/plugins/ml2/drivers/openvswitch/agent/extension_drivers/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/extension_drivers

creating build/lib.linux-i686-2.7/neutron/plugins/common
copying neutron/plugins/common/utils.py -> build/lib.linux-i686-2.7/neutron/plugins/common
copying neutron/plugins/common/constants.py -> build/lib.linux-i686-2.7/neutron/plugins/common
copying neutron/plugins/common/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/common
copying neutron/plugins/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins

creating build/lib.linux-i686-2.7/neutron/services/metering
creating build/lib.linux-i686-2.7/neutron/services/metering/drivers
creating build/lib.linux-i686-2.7/neutron/services/metering/drivers/noop
copying neutron/services/metering/drivers/noop/noop_driver.py -> build/lib.linux-i686-2.7/neutron/services/metering/drivers/noop
copying neutron/services/metering/drivers/noop/__init__.py -> build/lib.linux-i686-2.7/neutron/services/metering/drivers/noop

creating build/lib.linux-i686-2.7/neutron/tests/functional/plugins
creating build/lib.linux-i686-2.7/neutron/tests/functional/plugins/ml2
creating build/lib.linux-i686-2.7/neutron/tests/functional/plugins/ml2/drivers
copying neutron/tests/functional/plugins/ml2/drivers/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/plugins/ml2/drivers

creating build/lib.linux-i686-2.7/neutron/pecan_wsgi
creating build/lib.linux-i686-2.7/neutron/pecan_wsgi/controllers
copying neutron/pecan_wsgi/controllers/router.py -> build/lib.linux-i686-2.7/neutron/pecan_wsgi/controllers
copying neutron/pecan_wsgi/controllers/quota.py -> build/lib.linux-i686-2.7/neutron/pecan_wsgi/controllers
copying neutron/pecan_wsgi/controllers/utils.py -> build/lib.linux-i686-2.7/neutron/pecan_wsgi/controllers
copying neutron/pecan_wsgi/controllers/root.py -> build/lib.linux-i686-2.7/neutron/pecan_wsgi/controllers
copying neutron/pecan_wsgi/controllers/resource.py -> build/lib.linux-i686-2.7/neutron/pecan_wsgi/controllers
copying neutron/pecan_wsgi/controllers/extensions.py -> build/lib.linux-i686-2.7/neutron/pecan_wsgi/controllers
copying neutron/pecan_wsgi/controllers/__init__.py -> build/lib.linux-i686-2.7/neutron/pecan_wsgi/controllers

creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/mech_sriov
copying neutron/plugins/ml2/drivers/mech_sriov/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/mech_sriov

creating build/lib.linux-i686-2.7/neutron/services/metering/agents
copying neutron/services/metering/agents/metering_agent.py -> build/lib.linux-i686-2.7/neutron/services/metering/agents
copying neutron/services/metering/agents/__init__.py -> build/lib.linux-i686-2.7/neutron/services/metering/agents

creating build/lib.linux-i686-2.7/neutron/agent
creating build/lib.linux-i686-2.7/neutron/agent/ovsdb
creating build/lib.linux-i686-2.7/neutron/agent/ovsdb/native
copying neutron/agent/ovsdb/native/idlutils.py -> build/lib.linux-i686-2.7/neutron/agent/ovsdb/native
copying neutron/agent/ovsdb/native/commands.py -> build/lib.linux-i686-2.7/neutron/agent/ovsdb/native
copying neutron/agent/ovsdb/native/helpers.py -> build/lib.linux-i686-2.7/neutron/agent/ovsdb/native
copying neutron/agent/ovsdb/native/connection.py -> build/lib.linux-i686-2.7/neutron/agent/ovsdb/native
copying neutron/agent/ovsdb/native/__init__.py -> build/lib.linux-i686-2.7/neutron/agent/ovsdb/native

creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/mech_sriov
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/mech_sriov/agent
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/mech_sriov/agent/extension_drivers
copying neutron/tests/unit/plugins/ml2/drivers/mech_sriov/agent/extension_drivers/test_qos_driver.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/mech_sriov/agent/extension_drivers
copying neutron/tests/unit/plugins/ml2/drivers/mech_sriov/agent/extension_drivers/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/mech_sriov/agent/extension_drivers
creating build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/daemon.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/ip_conntrack.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/interface.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/ipset_manager.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/bridge_lib.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/ra.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/external_process.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/ovsdb_monitor.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/utils.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/pd.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/ip_monitor.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/dhcp.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/iptables_firewall.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/ip_link_support.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/tc_lib.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/polling.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/keepalived.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/ip_lib.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/pd_driver.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/iptables_manager.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/async_process.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/iptables_comments.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/__init__.py -> build/lib.linux-i686-2.7/neutron/agent/linux
copying neutron/agent/linux/dibbler.py -> build/lib.linux-i686-2.7/neutron/agent/linux
creating build/lib.linux-i686-2.7/neutron/services/rbac
copying neutron/services/rbac/__init__.py -> build/lib.linux-i686-2.7/neutron/services/rbac
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/l2pop
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/l2pop/rpc_manager
copying neutron/plugins/ml2/drivers/l2pop/rpc_manager/l2population_rpc.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/l2pop/rpc_manager
copying neutron/plugins/ml2/drivers/l2pop/rpc_manager/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/l2pop/rpc_manager
creating build/lib.linux-i686-2.7/neutron/db/quota
copying neutron/db/quota/api.py -> build/lib.linux-i686-2.7/neutron/db/quota
copying neutron/db/quota/models.py -> build/lib.linux-i686-2.7/neutron/db/quota
copying neutron/db/quota/driver.py -> build/lib.linux-i686-2.7/neutron/db/quota
copying neutron/db/quota/__init__.py -> build/lib.linux-i686-2.7/neutron/db/quota
creating build/lib.linux-i686-2.7/neutron/tests/unit/agent
creating build/lib.linux-i686-2.7/neutron/tests/unit/agent/common
copying neutron/tests/unit/agent/common/test_ovs_lib.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/common
copying neutron/tests/unit/agent/common/test_polling.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/common
copying neutron/tests/unit/agent/common/test_utils.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/common
copying neutron/tests/unit/agent/common/test_config.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/common
copying neutron/tests/unit/agent/common/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/common
creating build/lib.linux-i686-2.7/neutron/tests/unit/services/qos/notification_drivers
copying neutron/tests/unit/services/qos/notification_drivers/test_manager.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/qos/notification_drivers
copying neutron/tests/unit/services/qos/notification_drivers/dummy.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/qos/notification_drivers
copying neutron/tests/unit/services/qos/notification_drivers/test_message_queue.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/qos/notification_drivers
copying neutron/tests/unit/services/qos/notification_drivers/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/qos/notification_drivers
creating build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
creating build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux/openvswitch_firewall
copying neutron/tests/unit/agent/linux/openvswitch_firewall/test_rules.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux/openvswitch_firewall
copying neutron/tests/unit/agent/linux/openvswitch_firewall/test_firewall.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux/openvswitch_firewall
copying neutron/tests/unit/agent/linux/openvswitch_firewall/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux/openvswitch_firewall
copying neutron/agent/ovsdb/impl_idl.py -> build/lib.linux-i686-2.7/neutron/agent/ovsdb
copying neutron/agent/ovsdb/api.py -> build/lib.linux-i686-2.7/neutron/agent/ovsdb
copying neutron/agent/ovsdb/impl_vsctl.py -> build/lib.linux-i686-2.7/neutron/agent/ovsdb
copying neutron/agent/ovsdb/__init__.py -> build/lib.linux-i686-2.7/neutron/agent/ovsdb
creating build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_security_groups.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_address_scopes_negative.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_security_groups_negative.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_auto_allocated_topology.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_floating_ips.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_metering_extensions.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_networks.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/clients.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_timestamp.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_routers.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_routers_negative.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_subnetpools_negative.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_network_ip_availability.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_extension_driver_port_security.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_allowed_address_pair.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_flavors_extensions.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_bgp_speaker_extensions.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/base_routers.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/base_security_groups.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_service_type_management.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_ports.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_bgp_speaker_extensions_negative.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_floating_ips_negative.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_address_scopes.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_dhcp_ipv6.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_subnetpools.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/base.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_qos.py -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/api/test_extra_dhcp_options.py -> build/lib.linux-i686-2.7/neutron/tests/api
creating build/lib.linux-i686-2.7/neutron/hacking
copying neutron/hacking/checks.py -> build/lib.linux-i686-2.7/neutron/hacking
copying neutron/hacking/__init__.py -> build/lib.linux-i686-2.7/neutron/hacking
creating build/lib.linux-i686-2.7/neutron/db/migration/models
copying neutron/db/migration/models/__init__.py -> build/lib.linux-i686-2.7/neutron/db/migration/models
copying neutron/db/migration/models/head.py -> build/lib.linux-i686-2.7/neutron/db/migration/models
creating build/lib.linux-i686-2.7/neutron/tests/unit/api
creating build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc
copying neutron/tests/unit/api/rpc/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc
creating build/lib.linux-i686-2.7/neutron/services/auto_allocate
copying neutron/services/auto_allocate/plugin.py -> build/lib.linux-i686-2.7/neutron/services/auto_allocate
copying neutron/services/auto_allocate/exceptions.py -> build/lib.linux-i686-2.7/neutron/services/auto_allocate
copying neutron/services/auto_allocate/db.py -> build/lib.linux-i686-2.7/neutron/services/auto_allocate
copying neutron/services/auto_allocate/models.py -> build/lib.linux-i686-2.7/neutron/services/auto_allocate
copying neutron/services/auto_allocate/__init__.py -> build/lib.linux-i686-2.7/neutron/services/auto_allocate
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/l2pop
copying neutron/tests/unit/plugins/ml2/drivers/l2pop/test_db.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/l2pop
copying neutron/tests/unit/plugins/ml2/drivers/l2pop/test_mech_driver.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/l2pop
copying neutron/tests/unit/plugins/ml2/drivers/l2pop/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/l2pop
creating build/lib.linux-i686-2.7/neutron/tests/functional/services
copying neutron/tests/functional/services/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/services
creating build/lib.linux-i686-2.7/neutron/tests/functional/sanity
copying neutron/tests/functional/sanity/test_sanity.py -> build/lib.linux-i686-2.7/neutron/tests/functional/sanity
copying neutron/tests/functional/sanity/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/sanity
creating build/lib.linux-i686-2.7/neutron/tests/unit/services/metering
creating build/lib.linux-i686-2.7/neutron/tests/unit/services/metering/drivers
copying neutron/tests/unit/services/metering/drivers/test_iptables.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/metering/drivers
copying neutron/tests/unit/services/metering/drivers/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/metering/drivers
creating build/lib.linux-i686-2.7/neutron/services/firewall
creating build/lib.linux-i686-2.7/neutron/services/firewall/agents
creating build/lib.linux-i686-2.7/neutron/services/firewall/agents/l3reference
copying neutron/services/firewall/agents/l3reference/firewall_l3_agent.py -> build/lib.linux-i686-2.7/neutron/services/firewall/agents/l3reference
copying neutron/services/firewall/agents/l3reference/__init__.py -> build/lib.linux-i686-2.7/neutron/services/firewall/agents/l3reference
creating build/lib.linux-i686-2.7/neutron/agent/l2
copying neutron/agent/l2/agent_extension.py -> build/lib.linux-i686-2.7/neutron/agent/l2
copying neutron/agent/l2/__init__.py -> build/lib.linux-i686-2.7/neutron/agent/l2
creating build/lib.linux-i686-2.7/neutron/agent/l3
copying neutron/agent/l3/namespace_manager.py -> build/lib.linux-i686-2.7/neutron/agent/l3
copying neutron/agent/l3/link_local_allocator.py -> build/lib.linux-i686-2.7/neutron/agent/l3
copying neutron/agent/l3/keepalived_state_change.py -> build/lib.linux-i686-2.7/neutron/agent/l3
copying neutron/agent/l3/dvr_router_base.py -> build/lib.linux-i686-2.7/neutron/agent/l3
copying neutron/agent/l3/config.py -> build/lib.linux-i686-2.7/neutron/agent/l3
copying neutron/agent/l3/legacy_router.py -> build/lib.linux-i686-2.7/neutron/agent/l3
copying neutron/agent/l3/dvr_fip_ns.py -> build/lib.linux-i686-2.7/neutron/agent/l3
copying neutron/agent/l3/namespaces.py -> build/lib.linux-i686-2.7/neutron/agent/l3
copying neutron/agent/l3/router_processing_queue.py -> build/lib.linux-i686-2.7/neutron/agent/l3
copying neutron/agent/l3/agent.py -> build/lib.linux-i686-2.7/neutron/agent/l3
copying neutron/agent/l3/dvr_local_router.py -> build/lib.linux-i686-2.7/neutron/agent/l3
copying neutron/agent/l3/dvr_edge_router.py -> build/lib.linux-i686-2.7/neutron/agent/l3
copying neutron/agent/l3/router_info.py -> build/lib.linux-i686-2.7/neutron/agent/l3
copying neutron/agent/l3/dvr.py -> build/lib.linux-i686-2.7/neutron/agent/l3
copying neutron/agent/l3/ha.py -> build/lib.linux-i686-2.7/neutron/agent/l3
copying neutron/agent/l3/dvr_snat_ns.py -> build/lib.linux-i686-2.7/neutron/agent/l3
copying neutron/agent/l3/fip_rule_priority_allocator.py -> build/lib.linux-i686-2.7/neutron/agent/l3
copying neutron/agent/l3/ha_router.py -> build/lib.linux-i686-2.7/neutron/agent/l3
copying neutron/agent/l3/item_allocator.py -> build/lib.linux-i686-2.7/neutron/agent/l3
copying neutron/agent/l3/dvr_edge_ha_router.py -> build/lib.linux-i686-2.7/neutron/agent/l3
copying neutron/agent/l3/__init__.py -> build/lib.linux-i686-2.7/neutron/agent/l3
creating build/lib.linux-i686-2.7/neutron/tests/unit/debug
copying neutron/tests/unit/debug/test_commands.py -> build/lib.linux-i686-2.7/neutron/tests/unit/debug
copying neutron/tests/unit/debug/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/debug
creating build/lib.linux-i686-2.7/neutron/tests/unit/common
copying neutron/tests/unit/common/test_ipv6_utils.py -> build/lib.linux-i686-2.7/neutron/tests/unit/common
copying neutron/tests/unit/common/test_rpc.py -> build/lib.linux-i686-2.7/neutron/tests/unit/common
copying neutron/tests/unit/common/test_utils.py -> build/lib.linux-i686-2.7/neutron/tests/unit/common
copying neutron/tests/unit/common/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/common
creating build/lib.linux-i686-2.7/neutron/tests/functional/common
copying neutron/tests/functional/common/test_utils.py -> build/lib.linux-i686-2.7/neutron/tests/functional/common
copying neutron/tests/functional/common/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/common
copying neutron/tests/unit/plugins/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins
creating build/lib.linux-i686-2.7/neutron/agent/common
copying neutron/agent/common/config.py -> build/lib.linux-i686-2.7/neutron/agent/common
copying neutron/agent/common/utils.py -> build/lib.linux-i686-2.7/neutron/agent/common
copying neutron/agent/common/base_polling.py -> build/lib.linux-i686-2.7/neutron/agent/common
copying neutron/agent/common/ovs_lib.py -> build/lib.linux-i686-2.7/neutron/agent/common
copying neutron/agent/common/polling.py -> build/lib.linux-i686-2.7/neutron/agent/common
copying neutron/agent/common/ip_lib.py -> build/lib.linux-i686-2.7/neutron/agent/common
copying neutron/agent/common/__init__.py -> build/lib.linux-i686-2.7/neutron/agent/common
creating build/lib.linux-i686-2.7/neutron/cmd
creating build/lib.linux-i686-2.7/neutron/cmd/eventlet
creating build/lib.linux-i686-2.7/neutron/cmd/eventlet/agents
copying neutron/cmd/eventlet/agents/metadata.py -> build/lib.linux-i686-2.7/neutron/cmd/eventlet/agents
copying neutron/cmd/eventlet/agents/bgp_dragent.py -> build/lib.linux-i686-2.7/neutron/cmd/eventlet/agents
copying neutron/cmd/eventlet/agents/dhcp.py -> build/lib.linux-i686-2.7/neutron/cmd/eventlet/agents
copying neutron/cmd/eventlet/agents/l3.py -> build/lib.linux-i686-2.7/neutron/cmd/eventlet/agents
copying neutron/cmd/eventlet/agents/metadata_proxy.py -> build/lib.linux-i686-2.7/neutron/cmd/eventlet/agents
copying neutron/cmd/eventlet/agents/__init__.py -> build/lib.linux-i686-2.7/neutron/cmd/eventlet/agents
creating build/lib.linux-i686-2.7/neutron/services/bgp
creating build/lib.linux-i686-2.7/neutron/services/bgp/common
copying neutron/services/bgp/common/opts.py -> build/lib.linux-i686-2.7/neutron/services/bgp/common
copying neutron/services/bgp/common/constants.py -> build/lib.linux-i686-2.7/neutron/services/bgp/common
copying neutron/services/bgp/common/__init__.py -> build/lib.linux-i686-2.7/neutron/services/bgp/common
copying neutron/tests/functional/plugins/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/plugins
creating build/lib.linux-i686-2.7/neutron/api/rpc/agentnotifiers
copying neutron/api/rpc/agentnotifiers/bgp_dr_rpc_agent_api.py -> build/lib.linux-i686-2.7/neutron/api/rpc/agentnotifiers
copying neutron/api/rpc/agentnotifiers/metering_rpc_agent_api.py -> build/lib.linux-i686-2.7/neutron/api/rpc/agentnotifiers
copying neutron/api/rpc/agentnotifiers/dhcp_rpc_agent_api.py -> build/lib.linux-i686-2.7/neutron/api/rpc/agentnotifiers
copying neutron/api/rpc/agentnotifiers/l3_rpc_agent_api.py -> build/lib.linux-i686-2.7/neutron/api/rpc/agentnotifiers
copying neutron/api/rpc/agentnotifiers/__init__.py -> build/lib.linux-i686-2.7/neutron/api/rpc/agentnotifiers
creating build/lib.linux-i686-2.7/neutron/services/bgp/agent
copying neutron/services/bgp/agent/config.py -> build/lib.linux-i686-2.7/neutron/services/bgp/agent
copying neutron/services/bgp/agent/bgp_dragent.py -> build/lib.linux-i686-2.7/neutron/services/bgp/agent
copying neutron/services/bgp/agent/entry.py -> build/lib.linux-i686-2.7/neutron/services/bgp/agent
copying neutron/services/bgp/agent/__init__.py -> build/lib.linux-i686-2.7/neutron/services/bgp/agent
creating build/lib.linux-i686-2.7/neutron/tests/tempest
copying neutron/tests/tempest/config.py -> build/lib.linux-i686-2.7/neutron/tests/tempest
copying neutron/tests/tempest/exceptions.py -> build/lib.linux-i686-2.7/neutron/tests/tempest
copying neutron/tests/tempest/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/tempest
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/mech_sriov/agent
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/mech_sriov/agent/extension_drivers
copying neutron/plugins/ml2/drivers/mech_sriov/agent/extension_drivers/qos_driver.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/mech_sriov/agent/extension_drivers
copying neutron/plugins/ml2/drivers/mech_sriov/agent/extension_drivers/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/mech_sriov/agent/extension_drivers
creating build/lib.linux-i686-2.7/neutron/tests/unit/db
creating build/lib.linux-i686-2.7/neutron/tests/unit/db/metering
copying neutron/tests/unit/db/metering/test_metering_db.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db/metering
copying neutron/tests/unit/db/metering/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db/metering
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/agent
copying neutron/tests/unit/plugins/ml2/drivers/agent/test__common_agent.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/agent
copying neutron/tests/unit/plugins/ml2/drivers/agent/test__agent_manager_base.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/agent
copying neutron/tests/unit/plugins/ml2/drivers/agent/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/agent
copying neutron/db/db_base_plugin_v2.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/l3_dvrscheduler_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/ipam_pluggable_backend.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/external_net_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/agentschedulers_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/rbac_db_models.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/quota_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/portsecurity_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/dns_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/dvr_mac_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/portsecurity_db_common.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/bgp_dragentscheduler_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/common_db_mixin.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/agents_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/api.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/ipam_backend_mixin.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/securitygroups_rpc_base.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/flavors_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/standardattrdescription_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/extraroute_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/l3_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/l3_dvr_ha_scheduler_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/l3_hascheduler_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/l3_attrs_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/allowedaddresspairs_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/tag_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/db_base_plugin_common.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/l3_agentschedulers_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/extradhcpopt_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/vlantransparent_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/rbac_db_mixin.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/network_ip_availability_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/l3_hamode_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/l3_dvr_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/models_v2.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/securitygroups_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/bgp_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/model_base.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/address_scope_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/ipam_non_pluggable_backend.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/servicetype_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/sqlalchemyutils.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/l3_gwmode_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/netmtu_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/sqlalchemytypes.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/portbindings_db.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/portbindings_base.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/db/__init__.py -> build/lib.linux-i686-2.7/neutron/db
copying neutron/plugins/ml2/drivers/l2pop/config.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/l2pop
copying neutron/plugins/ml2/drivers/l2pop/db.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/l2pop
copying neutron/plugins/ml2/drivers/l2pop/rpc.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/l2pop
copying neutron/plugins/ml2/drivers/l2pop/mech_driver.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/l2pop
copying neutron/plugins/ml2/drivers/l2pop/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/l2pop
creating build/lib.linux-i686-2.7/neutron/tests/functional/agent
creating build/lib.linux-i686-2.7/neutron/tests/functional/agent/l2
creating build/lib.linux-i686-2.7/neutron/tests/functional/agent/l2/extensions
copying neutron/tests/functional/agent/l2/extensions/test_ovs_agent_qos_extension.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/l2/extensions
copying neutron/tests/functional/agent/l2/extensions/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/l2/extensions
creating build/lib.linux-i686-2.7/neutron/ipam
creating build/lib.linux-i686-2.7/neutron/ipam/drivers
creating build/lib.linux-i686-2.7/neutron/ipam/drivers/neutrondb_ipam
copying neutron/ipam/drivers/neutrondb_ipam/driver.py -> build/lib.linux-i686-2.7/neutron/ipam/drivers/neutrondb_ipam
copying neutron/ipam/drivers/neutrondb_ipam/db_models.py -> build/lib.linux-i686-2.7/neutron/ipam/drivers/neutrondb_ipam
copying neutron/ipam/drivers/neutrondb_ipam/__init__.py -> build/lib.linux-i686-2.7/neutron/ipam/drivers/neutrondb_ipam
copying neutron/ipam/drivers/neutrondb_ipam/db_api.py -> build/lib.linux-i686-2.7/neutron/ipam/drivers/neutrondb_ipam
creating build/lib.linux-i686-2.7/neutron/tests/functional/plugins/ml2/drivers/macvtap
copying neutron/tests/functional/plugins/ml2/drivers/macvtap/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/plugins/ml2/drivers/macvtap
copying neutron/services/firewall/__init__.py -> build/lib.linux-i686-2.7/neutron/services/firewall
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/linuxbridge/agent/extension_drivers
copying neutron/plugins/ml2/drivers/linuxbridge/agent/extension_drivers/qos_driver.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/linuxbridge/agent/extension_drivers
copying neutron/plugins/ml2/drivers/linuxbridge/agent/extension_drivers/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/linuxbridge/agent/extension_drivers
creating build/lib.linux-i686-2.7/neutron/tests/unit/tests
creating build/lib.linux-i686-2.7/neutron/tests/unit/tests/example
creating build/lib.linux-i686-2.7/neutron/tests/unit/tests/example/dir
copying neutron/tests/unit/tests/example/dir/example_module.py -> build/lib.linux-i686-2.7/neutron/tests/unit/tests/example/dir
copying neutron/tests/unit/tests/example/dir/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/tests/example/dir
creating build/lib.linux-i686-2.7/neutron/db/availability_zone
copying neutron/db/availability_zone/network.py -> build/lib.linux-i686-2.7/neutron/db/availability_zone
copying neutron/db/availability_zone/router.py -> build/lib.linux-i686-2.7/neutron/db/availability_zone
copying neutron/db/availability_zone/__init__.py -> build/lib.linux-i686-2.7/neutron/db/availability_zone
copying neutron/tests/unit/plugins/ml2/drivers/mech_sriov/agent/test_pci_lib.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/mech_sriov/agent
copying neutron/tests/unit/plugins/ml2/drivers/mech_sriov/agent/test_sriov_nic_agent.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/mech_sriov/agent
copying neutron/tests/unit/plugins/ml2/drivers/mech_sriov/agent/test_eswitch_manager.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/mech_sriov/agent
copying neutron/tests/unit/plugins/ml2/drivers/mech_sriov/agent/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/mech_sriov/agent
creating build/lib.linux-i686-2.7/neutron/tests/functional/services/l3_router
copying neutron/tests/functional/services/l3_router/test_l3_dvr_router_plugin.py -> build/lib.linux-i686-2.7/neutron/tests/functional/services/l3_router
copying neutron/tests/functional/services/l3_router/test_l3_dvr_ha_router_plugin.py -> build/lib.linux-i686-2.7/neutron/tests/functional/services/l3_router
copying neutron/tests/functional/services/l3_router/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/services/l3_router
creating build/lib.linux-i686-2.7/neutron/tests/api/admin
copying neutron/tests/api/admin/test_floating_ips_admin_actions.py -> build/lib.linux-i686-2.7/neutron/tests/api/admin
copying neutron/tests/api/admin/test_quotas.py -> build/lib.linux-i686-2.7/neutron/tests/api/admin
copying neutron/tests/api/admin/test_l3_agent_scheduler.py -> build/lib.linux-i686-2.7/neutron/tests/api/admin
copying neutron/tests/api/admin/test_agent_management.py -> build/lib.linux-i686-2.7/neutron/tests/api/admin
copying neutron/tests/api/admin/test_routers_dvr.py -> build/lib.linux-i686-2.7/neutron/tests/api/admin
copying neutron/tests/api/admin/test_external_network_extension.py -> build/lib.linux-i686-2.7/neutron/tests/api/admin
copying neutron/tests/api/admin/test_extension_driver_port_security_admin.py -> build/lib.linux-i686-2.7/neutron/tests/api/admin
copying neutron/tests/api/admin/test_dhcp_agent_scheduler.py -> build/lib.linux-i686-2.7/neutron/tests/api/admin
copying neutron/tests/api/admin/test_shared_network_extension.py -> build/lib.linux-i686-2.7/neutron/tests/api/admin
copying neutron/tests/api/admin/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/api/admin
creating build/lib.linux-i686-2.7/neutron/tests/unit/objects
copying neutron/tests/unit/objects/test_common_types.py -> build/lib.linux-i686-2.7/neutron/tests/unit/objects
copying neutron/tests/unit/objects/test_objects.py -> build/lib.linux-i686-2.7/neutron/tests/unit/objects
copying neutron/tests/unit/objects/test_rbac_db.py -> build/lib.linux-i686-2.7/neutron/tests/unit/objects
copying neutron/tests/unit/objects/test_base.py -> build/lib.linux-i686-2.7/neutron/tests/unit/objects
copying neutron/tests/unit/objects/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/objects
creating build/lib.linux-i686-2.7/neutron/plugins/hyperv
copying neutron/plugins/hyperv/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/hyperv
copying neutron/plugins/ml2/drivers/mech_sriov/agent/sriov_nic_agent.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/mech_sriov/agent
copying neutron/plugins/ml2/drivers/mech_sriov/agent/pci_lib.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/mech_sriov/agent
copying neutron/plugins/ml2/drivers/mech_sriov/agent/eswitch_manager.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/mech_sriov/agent
copying neutron/plugins/ml2/drivers/mech_sriov/agent/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/mech_sriov/agent
copying neutron/plugins/ml2/plugin.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2
copying neutron/plugins/ml2/managers.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2
copying neutron/plugins/ml2/config.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2
copying neutron/plugins/ml2/driver_context.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2
copying neutron/plugins/ml2/db.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2
copying neutron/plugins/ml2/models.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2
copying neutron/plugins/ml2/rpc.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2
copying neutron/plugins/ml2/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2
copying neutron/plugins/ml2/driver_api.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2
creating build/lib.linux-i686-2.7/neutron/core_extensions
copying neutron/core_extensions/qos.py -> build/lib.linux-i686-2.7/neutron/core_extensions
copying neutron/core_extensions/__init__.py -> build/lib.linux-i686-2.7/neutron/core_extensions
copying neutron/core_extensions/base.py -> build/lib.linux-i686-2.7/neutron/core_extensions
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/linuxbridge
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/linuxbridge/mech_driver
copying neutron/tests/unit/plugins/ml2/drivers/linuxbridge/mech_driver/test_mech_linuxbridge.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/linuxbridge/mech_driver
copying neutron/tests/unit/plugins/ml2/drivers/linuxbridge/mech_driver/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/linuxbridge/mech_driver
creating build/lib.linux-i686-2.7/neutron/objects
copying neutron/objects/common_types.py -> build/lib.linux-i686-2.7/neutron/objects
copying neutron/objects/rbac_db.py -> build/lib.linux-i686-2.7/neutron/objects
copying neutron/objects/__init__.py -> build/lib.linux-i686-2.7/neutron/objects
copying neutron/objects/base.py -> build/lib.linux-i686-2.7/neutron/objects
creating build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/callbacks
copying neutron/tests/unit/api/rpc/callbacks/test_resources.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/callbacks
copying neutron/tests/unit/api/rpc/callbacks/test_resource_manager.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/callbacks
copying neutron/tests/unit/api/rpc/callbacks/test_version_manager.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/callbacks
copying neutron/tests/unit/api/rpc/callbacks/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/callbacks
copying neutron/plugins/ml2/drivers/type_vxlan.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers
copying neutron/plugins/ml2/drivers/type_geneve.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers
copying neutron/plugins/ml2/drivers/helpers.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers
copying neutron/plugins/ml2/drivers/mech_agent.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers
copying neutron/plugins/ml2/drivers/type_gre.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers
copying neutron/plugins/ml2/drivers/type_local.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers
copying neutron/plugins/ml2/drivers/type_tunnel.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers
copying neutron/plugins/ml2/drivers/type_flat.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers
copying neutron/plugins/ml2/drivers/type_vlan.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers
copying neutron/plugins/ml2/drivers/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers
copying neutron/tests/unit/agent/test_rpc.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent
copying neutron/tests/unit/agent/test_securitygroups_rpc.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent
copying neutron/tests/unit/agent/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent
creating build/lib.linux-i686-2.7/neutron/tests/unit/cmd
copying neutron/tests/unit/cmd/test_sanity_check.py -> build/lib.linux-i686-2.7/neutron/tests/unit/cmd
copying neutron/tests/unit/cmd/test_ovs_cleanup.py -> build/lib.linux-i686-2.7/neutron/tests/unit/cmd
copying neutron/tests/unit/cmd/test_netns_cleanup.py -> build/lib.linux-i686-2.7/neutron/tests/unit/cmd
copying neutron/tests/unit/cmd/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/cmd
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/mech_sriov/agent/common
copying neutron/tests/unit/plugins/ml2/drivers/mech_sriov/agent/common/test_config.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/mech_sriov/agent/common
copying neutron/tests/unit/plugins/ml2/drivers/mech_sriov/agent/common/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/mech_sriov/agent/common
creating build/lib.linux-i686-2.7/neutron/api/views
copying neutron/api/views/versions.py -> build/lib.linux-i686-2.7/neutron/api/views
copying neutron/api/views/__init__.py -> build/lib.linux-i686-2.7/neutron/api/views
creating build/lib.linux-i686-2.7/neutron/agent/metadata
copying neutron/agent/metadata/namespace_proxy.py -> build/lib.linux-i686-2.7/neutron/agent/metadata
copying neutron/agent/metadata/config.py -> build/lib.linux-i686-2.7/neutron/agent/metadata
copying neutron/agent/metadata/agent.py -> build/lib.linux-i686-2.7/neutron/agent/metadata
copying neutron/agent/metadata/driver.py -> build/lib.linux-i686-2.7/neutron/agent/metadata
copying neutron/agent/metadata/__init__.py -> build/lib.linux-i686-2.7/neutron/agent/metadata
creating build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux
copying neutron/tests/functional/agent/linux/test_keepalived.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux
copying neutron/tests/functional/agent/linux/test_process_monitor.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux
copying neutron/tests/functional/agent/linux/test_linuxbridge_arp_protect.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux
copying neutron/tests/functional/agent/linux/test_tc_lib.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux
copying neutron/tests/functional/agent/linux/test_async_process.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux
copying neutron/tests/functional/agent/linux/helpers.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux
copying neutron/tests/functional/agent/linux/test_ipset.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux
copying neutron/tests/functional/agent/linux/simple_daemon.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux
copying neutron/tests/functional/agent/linux/test_iptables.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux
copying neutron/tests/functional/agent/linux/test_ip_lib.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux
copying neutron/tests/functional/agent/linux/test_dhcp.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux
copying neutron/tests/functional/agent/linux/test_utils.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux
copying neutron/tests/functional/agent/linux/test_ip_monitor.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux
copying neutron/tests/functional/agent/linux/test_bridge_lib.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux
copying neutron/tests/functional/agent/linux/test_ovsdb_monitor.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux
copying neutron/tests/functional/agent/linux/test_interface.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux
copying neutron/tests/functional/agent/linux/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux
copying neutron/tests/functional/agent/linux/base.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux
creating build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/callbacks/consumer
copying neutron/tests/unit/api/rpc/callbacks/consumer/test_registry.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/callbacks/consumer
copying neutron/tests/unit/api/rpc/callbacks/consumer/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/callbacks/consumer
creating build/lib.linux-i686-2.7/neutron/tests/unit/agent/ovsdb
creating build/lib.linux-i686-2.7/neutron/tests/unit/agent/ovsdb/native
copying neutron/tests/unit/agent/ovsdb/native/test_helpers.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/ovsdb/native
copying neutron/tests/unit/agent/ovsdb/native/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/ovsdb/native
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/native
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/native/test_br_int.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/native
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/native/ovs_bridge_test_base.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/native
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/native/test_ovs_bridge.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/native
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/native/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/native
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/native/test_br_phys.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/native
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/native/test_br_tun.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/native
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/agent
copying neutron/plugins/ml2/drivers/agent/_agent_manager_base.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/agent
copying neutron/plugins/ml2/drivers/agent/config.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/agent
copying neutron/plugins/ml2/drivers/agent/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/agent
copying neutron/plugins/ml2/drivers/agent/_common_agent.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/agent
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/macvtap
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/macvtap/agent
copying neutron/tests/unit/plugins/ml2/drivers/macvtap/agent/test_macvtap_neutron_agent.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/macvtap/agent
copying neutron/tests/unit/plugins/ml2/drivers/macvtap/agent/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/macvtap/agent
copying neutron/services/bgp/bgp_plugin.py -> build/lib.linux-i686-2.7/neutron/services/bgp
copying neutron/services/bgp/__init__.py -> build/lib.linux-i686-2.7/neutron/services/bgp
creating build/lib.linux-i686-2.7/neutron/api/rpc/callbacks
creating build/lib.linux-i686-2.7/neutron/api/rpc/callbacks/consumer
copying neutron/api/rpc/callbacks/consumer/registry.py -> build/lib.linux-i686-2.7/neutron/api/rpc/callbacks/consumer
copying neutron/api/rpc/callbacks/consumer/__init__.py -> build/lib.linux-i686-2.7/neutron/api/rpc/callbacks/consumer
creating build/lib.linux-i686-2.7/neutron/tests/unit/agent/dhcp
copying neutron/tests/unit/agent/dhcp/test_agent.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/dhcp
copying neutron/tests/unit/agent/dhcp/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/dhcp
copying neutron/tests/functional/agent/test_ovs_lib.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent
copying neutron/tests/functional/agent/test_ovs_flows.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent
copying neutron/tests/functional/agent/test_l2_lb_agent.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent
copying neutron/tests/functional/agent/test_l2_ovs_agent.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent
copying neutron/tests/functional/agent/test_firewall.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent
copying neutron/tests/functional/agent/test_dhcp_agent.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent
copying neutron/tests/functional/agent/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl
copying neutron/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl/br_int.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl
copying neutron/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl/ofswitch.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl
copying neutron/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl/main.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl
copying neutron/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl/br_tun.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl
copying neutron/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl/br_phys.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl
copying neutron/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl/br_dvr_process.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl
copying neutron/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl/ovs_bridge.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl
copying neutron/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl
copying neutron/services/metering/metering_plugin.py -> build/lib.linux-i686-2.7/neutron/services/metering
copying neutron/services/metering/__init__.py -> build/lib.linux-i686-2.7/neutron/services/metering
creating build/lib.linux-i686-2.7/neutron/cmd/sanity
copying neutron/cmd/sanity/checks.py -> build/lib.linux-i686-2.7/neutron/cmd/sanity
copying neutron/cmd/sanity/__init__.py -> build/lib.linux-i686-2.7/neutron/cmd/sanity
creating build/lib.linux-i686-2.7/neutron/tests/retargetable
copying neutron/tests/retargetable/test_example.py -> build/lib.linux-i686-2.7/neutron/tests/retargetable
copying neutron/tests/retargetable/client_fixtures.py -> build/lib.linux-i686-2.7/neutron/tests/retargetable
copying neutron/tests/retargetable/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/retargetable
copying neutron/tests/retargetable/base.py -> build/lib.linux-i686-2.7/neutron/tests/retargetable
copying neutron/tests/retargetable/rest_fixture.py -> build/lib.linux-i686-2.7/neutron/tests/retargetable
creating build/lib.linux-i686-2.7/neutron/tests/unit/db/quota
copying neutron/tests/unit/db/quota/test_api.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db/quota
copying neutron/tests/unit/db/quota/test_driver.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db/quota
copying neutron/tests/unit/db/quota/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db/quota
copying neutron/tests/unit/plugins/ml2/drivers/mech_sriov/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/mech_sriov
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/linuxbridge/mech_driver
copying neutron/plugins/ml2/drivers/linuxbridge/mech_driver/mech_linuxbridge.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/linuxbridge/mech_driver
copying neutron/plugins/ml2/drivers/linuxbridge/mech_driver/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/linuxbridge/mech_driver
creating build/lib.linux-i686-2.7/neutron/services/externaldns
copying neutron/services/externaldns/driver.py -> build/lib.linux-i686-2.7/neutron/services/externaldns
copying neutron/services/externaldns/__init__.py -> build/lib.linux-i686-2.7/neutron/services/externaldns
copying neutron/tests/unit/test_wsgi.py -> build/lib.linux-i686-2.7/neutron/tests/unit
copying neutron/tests/unit/_test_extension_portbindings.py -> build/lib.linux-i686-2.7/neutron/tests/unit
copying neutron/tests/unit/dummy_plugin.py -> build/lib.linux-i686-2.7/neutron/tests/unit
copying neutron/tests/unit/extension_stubs.py -> build/lib.linux-i686-2.7/neutron/tests/unit
copying neutron/tests/unit/test_context.py -> build/lib.linux-i686-2.7/neutron/tests/unit
copying neutron/tests/unit/test_policy.py -> build/lib.linux-i686-2.7/neutron/tests/unit
copying neutron/tests/unit/test_manager.py -> build/lib.linux-i686-2.7/neutron/tests/unit
copying neutron/tests/unit/test_auth.py -> build/lib.linux-i686-2.7/neutron/tests/unit
copying neutron/tests/unit/test_service.py -> build/lib.linux-i686-2.7/neutron/tests/unit
copying neutron/tests/unit/testlib_api.py -> build/lib.linux-i686-2.7/neutron/tests/unit
copying neutron/tests/unit/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit
creating build/lib.linux-i686-2.7/neutron/agent/linux/openvswitch_firewall
copying neutron/agent/linux/openvswitch_firewall/rules.py -> build/lib.linux-i686-2.7/neutron/agent/linux/openvswitch_firewall
copying neutron/agent/linux/openvswitch_firewall/firewall.py -> build/lib.linux-i686-2.7/neutron/agent/linux/openvswitch_firewall
copying neutron/agent/linux/openvswitch_firewall/constants.py -> build/lib.linux-i686-2.7/neutron/agent/linux/openvswitch_firewall
copying neutron/agent/linux/openvswitch_firewall/__init__.py -> build/lib.linux-i686-2.7/neutron/agent/linux/openvswitch_firewall
creating build/lib.linux-i686-2.7/neutron/tests/unit/ipam
copying neutron/tests/unit/ipam/test_requests.py -> build/lib.linux-i686-2.7/neutron/tests/unit/ipam
copying neutron/tests/unit/ipam/fake_driver.py -> build/lib.linux-i686-2.7/neutron/tests/unit/ipam
copying neutron/tests/unit/ipam/test_utils.py -> build/lib.linux-i686-2.7/neutron/tests/unit/ipam
copying neutron/tests/unit/ipam/test_subnet_alloc.py -> build/lib.linux-i686-2.7/neutron/tests/unit/ipam
copying neutron/tests/unit/ipam/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/ipam
copying neutron/tests/unit/agent/ovsdb/test_impl_idl.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/ovsdb
copying neutron/tests/unit/agent/ovsdb/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/ovsdb
creating build/lib.linux-i686-2.7/neutron/server
copying neutron/server/wsgi_eventlet.py -> build/lib.linux-i686-2.7/neutron/server
copying neutron/server/rpc_eventlet.py -> build/lib.linux-i686-2.7/neutron/server
copying neutron/server/wsgi_pecan.py -> build/lib.linux-i686-2.7/neutron/server
copying neutron/server/__init__.py -> build/lib.linux-i686-2.7/neutron/server
copying neutron/ipam/exceptions.py -> build/lib.linux-i686-2.7/neutron/ipam
copying neutron/ipam/requests.py -> build/lib.linux-i686-2.7/neutron/ipam
copying neutron/ipam/utils.py -> build/lib.linux-i686-2.7/neutron/ipam
copying neutron/ipam/driver.py -> build/lib.linux-i686-2.7/neutron/ipam
copying neutron/ipam/subnet_alloc.py -> build/lib.linux-i686-2.7/neutron/ipam
copying neutron/ipam/__init__.py -> build/lib.linux-i686-2.7/neutron/ipam
creating build/lib.linux-i686-2.7/neutron/tests/unit/callbacks
copying neutron/tests/unit/callbacks/test_manager.py -> build/lib.linux-i686-2.7/neutron/tests/unit/callbacks
copying neutron/tests/unit/callbacks/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/callbacks
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/extension_drivers
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/extension_drivers/test_qos_driver.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/extension_drivers
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/extension_drivers/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/extension_drivers
copying neutron/plugins/ml2/drivers/openvswitch/agent/ovs_dvr_neutron_agent.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent
copying neutron/plugins/ml2/drivers/openvswitch/agent/ovs_agent_extension_api.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent
copying neutron/plugins/ml2/drivers/openvswitch/agent/main.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent
copying neutron/plugins/ml2/drivers/openvswitch/agent/ovs_neutron_agent.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent
copying neutron/plugins/ml2/drivers/openvswitch/agent/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent
copying neutron/services/metering/drivers/abstract_driver.py -> build/lib.linux-i686-2.7/neutron/services/metering/drivers
copying neutron/services/metering/drivers/__init__.py -> build/lib.linux-i686-2.7/neutron/services/metering/drivers
creating build/lib.linux-i686-2.7/neutron/tests/unit/objects/qos
copying neutron/tests/unit/objects/qos/test_policy.py -> build/lib.linux-i686-2.7/neutron/tests/unit/objects/qos
copying neutron/tests/unit/objects/qos/test_rule.py -> build/lib.linux-i686-2.7/neutron/tests/unit/objects/qos
copying neutron/tests/unit/objects/qos/test_rule_type.py -> build/lib.linux-i686-2.7/neutron/tests/unit/objects/qos
copying neutron/tests/unit/objects/qos/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/objects/qos
creating build/lib.linux-i686-2.7/neutron/tests/unit/agent/l2
creating build/lib.linux-i686-2.7/neutron/tests/unit/agent/l2/extensions
copying neutron/tests/unit/agent/l2/extensions/test_manager.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/l2/extensions
copying neutron/tests/unit/agent/l2/extensions/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/l2/extensions
copying neutron/tests/unit/agent/l2/extensions/test_qos.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/l2/extensions
creating build/lib.linux-i686-2.7/neutron/cmd/eventlet/services
copying neutron/cmd/eventlet/services/fabric.py -> build/lib.linux-i686-2.7/neutron/cmd/eventlet/services
copying neutron/cmd/eventlet/services/metering_agent.py -> build/lib.linux-i686-2.7/neutron/cmd/eventlet/services
copying neutron/cmd/eventlet/services/__init__.py -> build/lib.linux-i686-2.7/neutron/cmd/eventlet/services
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/mech_driver
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/mech_driver/test_mech_openvswitch.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/mech_driver
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/mech_driver/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/mech_driver
creating build/lib.linux-i686-2.7/neutron/tests/unit/quota
copying neutron/tests/unit/quota/test_resource.py -> build/lib.linux-i686-2.7/neutron/tests/unit/quota
copying neutron/tests/unit/quota/test_resource_registry.py -> build/lib.linux-i686-2.7/neutron/tests/unit/quota
copying neutron/tests/unit/quota/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/quota
creating build/lib.linux-i686-2.7/neutron/tests/functional/api
copying neutron/tests/functional/api/test_policies.py -> build/lib.linux-i686-2.7/neutron/tests/functional/api
copying neutron/tests/functional/api/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/api
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/mech_sriov/mech_driver
copying neutron/tests/unit/plugins/ml2/drivers/mech_sriov/mech_driver/test_mech_sriov_nic_switch.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/mech_sriov/mech_driver
copying neutron/tests/unit/plugins/ml2/drivers/mech_sriov/mech_driver/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/mech_sriov/mech_driver
creating build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/handlers
copying neutron/tests/unit/api/rpc/handlers/test_resources_rpc.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/handlers
copying neutron/tests/unit/api/rpc/handlers/test_dhcp_rpc.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/handlers
copying neutron/tests/unit/api/rpc/handlers/test_l3_rpc.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/handlers
copying neutron/tests/unit/api/rpc/handlers/test_dvr_rpc.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/handlers
copying neutron/tests/unit/api/rpc/handlers/test_securitygroups_rpc.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/handlers
copying neutron/tests/unit/api/rpc/handlers/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/handlers
copying neutron/tests/unit/api/rpc/handlers/test_bgp_speaker_rpc.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/handlers
creating build/lib.linux-i686-2.7/neutron/tests/functional/scheduler
copying neutron/tests/functional/scheduler/test_l3_agent_scheduler.py -> build/lib.linux-i686-2.7/neutron/tests/functional/scheduler
copying neutron/tests/functional/scheduler/test_dhcp_agent_scheduler.py -> build/lib.linux-i686-2.7/neutron/tests/functional/scheduler
copying neutron/tests/functional/scheduler/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/scheduler
copying neutron/tests/unit/plugins/ml2/drivers/macvtap/test_macvtap_common.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/macvtap
copying neutron/tests/unit/plugins/ml2/drivers/macvtap/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/macvtap
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/mech_sriov/agent/common
copying neutron/plugins/ml2/drivers/mech_sriov/agent/common/config.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/mech_sriov/agent/common
copying neutron/plugins/ml2/drivers/mech_sriov/agent/common/exceptions.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/mech_sriov/agent/common
copying neutron/plugins/ml2/drivers/mech_sriov/agent/common/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/mech_sriov/agent/common
creating build/lib.linux-i686-2.7/neutron/tests/unit/notifiers
copying neutron/tests/unit/notifiers/test_nova.py -> build/lib.linux-i686-2.7/neutron/tests/unit/notifiers
copying neutron/tests/unit/notifiers/test_batch_notifier.py -> build/lib.linux-i686-2.7/neutron/tests/unit/notifiers
copying neutron/tests/unit/notifiers/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/notifiers
creating build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_availability_zone.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_router_availability_zone.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_agent.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_address_scope.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_servicetype.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_timestamp_core.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/foxinsocks.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/extendedattribute.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_portsecurity.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/extensionattribute.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_bgp_dragentscheduler.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_quotasv2.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_network_ip_availability.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_l3_ext_gw_mode.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_extraroute.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_flavors.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_default_subnetpools.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_vlantransparent.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_securitygroup.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/v2attributes.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_netmtu.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_providernet.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_l3.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_extra_dhcp_opt.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_dns.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_tag.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/test_external_net.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
copying neutron/tests/unit/extensions/base.py -> build/lib.linux-i686-2.7/neutron/tests/unit/extensions
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/l2pop/rpc_manager
copying neutron/tests/unit/plugins/ml2/drivers/l2pop/rpc_manager/l2population_rpc_base.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/l2pop/rpc_manager
copying neutron/tests/unit/plugins/ml2/drivers/l2pop/rpc_manager/test_l2population_rpc.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/l2pop/rpc_manager
copying neutron/tests/unit/plugins/ml2/drivers/l2pop/rpc_manager/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/l2pop/rpc_manager
copying neutron/tests/functional/plugins/ml2/test_plugin.py -> build/lib.linux-i686-2.7/neutron/tests/functional/plugins/ml2
copying neutron/tests/functional/plugins/ml2/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/plugins/ml2
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/macvtap
copying neutron/plugins/ml2/drivers/macvtap/macvtap_common.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/macvtap
copying neutron/plugins/ml2/drivers/macvtap/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/macvtap
creating build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/l3agentscheduler.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/availability_zone.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/bgp_dragentscheduler.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/portbindings.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/address_scope.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/quotasv2.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/bgp.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/dhcpagentscheduler.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/auto_allocated_topology.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/extraroute.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/external_net.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/dns.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/qos.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/netmtu.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/router_availability_zone.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/servicetype.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/standardattrdescription.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/securitygroup.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/tag.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/multiprovidernet.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/agent.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/l3_ext_gw_mode.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/timestamp_core.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/network_ip_availability.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/metering.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/default_subnetpools.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/flavors.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/network_availability_zone.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/allowedaddresspairs.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/l3_ext_ha_mode.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/providernet.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/dvr.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/routerservicetype.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/l3.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/rbac.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/vlantransparent.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/extra_dhcp_opt.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/subnetallocation.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/portsecurity.py -> build/lib.linux-i686-2.7/neutron/extensions
copying neutron/extensions/__init__.py -> build/lib.linux-i686-2.7/neutron/extensions
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/macvtap/mech_driver
copying neutron/plugins/ml2/drivers/macvtap/mech_driver/mech_macvtap.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/macvtap/mech_driver
copying neutron/plugins/ml2/drivers/macvtap/mech_driver/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/macvtap/mech_driver
creating build/lib.linux-i686-2.7/neutron/services/bgp/scheduler
copying neutron/services/bgp/scheduler/bgp_dragent_scheduler.py -> build/lib.linux-i686-2.7/neutron/services/bgp/scheduler
copying neutron/services/bgp/scheduler/__init__.py -> build/lib.linux-i686-2.7/neutron/services/bgp/scheduler
creating build/lib.linux-i686-2.7/neutron/callbacks
copying neutron/callbacks/registry.py -> build/lib.linux-i686-2.7/neutron/callbacks
copying neutron/callbacks/resources.py -> build/lib.linux-i686-2.7/neutron/callbacks
copying neutron/callbacks/exceptions.py -> build/lib.linux-i686-2.7/neutron/callbacks
copying neutron/callbacks/manager.py -> build/lib.linux-i686-2.7/neutron/callbacks
copying neutron/callbacks/events.py -> build/lib.linux-i686-2.7/neutron/callbacks
copying neutron/callbacks/__init__.py -> build/lib.linux-i686-2.7/neutron/callbacks
copying neutron/db/migration/autogen.py -> build/lib.linux-i686-2.7/neutron/db/migration
copying neutron/db/migration/connection.py -> build/lib.linux-i686-2.7/neutron/db/migration
copying neutron/db/migration/cli.py -> build/lib.linux-i686-2.7/neutron/db/migration
copying neutron/db/migration/__init__.py -> build/lib.linux-i686-2.7/neutron/db/migration
creating build/lib.linux-i686-2.7/neutron/tests/unit/agent/windows
copying neutron/tests/unit/agent/windows/test_ip_lib.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/windows
copying neutron/tests/unit/agent/windows/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/windows
copying neutron/tests/unit/tests/test_tools.py -> build/lib.linux-i686-2.7/neutron/tests/unit/tests
copying neutron/tests/unit/tests/test_post_mortem_debug.py -> build/lib.linux-i686-2.7/neutron/tests/unit/tests
copying neutron/tests/unit/tests/test_base.py -> build/lib.linux-i686-2.7/neutron/tests/unit/tests
copying neutron/tests/unit/tests/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/tests
creating build/lib.linux-i686-2.7/neutron/tests/unit/ipam/drivers
copying neutron/tests/unit/ipam/drivers/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/ipam/drivers
creating build/lib.linux-i686-2.7/neutron/services/l3_router
copying neutron/services/l3_router/l3_router_plugin.py -> build/lib.linux-i686-2.7/neutron/services/l3_router
copying neutron/services/l3_router/__init__.py -> build/lib.linux-i686-2.7/neutron/services/l3_router
creating build/lib.linux-i686-2.7/neutron/tests/functional/agent/l3
copying neutron/tests/functional/agent/l3/test_namespace_manager.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/l3
copying neutron/tests/functional/agent/l3/test_keepalived_state_change.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/l3
copying neutron/tests/functional/agent/l3/test_dvr_router.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/l3
copying neutron/tests/functional/agent/l3/framework.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/l3
copying neutron/tests/functional/agent/l3/test_ha_router.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/l3
copying neutron/tests/functional/agent/l3/test_legacy_router.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/l3
copying neutron/tests/functional/agent/l3/test_metadata_proxy.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/l3
copying neutron/tests/functional/agent/l3/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/l3
creating build/lib.linux-i686-2.7/neutron/objects/db
copying neutron/objects/db/api.py -> build/lib.linux-i686-2.7/neutron/objects/db
copying neutron/objects/db/__init__.py -> build/lib.linux-i686-2.7/neutron/objects/db
creating build/lib.linux-i686-2.7/neutron/tests/fullstack
copying neutron/tests/fullstack/test_connectivity.py -> build/lib.linux-i686-2.7/neutron/tests/fullstack
copying neutron/tests/fullstack/test_l3_agent.py -> build/lib.linux-i686-2.7/neutron/tests/fullstack
copying neutron/tests/fullstack/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/fullstack
copying neutron/tests/fullstack/base.py -> build/lib.linux-i686-2.7/neutron/tests/fullstack
copying neutron/tests/fullstack/test_qos.py -> build/lib.linux-i686-2.7/neutron/tests/fullstack
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/mech_driver
copying neutron/plugins/ml2/drivers/openvswitch/mech_driver/mech_openvswitch.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/mech_driver
copying neutron/plugins/ml2/drivers/openvswitch/mech_driver/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/mech_driver
creating build/lib.linux-i686-2.7/neutron/tests/functional/services/bgp
copying neutron/tests/functional/services/bgp/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/services/bgp
creating build/lib.linux-i686-2.7/neutron/notifiers
copying neutron/notifiers/nova.py -> build/lib.linux-i686-2.7/neutron/notifiers
copying neutron/notifiers/batch_notifier.py -> build/lib.linux-i686-2.7/neutron/notifiers
copying neutron/notifiers/__init__.py -> build/lib.linux-i686-2.7/neutron/notifiers
creating build/lib.linux-i686-2.7/neutron/tests/fullstack/resources
copying neutron/tests/fullstack/resources/config.py -> build/lib.linux-i686-2.7/neutron/tests/fullstack/resources
copying neutron/tests/fullstack/resources/machine.py -> build/lib.linux-i686-2.7/neutron/tests/fullstack/resources
copying neutron/tests/fullstack/resources/client.py -> build/lib.linux-i686-2.7/neutron/tests/fullstack/resources
copying neutron/tests/fullstack/resources/process.py -> build/lib.linux-i686-2.7/neutron/tests/fullstack/resources
copying neutron/tests/fullstack/resources/environment.py -> build/lib.linux-i686-2.7/neutron/tests/fullstack/resources
copying neutron/tests/fullstack/resources/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/fullstack/resources
creating build/lib.linux-i686-2.7/neutron/tests/tempest/services
copying neutron/tests/tempest/services/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/tempest/services
copying neutron/plugins/ml2/drivers/openvswitch/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch
creating build/lib.linux-i686-2.7/neutron/tests/functional/agent/ovsdb
copying neutron/tests/functional/agent/ovsdb/test_impl_idl.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/ovsdb
copying neutron/tests/functional/agent/ovsdb/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/ovsdb
copying neutron/tests/unit/api/test_extensions.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api
copying neutron/tests/unit/api/test_api_common.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api
copying neutron/tests/unit/api/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api
creating build/lib.linux-i686-2.7/neutron/tests/unit/core_extensions
copying neutron/tests/unit/core_extensions/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/core_extensions
copying neutron/tests/unit/core_extensions/test_qos.py -> build/lib.linux-i686-2.7/neutron/tests/unit/core_extensions
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/mech_sriov/mech_driver
copying neutron/plugins/ml2/drivers/mech_sriov/mech_driver/exceptions.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/mech_sriov/mech_driver
copying neutron/plugins/ml2/drivers/mech_sriov/mech_driver/mech_driver.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/mech_sriov/mech_driver
copying neutron/plugins/ml2/drivers/mech_sriov/mech_driver/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/mech_sriov/mech_driver
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/linuxbridge/agent
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/linuxbridge/agent/extension_drivers
copying neutron/tests/unit/plugins/ml2/drivers/linuxbridge/agent/extension_drivers/test_qos_driver.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/linuxbridge/agent/extension_drivers
copying neutron/tests/unit/plugins/ml2/drivers/linuxbridge/agent/extension_drivers/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/linuxbridge/agent/extension_drivers
creating build/lib.linux-i686-2.7/neutron/tests/unit/scheduler
copying neutron/tests/unit/scheduler/test_l3_agent_scheduler.py -> build/lib.linux-i686-2.7/neutron/tests/unit/scheduler
copying neutron/tests/unit/scheduler/test_dhcp_agent_scheduler.py -> build/lib.linux-i686-2.7/neutron/tests/unit/scheduler
copying neutron/tests/unit/scheduler/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/scheduler
copying neutron/cmd/eventlet/usage_audit.py -> build/lib.linux-i686-2.7/neutron/cmd/eventlet
copying neutron/cmd/eventlet/__init__.py -> build/lib.linux-i686-2.7/neutron/cmd/eventlet
creating build/lib.linux-i686-2.7/neutron/tests/unit/tests/common
copying neutron/tests/unit/tests/common/test_net_helpers.py -> build/lib.linux-i686-2.7/neutron/tests/unit/tests/common
copying neutron/tests/unit/tests/common/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/tests/common
creating build/lib.linux-i686-2.7/neutron/quota
copying neutron/quota/resource.py -> build/lib.linux-i686-2.7/neutron/quota
copying neutron/quota/resource_registry.py -> build/lib.linux-i686-2.7/neutron/quota
copying neutron/quota/__init__.py -> build/lib.linux-i686-2.7/neutron/quota
creating build/lib.linux-i686-2.7/neutron/plugins/hyperv/agent
copying neutron/plugins/hyperv/agent/security_groups_driver.py -> build/lib.linux-i686-2.7/neutron/plugins/hyperv/agent
copying neutron/plugins/hyperv/agent/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/hyperv/agent
creating build/lib.linux-i686-2.7/neutron/tests/unit/services/bgp
copying neutron/tests/unit/services/bgp/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/bgp
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl/test_br_int.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl/ovs_bridge_test_base.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl/test_br_phys.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl/test_br_tun.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/ovs_ofctl
creating build/lib.linux-i686-2.7/neutron/openstack
copying neutron/openstack/__init__.py -> build/lib.linux-i686-2.7/neutron/openstack
creating build/lib.linux-i686-2.7/neutron/agent/l2/extensions
copying neutron/agent/l2/extensions/qos.py -> build/lib.linux-i686-2.7/neutron/agent/l2/extensions
copying neutron/agent/l2/extensions/manager.py -> build/lib.linux-i686-2.7/neutron/agent/l2/extensions
copying neutron/agent/l2/extensions/__init__.py -> build/lib.linux-i686-2.7/neutron/agent/l2/extensions
creating build/lib.linux-i686-2.7/neutron/tests/functional/pecan_wsgi
copying neutron/tests/functional/pecan_wsgi/config.py -> build/lib.linux-i686-2.7/neutron/tests/functional/pecan_wsgi
copying neutron/tests/functional/pecan_wsgi/test_controllers.py -> build/lib.linux-i686-2.7/neutron/tests/functional/pecan_wsgi
copying neutron/tests/functional/pecan_wsgi/utils.py -> build/lib.linux-i686-2.7/neutron/tests/functional/pecan_wsgi
copying neutron/tests/functional/pecan_wsgi/test_hooks.py -> build/lib.linux-i686-2.7/neutron/tests/functional/pecan_wsgi
copying neutron/tests/functional/pecan_wsgi/test_functional.py -> build/lib.linux-i686-2.7/neutron/tests/functional/pecan_wsgi
copying neutron/tests/functional/pecan_wsgi/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/pecan_wsgi
copying neutron/tests/unit/plugins/ml2/drivers/linuxbridge/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/linuxbridge
copying neutron/tests/unit/plugins/ml2/drivers/test_type_local.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers
copying neutron/tests/unit/plugins/ml2/drivers/test_type_geneve.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers
copying neutron/tests/unit/plugins/ml2/drivers/test_type_gre.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers
copying neutron/tests/unit/plugins/ml2/drivers/mechanism_test.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers
copying neutron/tests/unit/plugins/ml2/drivers/ext_test.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers
copying neutron/tests/unit/plugins/ml2/drivers/test_type_vxlan.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers
copying neutron/tests/unit/plugins/ml2/drivers/mech_fake_agent.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers
copying neutron/tests/unit/plugins/ml2/drivers/test_type_vlan.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers
copying neutron/tests/unit/plugins/ml2/drivers/base_type_tunnel.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers
copying neutron/tests/unit/plugins/ml2/drivers/mechanism_logger.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers
copying neutron/tests/unit/plugins/ml2/drivers/test_helpers.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers
copying neutron/tests/unit/plugins/ml2/drivers/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers
copying neutron/tests/unit/plugins/ml2/drivers/test_type_flat.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers
copying neutron/services/provider_configuration.py -> build/lib.linux-i686-2.7/neutron/services
copying neutron/services/service_base.py -> build/lib.linux-i686-2.7/neutron/services
copying neutron/services/__init__.py -> build/lib.linux-i686-2.7/neutron/services
creating build/lib.linux-i686-2.7/neutron/tests/unit/services/bgp/scheduler
copying neutron/tests/unit/services/bgp/scheduler/test_bgp_dragent_scheduler.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/bgp/scheduler
copying neutron/tests/unit/services/bgp/scheduler/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/bgp/scheduler
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/common
copying neutron/plugins/ml2/drivers/openvswitch/agent/common/config.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/common
copying neutron/plugins/ml2/drivers/openvswitch/agent/common/constants.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/common
copying neutron/plugins/ml2/drivers/openvswitch/agent/common/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/common
creating build/lib.linux-i686-2.7/neutron/services/tag
copying neutron/services/tag/tag_plugin.py -> build/lib.linux-i686-2.7/neutron/services/tag
copying neutron/services/tag/__init__.py -> build/lib.linux-i686-2.7/neutron/services/tag
copying neutron/tests/unit/services/test_provider_configuration.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services
copying neutron/tests/unit/services/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services
creating build/lib.linux-i686-2.7/neutron/tests/unit/services/bgp/driver
creating build/lib.linux-i686-2.7/neutron/tests/unit/services/bgp/driver/ryu
copying neutron/tests/unit/services/bgp/driver/ryu/test_driver.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/bgp/driver/ryu
copying neutron/tests/unit/services/bgp/driver/ryu/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/bgp/driver/ryu
copying neutron/plugins/ml2/drivers/openvswitch/agent/openflow/br_cookie.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow
copying neutron/plugins/ml2/drivers/openvswitch/agent/openflow/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow
creating build/lib.linux-i686-2.7/neutron/api/v2
copying neutron/api/v2/attributes.py -> build/lib.linux-i686-2.7/neutron/api/v2
copying neutron/api/v2/router.py -> build/lib.linux-i686-2.7/neutron/api/v2
copying neutron/api/v2/resource.py -> build/lib.linux-i686-2.7/neutron/api/v2
copying neutron/api/v2/resource_helper.py -> build/lib.linux-i686-2.7/neutron/api/v2
copying neutron/api/v2/__init__.py -> build/lib.linux-i686-2.7/neutron/api/v2
copying neutron/api/v2/base.py -> build/lib.linux-i686-2.7/neutron/api/v2
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/test_br_cookie.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/openflow
creating build/lib.linux-i686-2.7/neutron/tests/tempest/common
copying neutron/tests/tempest/common/tempest_fixtures.py -> build/lib.linux-i686-2.7/neutron/tests/tempest/common
copying neutron/tests/tempest/common/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/tempest/common
creating build/lib.linux-i686-2.7/neutron/services/network_ip_availability
copying neutron/services/network_ip_availability/plugin.py -> build/lib.linux-i686-2.7/neutron/services/network_ip_availability
copying neutron/services/network_ip_availability/__init__.py -> build/lib.linux-i686-2.7/neutron/services/network_ip_availability
creating build/lib.linux-i686-2.7/neutron/tests/unit/hacking
copying neutron/tests/unit/hacking/test_checks.py -> build/lib.linux-i686-2.7/neutron/tests/unit/hacking
copying neutron/tests/unit/hacking/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/hacking
creating build/lib.linux-i686-2.7/neutron/tests/functional/agent/windows
copying neutron/tests/functional/agent/windows/test_ip_lib.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/windows
copying neutron/tests/functional/agent/windows/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/windows
creating build/lib.linux-i686-2.7/neutron/tests/common
creating build/lib.linux-i686-2.7/neutron/tests/common/agents
copying neutron/tests/common/agents/ovs_agent.py -> build/lib.linux-i686-2.7/neutron/tests/common/agents
copying neutron/tests/common/agents/l2_extensions.py -> build/lib.linux-i686-2.7/neutron/tests/common/agents
copying neutron/tests/common/agents/l3_agent.py -> build/lib.linux-i686-2.7/neutron/tests/common/agents
copying neutron/tests/common/agents/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/common/agents
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/common
copying neutron/tests/unit/plugins/common/test_utils.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/common
copying neutron/tests/unit/plugins/common/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/common
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/test_ovs_neutron_agent.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/test_ovs_agent_extension_api.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/test_ovs_tunnel.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/ovs_test_base.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/fake_oflib.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch/agent
copying neutron/tests/unit/tests/example/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/tests/example
creating build/lib.linux-i686-2.7/neutron/tests/functional/cmd
copying neutron/tests/functional/cmd/test_linuxbridge_cleanup.py -> build/lib.linux-i686-2.7/neutron/tests/functional/cmd
copying neutron/tests/functional/cmd/test_netns_cleanup.py -> build/lib.linux-i686-2.7/neutron/tests/functional/cmd
copying neutron/tests/functional/cmd/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/cmd
creating build/lib.linux-i686-2.7/neutron/tests/unit/cmd/server
copying neutron/tests/unit/cmd/server/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/cmd/server
creating build/lib.linux-i686-2.7/neutron/tests/unit/api/v2
copying neutron/tests/unit/api/v2/test_resource.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/v2
copying neutron/tests/unit/api/v2/test_attributes.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/v2
copying neutron/tests/unit/api/v2/test_base.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/v2
copying neutron/tests/unit/api/v2/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/v2
creating build/lib.linux-i686-2.7/neutron/debug
copying neutron/debug/commands.py -> build/lib.linux-i686-2.7/neutron/debug
copying neutron/debug/debug_agent.py -> build/lib.linux-i686-2.7/neutron/debug
copying neutron/debug/shell.py -> build/lib.linux-i686-2.7/neutron/debug
copying neutron/debug/__init__.py -> build/lib.linux-i686-2.7/neutron/debug
creating build/lib.linux-i686-2.7/neutron/cmd/eventlet/server
copying neutron/cmd/eventlet/server/__init__.py -> build/lib.linux-i686-2.7/neutron/cmd/eventlet/server
creating build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/callbacks/producer
copying neutron/tests/unit/api/rpc/callbacks/producer/test_registry.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/callbacks/producer
copying neutron/tests/unit/api/rpc/callbacks/producer/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/callbacks/producer
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/macvtap/agent
copying neutron/plugins/ml2/drivers/macvtap/agent/config.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/macvtap/agent
copying neutron/plugins/ml2/drivers/macvtap/agent/macvtap_neutron_agent.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/macvtap/agent
copying neutron/plugins/ml2/drivers/macvtap/agent/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/macvtap/agent
creating build/lib.linux-i686-2.7/neutron/services/fabric/plugin
copying neutron/services/fabric/plugin/fabric.py -> build/lib.linux-i686-2.7/neutron/services/fabric/plugin
copying neutron/services/fabric/plugin/__init__.py -> build/lib.linux-i686-2.7/neutron/services/fabric/plugin
creating build/lib.linux-i686-2.7/neutron/tests/tempest/services/network
copying neutron/tests/tempest/services/network/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/tempest/services/network
creating build/lib.linux-i686-2.7/neutron/api/rpc/handlers
copying neutron/api/rpc/handlers/resources_rpc.py -> build/lib.linux-i686-2.7/neutron/api/rpc/handlers
copying neutron/api/rpc/handlers/metadata_rpc.py -> build/lib.linux-i686-2.7/neutron/api/rpc/handlers
copying neutron/api/rpc/handlers/securitygroups_rpc.py -> build/lib.linux-i686-2.7/neutron/api/rpc/handlers
copying neutron/api/rpc/handlers/dhcp_rpc.py -> build/lib.linux-i686-2.7/neutron/api/rpc/handlers
copying neutron/api/rpc/handlers/dvr_rpc.py -> build/lib.linux-i686-2.7/neutron/api/rpc/handlers
copying neutron/api/rpc/handlers/bgp_speaker_rpc.py -> build/lib.linux-i686-2.7/neutron/api/rpc/handlers
copying neutron/api/rpc/handlers/l3_rpc.py -> build/lib.linux-i686-2.7/neutron/api/rpc/handlers
copying neutron/api/rpc/handlers/__init__.py -> build/lib.linux-i686-2.7/neutron/api/rpc/handlers
creating build/lib.linux-i686-2.7/neutron/tests/unit/services/auto_allocate
copying neutron/tests/unit/services/auto_allocate/test_db.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/auto_allocate
copying neutron/tests/unit/services/auto_allocate/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/auto_allocate
creating build/lib.linux-i686-2.7/neutron/tests/functional/services/bgp/scheduler
copying neutron/tests/functional/services/bgp/scheduler/test_bgp_dragent_scheduler.py -> build/lib.linux-i686-2.7/neutron/tests/functional/services/bgp/scheduler
copying neutron/tests/functional/services/bgp/scheduler/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/services/bgp/scheduler
copying neutron/tests/unit/plugins/ml2/drivers/openvswitch/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/openvswitch
copying neutron/tests/unit/plugins/ml2/test_driver_context.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2
copying neutron/tests/unit/plugins/ml2/test_agent_scheduler.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2
copying neutron/tests/unit/plugins/ml2/test_extension_driver_api.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2
copying neutron/tests/unit/plugins/ml2/test_db.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2
copying neutron/tests/unit/plugins/ml2/test_rpc.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2
copying neutron/tests/unit/plugins/ml2/test_ext_portsecurity.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2
copying neutron/tests/unit/plugins/ml2/test_managers.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2
copying neutron/tests/unit/plugins/ml2/test_port_binding.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2
copying neutron/tests/unit/plugins/ml2/test_security_group.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2
copying neutron/tests/unit/plugins/ml2/test_plugin.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2
copying neutron/tests/unit/plugins/ml2/_test_mech_agent.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2
copying neutron/tests/unit/plugins/ml2/test_tracked_resources.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2
copying neutron/tests/unit/plugins/ml2/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2
copying neutron/tests/unit/plugins/ml2/base.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2
copying neutron/tests/unit/agent/l2/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/l2
creating build/lib.linux-i686-2.7/neutron/tests/unit/agent/l3
copying neutron/tests/unit/agent/l3/test_link_local_allocator.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/l3
copying neutron/tests/unit/agent/l3/test_namespace_manager.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/l3
copying neutron/tests/unit/agent/l3/test_agent.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/l3
copying neutron/tests/unit/agent/l3/test_item_allocator.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/l3
copying neutron/tests/unit/agent/l3/test_dvr_local_router.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/l3
copying neutron/tests/unit/agent/l3/test_router_info.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/l3
copying neutron/tests/unit/agent/l3/test_ha_router.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/l3
copying neutron/tests/unit/agent/l3/test_legacy_router.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/l3
copying neutron/tests/unit/agent/l3/test_router_processing_queue.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/l3
copying neutron/tests/unit/agent/l3/test_dvr_fip_ns.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/l3
copying neutron/tests/unit/agent/l3/test_fip_rule_priority_allocator.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/l3
copying neutron/tests/unit/agent/l3/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/l3
creating build/lib.linux-i686-2.7/neutron/services/bgp/driver
creating build/lib.linux-i686-2.7/neutron/services/bgp/driver/ryu
copying neutron/services/bgp/driver/ryu/driver.py -> build/lib.linux-i686-2.7/neutron/services/bgp/driver/ryu
copying neutron/services/bgp/driver/ryu/__init__.py -> build/lib.linux-i686-2.7/neutron/services/bgp/driver/ryu
creating build/lib.linux-i686-2.7/neutron/api/rpc/callbacks/producer
copying neutron/api/rpc/callbacks/producer/registry.py -> build/lib.linux-i686-2.7/neutron/api/rpc/callbacks/producer
copying neutron/api/rpc/callbacks/producer/__init__.py -> build/lib.linux-i686-2.7/neutron/api/rpc/callbacks/producer
copying neutron/tests/unit/services/metering/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/metering
copying neutron/tests/unit/services/metering/test_metering_plugin.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/metering
creating build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/agentnotifiers
copying neutron/tests/unit/api/rpc/agentnotifiers/test_bgp_dr_rpc_agent_api.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/agentnotifiers
copying neutron/tests/unit/api/rpc/agentnotifiers/test_l3_rpc_agent_api.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/agentnotifiers
copying neutron/tests/unit/api/rpc/agentnotifiers/test_dhcp_rpc_agent_api.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/agentnotifiers
copying neutron/tests/unit/api/rpc/agentnotifiers/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/api/rpc/agentnotifiers
creating build/lib.linux-i686-2.7/neutron/agent/windows
copying neutron/agent/windows/utils.py -> build/lib.linux-i686-2.7/neutron/agent/windows
copying neutron/agent/windows/polling.py -> build/lib.linux-i686-2.7/neutron/agent/windows
copying neutron/agent/windows/ip_lib.py -> build/lib.linux-i686-2.7/neutron/agent/windows
copying neutron/agent/windows/__init__.py -> build/lib.linux-i686-2.7/neutron/agent/windows
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow/native
copying neutron/plugins/ml2/drivers/openvswitch/agent/openflow/native/br_int.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow/native
copying neutron/plugins/ml2/drivers/openvswitch/agent/openflow/native/ofswitch.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow/native
copying neutron/plugins/ml2/drivers/openvswitch/agent/openflow/native/main.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow/native
copying neutron/plugins/ml2/drivers/openvswitch/agent/openflow/native/br_tun.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow/native
copying neutron/plugins/ml2/drivers/openvswitch/agent/openflow/native/ovs_ryuapp.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow/native
copying neutron/plugins/ml2/drivers/openvswitch/agent/openflow/native/br_phys.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow/native
copying neutron/plugins/ml2/drivers/openvswitch/agent/openflow/native/br_dvr_process.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow/native
copying neutron/plugins/ml2/drivers/openvswitch/agent/openflow/native/ovs_bridge.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow/native
copying neutron/plugins/ml2/drivers/openvswitch/agent/openflow/native/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/openflow/native
creating build/lib.linux-i686-2.7/neutron/pecan_wsgi/hooks
copying neutron/pecan_wsgi/hooks/notifier.py -> build/lib.linux-i686-2.7/neutron/pecan_wsgi/hooks
copying neutron/pecan_wsgi/hooks/ownership_validation.py -> build/lib.linux-i686-2.7/neutron/pecan_wsgi/hooks
copying neutron/pecan_wsgi/hooks/policy_enforcement.py -> build/lib.linux-i686-2.7/neutron/pecan_wsgi/hooks
copying neutron/pecan_wsgi/hooks/context.py -> build/lib.linux-i686-2.7/neutron/pecan_wsgi/hooks
copying neutron/pecan_wsgi/hooks/quota_enforcement.py -> build/lib.linux-i686-2.7/neutron/pecan_wsgi/hooks
copying neutron/pecan_wsgi/hooks/body_validation.py -> build/lib.linux-i686-2.7/neutron/pecan_wsgi/hooks
copying neutron/pecan_wsgi/hooks/translation.py -> build/lib.linux-i686-2.7/neutron/pecan_wsgi/hooks
copying neutron/pecan_wsgi/hooks/__init__.py -> build/lib.linux-i686-2.7/neutron/pecan_wsgi/hooks
copying neutron/tests/unit/agent/linux/test_ip_link_support.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
copying neutron/tests/unit/agent/linux/test_keepalived.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
copying neutron/tests/unit/agent/linux/test_external_process.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
copying neutron/tests/unit/agent/linux/failing_process.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
copying neutron/tests/unit/agent/linux/test_tc_lib.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
copying neutron/tests/unit/agent/linux/test_async_process.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
copying neutron/tests/unit/agent/linux/test_pd.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
copying neutron/tests/unit/agent/linux/test_polling.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
copying neutron/tests/unit/agent/linux/test_iptables_firewall.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
copying neutron/tests/unit/agent/linux/test_ipset_manager.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
copying neutron/tests/unit/agent/linux/test_daemon.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
copying neutron/tests/unit/agent/linux/test_ip_lib.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
copying neutron/tests/unit/agent/linux/test_dhcp.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
copying neutron/tests/unit/agent/linux/test_utils.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
copying neutron/tests/unit/agent/linux/test_ip_monitor.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
copying neutron/tests/unit/agent/linux/test_iptables_manager.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
copying neutron/tests/unit/agent/linux/test_bridge_lib.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
copying neutron/tests/unit/agent/linux/test_ovsdb_monitor.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
copying neutron/tests/unit/agent/linux/test_ip_conntrack.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
copying neutron/tests/unit/agent/linux/test_interface.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
copying neutron/tests/unit/agent/linux/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/linux
creating build/lib.linux-i686-2.7/neutron/tests/functional/plugins/ml2/drivers/macvtap/agent
copying neutron/tests/functional/plugins/ml2/drivers/macvtap/agent/test_macvtap_neutron_agent.py -> build/lib.linux-i686-2.7/neutron/tests/functional/plugins/ml2/drivers/macvtap/agent
copying neutron/tests/functional/plugins/ml2/drivers/macvtap/agent/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/plugins/ml2/drivers/macvtap/agent
copying neutron/api/rpc/callbacks/resource_manager.py -> build/lib.linux-i686-2.7/neutron/api/rpc/callbacks
copying neutron/api/rpc/callbacks/resources.py -> build/lib.linux-i686-2.7/neutron/api/rpc/callbacks
copying neutron/api/rpc/callbacks/exceptions.py -> build/lib.linux-i686-2.7/neutron/api/rpc/callbacks
copying neutron/api/rpc/callbacks/version_manager.py -> build/lib.linux-i686-2.7/neutron/api/rpc/callbacks
copying neutron/api/rpc/callbacks/events.py -> build/lib.linux-i686-2.7/neutron/api/rpc/callbacks
copying neutron/api/rpc/callbacks/__init__.py -> build/lib.linux-i686-2.7/neutron/api/rpc/callbacks
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/extensions
copying neutron/plugins/ml2/extensions/qos.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/extensions
copying neutron/plugins/ml2/extensions/dns_integration.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/extensions
copying neutron/plugins/ml2/extensions/port_security.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/extensions
copying neutron/plugins/ml2/extensions/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/extensions
creating build/lib.linux-i686-2.7/neutron/tests/unit/services/bgp/agent
copying neutron/tests/unit/services/bgp/agent/test_bgp_dragent.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/bgp/agent
copying neutron/tests/unit/services/bgp/agent/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/bgp/agent
creating build/lib.linux-i686-2.7/neutron/tests/unit/agent/metadata
copying neutron/tests/unit/agent/metadata/test_agent.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/metadata
copying neutron/tests/unit/agent/metadata/test_driver.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/metadata
copying neutron/tests/unit/agent/metadata/test_namespace_proxy.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/metadata
copying neutron/tests/unit/agent/metadata/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/agent/metadata
copying neutron/services/firewall/agents/firewall_agent_api.py -> build/lib.linux-i686-2.7/neutron/services/firewall/agents
copying neutron/services/firewall/agents/__init__.py -> build/lib.linux-i686-2.7/neutron/services/firewall/agents
creating build/lib.linux-i686-2.7/neutron/services/externaldns/drivers
creating build/lib.linux-i686-2.7/neutron/services/externaldns/drivers/designate
copying neutron/services/externaldns/drivers/designate/driver.py -> build/lib.linux-i686-2.7/neutron/services/externaldns/drivers/designate
copying neutron/services/externaldns/drivers/designate/__init__.py -> build/lib.linux-i686-2.7/neutron/services/externaldns/drivers/designate
creating build/lib.linux-i686-2.7/neutron/services/timestamp
copying neutron/services/timestamp/timestamp_db.py -> build/lib.linux-i686-2.7/neutron/services/timestamp
copying neutron/services/timestamp/timestamp_plugin.py -> build/lib.linux-i686-2.7/neutron/services/timestamp
copying neutron/services/timestamp/__init__.py -> build/lib.linux-i686-2.7/neutron/services/timestamp
copying neutron/i18n.py -> build/lib.linux-i686-2.7/neutron
copying neutron/_i18n.py -> build/lib.linux-i686-2.7/neutron
copying neutron/worker.py -> build/lib.linux-i686-2.7/neutron
copying neutron/neutron_plugin_base_v2.py -> build/lib.linux-i686-2.7/neutron
copying neutron/wsgi.py -> build/lib.linux-i686-2.7/neutron
copying neutron/service.py -> build/lib.linux-i686-2.7/neutron
copying neutron/policy.py -> build/lib.linux-i686-2.7/neutron
copying neutron/context.py -> build/lib.linux-i686-2.7/neutron
copying neutron/opts.py -> build/lib.linux-i686-2.7/neutron
copying neutron/manager.py -> build/lib.linux-i686-2.7/neutron
copying neutron/auth.py -> build/lib.linux-i686-2.7/neutron
copying neutron/version.py -> build/lib.linux-i686-2.7/neutron
copying neutron/__init__.py -> build/lib.linux-i686-2.7/neutron
creating build/lib.linux-i686-2.7/neutron/services/qos
copying neutron/services/qos/qos_plugin.py -> build/lib.linux-i686-2.7/neutron/services/qos
copying neutron/services/qos/qos_consts.py -> build/lib.linux-i686-2.7/neutron/services/qos
copying neutron/services/qos/__init__.py -> build/lib.linux-i686-2.7/neutron/services/qos
creating build/lib.linux-i686-2.7/neutron/tests/unit/services/metering/agents
copying neutron/tests/unit/services/metering/agents/test_metering_agent.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/metering/agents
copying neutron/tests/unit/services/metering/agents/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/metering/agents
creating build/lib.linux-i686-2.7/neutron/tests/tempest/services/network/json
copying neutron/tests/tempest/services/network/json/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/tempest/services/network/json
copying neutron/tests/tempest/services/network/json/network_client.py -> build/lib.linux-i686-2.7/neutron/tests/tempest/services/network/json
creating build/lib.linux-i686-2.7/neutron/tests/functional/db
copying neutron/tests/functional/db/test_migrations.py -> build/lib.linux-i686-2.7/neutron/tests/functional/db
copying neutron/tests/functional/db/test_models.py -> build/lib.linux-i686-2.7/neutron/tests/functional/db
copying neutron/tests/functional/db/test_ipam.py -> build/lib.linux-i686-2.7/neutron/tests/functional/db
copying neutron/tests/functional/db/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/db
copying neutron/ipam/drivers/__init__.py -> build/lib.linux-i686-2.7/neutron/ipam/drivers
copying neutron/api/versions.py -> build/lib.linux-i686-2.7/neutron/api
copying neutron/api/api_common.py -> build/lib.linux-i686-2.7/neutron/api
copying neutron/api/extensions.py -> build/lib.linux-i686-2.7/neutron/api
copying neutron/api/__init__.py -> build/lib.linux-i686-2.7/neutron/api
creating build/lib.linux-i686-2.7/neutron/scheduler
copying neutron/scheduler/base_resource_filter.py -> build/lib.linux-i686-2.7/neutron/scheduler
copying neutron/scheduler/dhcp_agent_scheduler.py -> build/lib.linux-i686-2.7/neutron/scheduler
copying neutron/scheduler/base_scheduler.py -> build/lib.linux-i686-2.7/neutron/scheduler
copying neutron/scheduler/l3_agent_scheduler.py -> build/lib.linux-i686-2.7/neutron/scheduler
copying neutron/scheduler/__init__.py -> build/lib.linux-i686-2.7/neutron/scheduler
copying neutron/cmd/ovs_cleanup.py -> build/lib.linux-i686-2.7/neutron/cmd
copying neutron/cmd/keepalived_state_change.py -> build/lib.linux-i686-2.7/neutron/cmd
copying neutron/cmd/netns_cleanup.py -> build/lib.linux-i686-2.7/neutron/cmd
copying neutron/cmd/ipset_cleanup.py -> build/lib.linux-i686-2.7/neutron/cmd
copying neutron/cmd/linuxbridge_cleanup.py -> build/lib.linux-i686-2.7/neutron/cmd
copying neutron/cmd/sanity_check.py -> build/lib.linux-i686-2.7/neutron/cmd
copying neutron/cmd/pd_notify.py -> build/lib.linux-i686-2.7/neutron/cmd
copying neutron/cmd/__init__.py -> build/lib.linux-i686-2.7/neutron/cmd
copying neutron/tests/functional/agent/l2/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/l2
copying neutron/tests/functional/agent/l2/base.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/l2
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/common
copying neutron/plugins/ml2/common/exceptions.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/common
copying neutron/plugins/ml2/common/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/common
creating build/lib.linux-i686-2.7/neutron/tests/unit/ipam/drivers/neutrondb_ipam
copying neutron/tests/unit/ipam/drivers/neutrondb_ipam/test_driver.py -> build/lib.linux-i686-2.7/neutron/tests/unit/ipam/drivers/neutrondb_ipam
copying neutron/tests/unit/ipam/drivers/neutrondb_ipam/test_db_api.py -> build/lib.linux-i686-2.7/neutron/tests/unit/ipam/drivers/neutrondb_ipam
copying neutron/tests/unit/ipam/drivers/neutrondb_ipam/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/ipam/drivers/neutrondb_ipam
creating build/lib.linux-i686-2.7/neutron/common
copying neutron/common/config.py -> build/lib.linux-i686-2.7/neutron/common
copying neutron/common/exceptions.py -> build/lib.linux-i686-2.7/neutron/common
copying neutron/common/utils.py -> build/lib.linux-i686-2.7/neutron/common
copying neutron/common/_deprecate.py -> build/lib.linux-i686-2.7/neutron/common
copying neutron/common/topics.py -> build/lib.linux-i686-2.7/neutron/common
copying neutron/common/ipv6_utils.py -> build/lib.linux-i686-2.7/neutron/common
copying neutron/common/test_lib.py -> build/lib.linux-i686-2.7/neutron/common
copying neutron/common/rpc.py -> build/lib.linux-i686-2.7/neutron/common
copying neutron/common/constants.py -> build/lib.linux-i686-2.7/neutron/common
copying neutron/common/__init__.py -> build/lib.linux-i686-2.7/neutron/common
copying neutron/common/eventlet_utils.py -> build/lib.linux-i686-2.7/neutron/common
creating build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/macvtap/mech_driver
copying neutron/tests/unit/plugins/ml2/drivers/macvtap/mech_driver/test_mech_macvtap.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/macvtap/mech_driver
copying neutron/tests/unit/plugins/ml2/drivers/macvtap/mech_driver/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/macvtap/mech_driver
creating build/lib.linux-i686-2.7/neutron/services/metering/drivers/iptables
copying neutron/services/metering/drivers/iptables/iptables_driver.py -> build/lib.linux-i686-2.7/neutron/services/metering/drivers/iptables
copying neutron/services/metering/drivers/iptables/__init__.py -> build/lib.linux-i686-2.7/neutron/services/metering/drivers/iptables
copying neutron/agent/securitygroups_rpc.py -> build/lib.linux-i686-2.7/neutron/agent
copying neutron/agent/metadata_agent.py -> build/lib.linux-i686-2.7/neutron/agent
copying neutron/agent/firewall.py -> build/lib.linux-i686-2.7/neutron/agent
copying neutron/agent/dhcp_agent.py -> build/lib.linux-i686-2.7/neutron/agent
copying neutron/agent/rpc.py -> build/lib.linux-i686-2.7/neutron/agent
copying neutron/agent/l3_agent.py -> build/lib.linux-i686-2.7/neutron/agent
copying neutron/agent/__init__.py -> build/lib.linux-i686-2.7/neutron/agent
copying neutron/tests/unit/plugins/ml2/drivers/linuxbridge/agent/test_linuxbridge_neutron_agent.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/linuxbridge/agent
copying neutron/tests/unit/plugins/ml2/drivers/linuxbridge/agent/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/plugins/ml2/drivers/linuxbridge/agent
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/linuxbridge/agent/common
copying neutron/plugins/ml2/drivers/linuxbridge/agent/common/config.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/linuxbridge/agent/common
copying neutron/plugins/ml2/drivers/linuxbridge/agent/common/constants.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/linuxbridge/agent/common
copying neutron/plugins/ml2/drivers/linuxbridge/agent/common/__init__.py -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/linuxbridge/agent/common
creating build/lib.linux-i686-2.7/neutron/openstack/common
creating build/lib.linux-i686-2.7/neutron/openstack/common/cache
creating build/lib.linux-i686-2.7/neutron/openstack/common/cache/_backends
copying neutron/openstack/common/cache/_backends/memory.py -> build/lib.linux-i686-2.7/neutron/openstack/common/cache/_backends
copying neutron/openstack/common/cache/_backends/__init__.py -> build/lib.linux-i686-2.7/neutron/openstack/common/cache/_backends
creating build/lib.linux-i686-2.7/neutron/agent/dhcp
copying neutron/agent/dhcp/config.py -> build/lib.linux-i686-2.7/neutron/agent/dhcp
copying neutron/agent/dhcp/agent.py -> build/lib.linux-i686-2.7/neutron/agent/dhcp
copying neutron/agent/dhcp/__init__.py -> build/lib.linux-i686-2.7/neutron/agent/dhcp
copying neutron/pecan_wsgi/app.py -> build/lib.linux-i686-2.7/neutron/pecan_wsgi
copying neutron/pecan_wsgi/startup.py -> build/lib.linux-i686-2.7/neutron/pecan_wsgi
copying neutron/pecan_wsgi/constants.py -> build/lib.linux-i686-2.7/neutron/pecan_wsgi
copying neutron/pecan_wsgi/__init__.py -> build/lib.linux-i686-2.7/neutron/pecan_wsgi
copying neutron/tests/common/machine_fixtures.py -> build/lib.linux-i686-2.7/neutron/tests/common
copying neutron/tests/common/config_fixtures.py -> build/lib.linux-i686-2.7/neutron/tests/common
copying neutron/tests/common/helpers.py -> build/lib.linux-i686-2.7/neutron/tests/common
copying neutron/tests/common/conn_testers.py -> build/lib.linux-i686-2.7/neutron/tests/common
copying neutron/tests/common/net_helpers.py -> build/lib.linux-i686-2.7/neutron/tests/common
copying neutron/tests/common/l3_test_common.py -> build/lib.linux-i686-2.7/neutron/tests/common
copying neutron/tests/common/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/common
copying neutron/tests/common/base.py -> build/lib.linux-i686-2.7/neutron/tests/common
copying neutron/openstack/common/cache/cache.py -> build/lib.linux-i686-2.7/neutron/openstack/common/cache
copying neutron/openstack/common/cache/backends.py -> build/lib.linux-i686-2.7/neutron/openstack/common/cache
copying neutron/openstack/common/cache/__init__.py -> build/lib.linux-i686-2.7/neutron/openstack/common/cache
copying neutron/tests/unit/services/bgp/driver/test_utils.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/bgp/driver
copying neutron/tests/unit/services/bgp/driver/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/services/bgp/driver
copying neutron/openstack/common/__init__.py -> build/lib.linux-i686-2.7/neutron/openstack/common
creating build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux/bin
copying neutron/tests/functional/agent/linux/bin/ipt_binname.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux/bin
copying neutron/tests/functional/agent/linux/bin/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/functional/agent/linux/bin
creating build/lib.linux-i686-2.7/neutron/services/qos/notification_drivers
copying neutron/services/qos/notification_drivers/message_queue.py -> build/lib.linux-i686-2.7/neutron/services/qos/notification_drivers
copying neutron/services/qos/notification_drivers/qos_base.py -> build/lib.linux-i686-2.7/neutron/services/qos/notification_drivers
copying neutron/services/qos/notification_drivers/manager.py -> build/lib.linux-i686-2.7/neutron/services/qos/notification_drivers
copying neutron/services/qos/notification_drivers/__init__.py -> build/lib.linux-i686-2.7/neutron/services/qos/notification_drivers
copying neutron/services/bgp/driver/exceptions.py -> build/lib.linux-i686-2.7/neutron/services/bgp/driver
copying neutron/services/bgp/driver/utils.py -> build/lib.linux-i686-2.7/neutron/services/bgp/driver
copying neutron/services/bgp/driver/__init__.py -> build/lib.linux-i686-2.7/neutron/services/bgp/driver
copying neutron/services/bgp/driver/base.py -> build/lib.linux-i686-2.7/neutron/services/bgp/driver
creating build/lib.linux-i686-2.7/neutron/db/qos
copying neutron/db/qos/api.py -> build/lib.linux-i686-2.7/neutron/db/qos
copying neutron/db/qos/models.py -> build/lib.linux-i686-2.7/neutron/db/qos
copying neutron/db/qos/__init__.py -> build/lib.linux-i686-2.7/neutron/db/qos
copying neutron/tests/tools.py -> build/lib.linux-i686-2.7/neutron/tests
copying neutron/tests/post_mortem_debug.py -> build/lib.linux-i686-2.7/neutron/tests
copying neutron/tests/fake_notifier.py -> build/lib.linux-i686-2.7/neutron/tests
copying neutron/tests/__init__.py -> build/lib.linux-i686-2.7/neutron/tests
copying neutron/tests/base.py -> build/lib.linux-i686-2.7/neutron/tests
creating build/lib.linux-i686-2.7/neutron/cmd/eventlet/plugins
copying neutron/cmd/eventlet/plugins/sriov_nic_neutron_agent.py -> build/lib.linux-i686-2.7/neutron/cmd/eventlet/plugins
copying neutron/cmd/eventlet/plugins/ovs_neutron_agent.py -> build/lib.linux-i686-2.7/neutron/cmd/eventlet/plugins
copying neutron/cmd/eventlet/plugins/macvtap_neutron_agent.py -> build/lib.linux-i686-2.7/neutron/cmd/eventlet/plugins
copying neutron/cmd/eventlet/plugins/__init__.py -> build/lib.linux-i686-2.7/neutron/cmd/eventlet/plugins
copying neutron/cmd/eventlet/plugins/linuxbridge_neutron_agent.py -> build/lib.linux-i686-2.7/neutron/cmd/eventlet/plugins
copying neutron/tests/unit/db/test_ipam_non_pluggable_backend.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/tests/unit/db/test_ipam_backend_mixin.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/tests/unit/db/test_ipam_pluggable_backend.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/tests/unit/db/test_portsecurity_db.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/tests/unit/db/test_l3_dvr_db.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/tests/unit/db/test_l3_db.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/tests/unit/db/test_migration.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/tests/unit/db/test_api.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/tests/unit/db/test_securitygroups_db.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/tests/unit/db/test_portsecurity_db_common.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/tests/unit/db/test_db_base_plugin_common.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/tests/unit/db/test_sqlalchemytypes.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/tests/unit/db/test_allowedaddresspairs_db.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/tests/unit/db/test_common_db_mixin.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/tests/unit/db/test_dvr_mac_db.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/tests/unit/db/test_agentschedulers_db.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/tests/unit/db/test_bgp_dragentscheduler_db.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/tests/unit/db/test_db_base_plugin_v2.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/tests/unit/db/test_bgp_db.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/tests/unit/db/test_agents_db.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/tests/unit/db/__init__.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/tests/unit/db/test_l3_hamode_db.py -> build/lib.linux-i686-2.7/neutron/tests/unit/db
copying neutron/services/externaldns/drivers/__init__.py -> build/lib.linux-i686-2.7/neutron/services/externaldns/drivers
creating build/lib.linux-i686-2.7/neutron/objects/qos
copying neutron/objects/qos/rule.py -> build/lib.linux-i686-2.7/neutron/objects/qos
copying neutron/objects/qos/rule_type.py -> build/lib.linux-i686-2.7/neutron/objects/qos
copying neutron/objects/qos/policy.py -> build/lib.linux-i686-2.7/neutron/objects/qos
copying neutron/objects/qos/__init__.py -> build/lib.linux-i686-2.7/neutron/objects/qos
running egg_info
creating neutron.egg-info
writing pbr to neutron.egg-info/pbr.json
writing requirements to neutron.egg-info/requires.txt
writing neutron.egg-info/PKG-INFO
writing top-level names to neutron.egg-info/top_level.txt
writing dependency_links to neutron.egg-info/dependency_links.txt
writing entry points to neutron.egg-info/entry_points.txt
[pbr] Processing SOURCES.txt
writing manifest file 'neutron.egg-info/SOURCES.txt'
[pbr] In git context, generating filelist from git
warning: no files found matching 'AUTHORS'
warning: no files found matching 'ChangeLog'
warning: no previously-included files matching '*.pyc' found anywhere in distribution
reading manifest template 'MANIFEST.in'
warning: no files found matching 'AUTHORS'
warning: no files found matching 'ChangeLog'
warning: no previously-included files found matching '.gitignore'
warning: no previously-included files found matching '.gitreview'
warning: no previously-included files matching '*.pyc' found anywhere in distribution
writing manifest file 'neutron.egg-info/SOURCES.txt'
copying neutron/db/migration/alembic_migrations/script.py.mako -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations
creating build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions
copying neutron/db/migration/alembic_migrations/versions/CONTRACT_HEAD -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions
copying neutron/db/migration/alembic_migrations/versions/EXPAND_HEAD -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions
copying neutron/db/migration/alembic_migrations/versions/README -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions
copying neutron/db/migration/alembic_migrations/versions/kilo_initial.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions
creating build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty
creating build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty/contract
copying neutron/db/migration/alembic_migrations/versions/liberty/contract/11926bcfe72d_add_geneve_ml2_type_driver.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty/contract
copying neutron/db/migration/alembic_migrations/versions/liberty/contract/2a16083502f3_metaplugin_removal.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty/contract
copying neutron/db/migration/alembic_migrations/versions/liberty/contract/2e5352a0ad4d_add_missing_foreign_keys.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty/contract
copying neutron/db/migration/alembic_migrations/versions/liberty/contract/30018084ec99_initial.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty/contract
copying neutron/db/migration/alembic_migrations/versions/liberty/contract/4af11ca47297_drop_cisco_monolithic_tables.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty/contract
copying neutron/db/migration/alembic_migrations/versions/liberty/contract/4ffceebfada_rbac_network.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty/contract
copying neutron/db/migration/alembic_migrations/versions/liberty/contract/5498d17be016_drop_legacy_ovs_and_lb.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty/contract
creating build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty/expand
copying neutron/db/migration/alembic_migrations/versions/liberty/expand/1b4c6e320f79_address_scope_support_in_subnetpool.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty/expand
copying neutron/db/migration/alembic_migrations/versions/liberty/expand/1c844d1677f7_dns_nameservers_order.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty/expand
copying neutron/db/migration/alembic_migrations/versions/liberty/expand/26c371498592_subnetpool_hash.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty/expand
copying neutron/db/migration/alembic_migrations/versions/liberty/expand/31337ec0ffee_flavors.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty/expand
copying neutron/db/migration/alembic_migrations/versions/liberty/expand/34af2b5c5a59_add_dns_name_to_port.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty/expand
copying neutron/db/migration/alembic_migrations/versions/liberty/expand/354db87e3225_nsxv_vdr_metadata.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty/expand
copying neutron/db/migration/alembic_migrations/versions/liberty/expand/45f955889773_quota_usage.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty/expand
copying neutron/db/migration/alembic_migrations/versions/liberty/expand/48153cb5f051_qos_db_changes.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty/expand
copying neutron/db/migration/alembic_migrations/versions/liberty/expand/52c5312f6baf_address_scopes.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty/expand
copying neutron/db/migration/alembic_migrations/versions/liberty/expand/599c6a226151_neutrodb_ipam.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty/expand
copying neutron/db/migration/alembic_migrations/versions/liberty/expand/8675309a5c4f_rbac_network.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty/expand
copying neutron/db/migration/alembic_migrations/versions/liberty/expand/9859ac9c136_quota_reservations.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/liberty/expand
creating build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka
creating build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/contract
copying neutron/db/migration/alembic_migrations/versions/mitaka/contract/1b294093239c_remove_embrane_plugin.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/contract
copying neutron/db/migration/alembic_migrations/versions/mitaka/contract/2b4c2465d44b_dvr_sheduling_refactoring.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/contract
copying neutron/db/migration/alembic_migrations/versions/mitaka/contract/4ffceebfcdc_standard_desc.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/contract
copying neutron/db/migration/alembic_migrations/versions/mitaka/contract/5ffceebfada_rbac_network_external.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/contract
copying neutron/db/migration/alembic_migrations/versions/mitaka/contract/8a6d8bdae39_migrate_neutron_resources_table.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/contract
copying neutron/db/migration/alembic_migrations/versions/mitaka/contract/c6c112992c9_rbac_qos_policy.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/contract
copying neutron/db/migration/alembic_migrations/versions/mitaka/contract/e3278ee65050_drop_nec_plugin_tables.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/contract
creating build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/expand
copying neutron/db/migration/alembic_migrations/versions/mitaka/expand/0e66c5227a8a_add_desc_to_standard_attr.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/expand
copying neutron/db/migration/alembic_migrations/versions/mitaka/expand/13cfb89f881a_add_is_default_to_subnetpool.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/expand
copying neutron/db/migration/alembic_migrations/versions/mitaka/expand/15be73214821_add_bgp_model_data.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/expand
copying neutron/db/migration/alembic_migrations/versions/mitaka/expand/15e43b934f81_rbac_qos_policy.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/expand
copying neutron/db/migration/alembic_migrations/versions/mitaka/expand/19f26505c74f_auto_allocated_topology.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/expand
copying neutron/db/migration/alembic_migrations/versions/mitaka/expand/1df244e556f5_add_unique_ha_router_agent_port_bindings.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/expand
copying neutron/db/migration/alembic_migrations/versions/mitaka/expand/2f9e956e7532_tag_support.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/expand
copying neutron/db/migration/alembic_migrations/versions/mitaka/expand/31ed664953e6_add_resource_versions_row_to_agent_table.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/expand
copying neutron/db/migration/alembic_migrations/versions/mitaka/expand/32e5974ada25_add_neutron_resources_table.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/expand
copying neutron/db/migration/alembic_migrations/versions/mitaka/expand/3894bccad37f_add_timestamp_to_base_resources.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/expand
copying neutron/db/migration/alembic_migrations/versions/mitaka/expand/59cb5b6cf4d_availability_zone.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/expand
copying neutron/db/migration/alembic_migrations/versions/mitaka/expand/659bf3d90664_add_attributes_to_support_external_dns_integration.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/expand
copying neutron/db/migration/alembic_migrations/versions/mitaka/expand/b4caf27aae4_add_bgp_dragent_model_data.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/expand
copying neutron/db/migration/alembic_migrations/versions/mitaka/expand/c3a73f615e4_add_ip_version_to_address_scope.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/expand
copying neutron/db/migration/alembic_migrations/versions/mitaka/expand/dce3ec7a25c9_router_az.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/expand
copying neutron/db/migration/alembic_migrations/versions/mitaka/expand/ec7fcfbf72ee_network_az.py -> build/lib.linux-i686-2.7/neutron/db/migration/alembic_migrations/versions/mitaka/expand
copying neutron/tests/functional/requirements.txt -> build/lib.linux-i686-2.7/neutron/tests/functional
copying neutron/tests/api/requirements.txt -> build/lib.linux-i686-2.7/neutron/tests/api
copying neutron/tests/tempest/README.rst -> build/lib.linux-i686-2.7/neutron/tests/tempest
copying neutron/plugins/ml2/drivers/l2pop/README -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/l2pop
copying neutron/plugins/ml2/README -> build/lib.linux-i686-2.7/neutron/plugins/ml2
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/xenapi
copying neutron/plugins/ml2/drivers/openvswitch/agent/xenapi/README -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/xenapi
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/xenapi/contrib
copying neutron/plugins/ml2/drivers/openvswitch/agent/xenapi/contrib/build-rpm.sh -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/xenapi/contrib
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/xenapi/contrib/rpmbuild
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/xenapi/contrib/rpmbuild/SPECS
copying neutron/plugins/ml2/drivers/openvswitch/agent/xenapi/contrib/rpmbuild/SPECS/openstack-quantum-xen-plugins.spec -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/xenapi/contrib/rpmbuild/SPECS
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/xenapi/etc
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/xenapi/etc/xapi.d
creating build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/xenapi/etc/xapi.d/plugins
copying neutron/plugins/ml2/drivers/openvswitch/agent/xenapi/etc/xapi.d/plugins/netwrap -> build/lib.linux-i686-2.7/neutron/plugins/ml2/drivers/openvswitch/agent/xenapi/etc/xapi.d/plugins
copying neutron/db/migration/README -> build/lib.linux-i686-2.7/neutron/db/migration
copying neutron/db/migration/alembic.ini -> build/lib.linux-i686-2.7/neutron/db/migration
copying neutron/services/l3_router/README -> build/lib.linux-i686-2.7/neutron/services/l3_router
copying neutron/tests/fullstack/README -> build/lib.linux-i686-2.7/neutron/tests/fullstack
copying neutron/tests/unit/tests/example/README -> build/lib.linux-i686-2.7/neutron/tests/unit/tests/example
copying neutron/debug/README -> build/lib.linux-i686-2.7/neutron/debug
creating build/lib.linux-i686-2.7/neutron/locale
creating build/lib.linux-i686-2.7/neutron/locale/de
creating build/lib.linux-i686-2.7/neutron/locale/de/LC_MESSAGES
copying neutron/locale/de/LC_MESSAGES/neutron.po -> build/lib.linux-i686-2.7/neutron/locale/de/LC_MESSAGES
creating build/lib.linux-i686-2.7/neutron/locale/es
creating build/lib.linux-i686-2.7/neutron/locale/es/LC_MESSAGES
copying neutron/locale/es/LC_MESSAGES/neutron.po -> build/lib.linux-i686-2.7/neutron/locale/es/LC_MESSAGES
creating build/lib.linux-i686-2.7/neutron/locale/fr
creating build/lib.linux-i686-2.7/neutron/locale/fr/LC_MESSAGES
copying neutron/locale/fr/LC_MESSAGES/neutron.po -> build/lib.linux-i686-2.7/neutron/locale/fr/LC_MESSAGES
creating build/lib.linux-i686-2.7/neutron/locale/it
creating build/lib.linux-i686-2.7/neutron/locale/it/LC_MESSAGES
copying neutron/locale/it/LC_MESSAGES/neutron.po -> build/lib.linux-i686-2.7/neutron/locale/it/LC_MESSAGES
creating build/lib.linux-i686-2.7/neutron/locale/ja
creating build/lib.linux-i686-2.7/neutron/locale/ja/LC_MESSAGES
copying neutron/locale/ja/LC_MESSAGES/neutron.po -> build/lib.linux-i686-2.7/neutron/locale/ja/LC_MESSAGES
creating build/lib.linux-i686-2.7/neutron/locale/ko_KR
creating build/lib.linux-i686-2.7/neutron/locale/ko_KR/LC_MESSAGES
copying neutron/locale/ko_KR/LC_MESSAGES/neutron-log-error.po -> build/lib.linux-i686-2.7/neutron/locale/ko_KR/LC_MESSAGES
copying neutron/locale/ko_KR/LC_MESSAGES/neutron-log-info.po -> build/lib.linux-i686-2.7/neutron/locale/ko_KR/LC_MESSAGES
copying neutron/locale/ko_KR/LC_MESSAGES/neutron-log-warning.po -> build/lib.linux-i686-2.7/neutron/locale/ko_KR/LC_MESSAGES
copying neutron/locale/ko_KR/LC_MESSAGES/neutron.po -> build/lib.linux-i686-2.7/neutron/locale/ko_KR/LC_MESSAGES
creating build/lib.linux-i686-2.7/neutron/locale/pt_BR
creating build/lib.linux-i686-2.7/neutron/locale/pt_BR/LC_MESSAGES
copying neutron/locale/pt_BR/LC_MESSAGES/neutron.po -> build/lib.linux-i686-2.7/neutron/locale/pt_BR/LC_MESSAGES
creating build/lib.linux-i686-2.7/neutron/locale/ru
creating build/lib.linux-i686-2.7/neutron/locale/ru/LC_MESSAGES
copying neutron/locale/ru/LC_MESSAGES/neutron.po -> build/lib.linux-i686-2.7/neutron/locale/ru/LC_MESSAGES
creating build/lib.linux-i686-2.7/neutron/locale/tr_TR
creating build/lib.linux-i686-2.7/neutron/locale/tr_TR/LC_MESSAGES
copying neutron/locale/tr_TR/LC_MESSAGES/neutron-log-error.po -> build/lib.linux-i686-2.7/neutron/locale/tr_TR/LC_MESSAGES
copying neutron/locale/tr_TR/LC_MESSAGES/neutron-log-info.po -> build/lib.linux-i686-2.7/neutron/locale/tr_TR/LC_MESSAGES
copying neutron/locale/tr_TR/LC_MESSAGES/neutron-log-warning.po -> build/lib.linux-i686-2.7/neutron/locale/tr_TR/LC_MESSAGES
copying neutron/locale/tr_TR/LC_MESSAGES/neutron.po -> build/lib.linux-i686-2.7/neutron/locale/tr_TR/LC_MESSAGES
creating build/lib.linux-i686-2.7/neutron/locale/zh_CN
creating build/lib.linux-i686-2.7/neutron/locale/zh_CN/LC_MESSAGES
copying neutron/locale/zh_CN/LC_MESSAGES/neutron.po -> build/lib.linux-i686-2.7/neutron/locale/zh_CN/LC_MESSAGES
creating build/lib.linux-i686-2.7/neutron/locale/zh_TW
creating build/lib.linux-i686-2.7/neutron/locale/zh_TW/LC_MESSAGES
copying neutron/locale/zh_TW/LC_MESSAGES/neutron.po -> build/lib.linux-i686-2.7/neutron/locale/zh_TW/LC_MESSAGES
creating build/lib.linux-i686-2.7/neutron/tests/contrib
copying neutron/tests/contrib/README -> build/lib.linux-i686-2.7/neutron/tests/contrib
copying neutron/tests/contrib/functional-testing.filters -> build/lib.linux-i686-2.7/neutron/tests/contrib
copying neutron/tests/contrib/gate_hook.sh -> build/lib.linux-i686-2.7/neutron/tests/contrib
copying neutron/tests/contrib/post_test_hook.sh -> build/lib.linux-i686-2.7/neutron/tests/contrib
creating build/lib.linux-i686-2.7/neutron/tests/etc
copying neutron/tests/etc/api-paste.ini.test -> build/lib.linux-i686-2.7/neutron/tests/etc
copying neutron/tests/etc/neutron.conf -> build/lib.linux-i686-2.7/neutron/tests/etc
copying neutron/tests/etc/neutron_test.conf -> build/lib.linux-i686-2.7/neutron/tests/etc
copying neutron/tests/etc/neutron_test2.conf.example -> build/lib.linux-i686-2.7/neutron/tests/etc
copying neutron/tests/etc/policy.json -> build/lib.linux-i686-2.7/neutron/tests/etc
creating build/lib.linux-i686-2.7/neutron/tests/var
copying neutron/tests/var/ca.crt -> build/lib.linux-i686-2.7/neutron/tests/var
copying neutron/tests/var/certandkey.pem -> build/lib.linux-i686-2.7/neutron/tests/var
copying neutron/tests/var/certificate.crt -> build/lib.linux-i686-2.7/neutron/tests/var
copying neutron/tests/var/privatekey.key -> build/lib.linux-i686-2.7/neutron/tests/var
running build_scripts
creating build/scripts-2.7
copying and adjusting bin/neutron-rootwrap-xen-dom0 -> build/scripts-2.7
changing mode of build/scripts-2.7/neutron-rootwrap-xen-dom0 from 664 to 775
