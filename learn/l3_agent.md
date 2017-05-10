http://www.aboutyun.com/forum.php?mod=viewthread&tid=16629&highlight=neutron%2B%2B%CF%B5%C1%D0


概述？
----

参考《1》， 每个 L3 Agent 运行在一个network namespace中，每个namespace由qrouter-<router-UUID>命名。
比如qrouter-e506f8fe-3260-4880-bd06-32246225aeae。

Neutron L3 Agent 负责：
路由（routing）、
浮动 IP 分配（floatingip allocation），
地址转换（SNAT/DNAT）和
Security Group 管理。
