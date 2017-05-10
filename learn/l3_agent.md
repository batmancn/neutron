http://www.aboutyun.com/forum.php?mod=viewthread&tid=16629&highlight=neutron%2B%2B%CF%B5%C1%D0


概述？
----

参考《1》， 每个 L3 Agent 运行在一个network namespace中，每个namespace由qrouter-<router-UUID>命名。
比如qrouter-e506f8fe-3260-4880-bd06-32246225aeae。

Neutron L3 Agent 负责：
路由（routing）: router_info.py:update_routing_table()
浮动 IP 分配（floatingip allocation）: router_info.py:add_floating_ip()
地址转换（SNAT/DNAT）: external_gateway_nat_snat_rules(), process_floating_ip_nat_rules()
Security Group 管理: router_info.py:process_ports_address_scope_iptables()


floating ip?
-----------

router作为所管辖的fip虚拟机的arp-proxy。
