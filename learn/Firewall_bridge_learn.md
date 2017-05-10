1. http://www.aboutyun.com/forum.php?mod=viewthread&tid=16712&highlight=neutron%2B%2B%CF%B5%C1%D0
2. https://upload.wikimedia.org/wikipedia/commons/3/37/Netfilter-packet-flow.svg

FIREWALL种类?
------------

- outside/inside/DMZ network.
- L4 FW, L7 FW.
- main FW, distribute FW.
- rule, stratgy.
- IP Spoofing.


RULES of IPTABLES?
-----------------

#允许本机通过访问外网，但是将进来的 udp，tcp 和 icmp 的网络包写日志（INPUT 规则的 physdev-in 肯定是 eth1 了）
iptables -A INPUT -p udp -m physdev --physdev-in eth1 -j LOG
iptables -A INPUT -p tcp -m physdev --physdev-in eth1 -j LOG
iptables -A INPUT -p icmp -m physdev --physdev-in eth1 -j LOG

# 允许 ssh, smtp and http 到 br0(INPUT!)
iptables -A INPUT -p tcp --dport 22 -m physdev --physdev-in eth1 -j ACCEPT
iptables -A INPUT -p tcp --dport 25 -m physdev --physdev-in eth1 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -m physdev --physdev-in eth1 -j ACCEPT

# 拒绝到 br0 的别的网络包
iptables -A INPUT -p tcp --syn -m physdev --physdev-in eth1 -J REJECT

# 允许通过 tcp 端口 22（ssh），25 （smtp），80（http）到内网
iptables -A FORWARD -p tcp --dport 22 -m physdev --physdev-in eth1 --physdev-out eth0 -j ACCEPT
iptables -A FORWARD -p tcp --dport 25 -m physdev --physdev-in eth1 --physdev-out eth0 -j ACCEPT
iptables -A FORWARD -p tcp --dport 80 -m physdev --physdev-in eth1 --physdev-out eth0 -j ACCEPT

# 禁止 tcp 端口 6667 （IRC）
iptables -A FORWARD -p tcp --dport 6667 -m physdev --physdev-in eth1 -j REJECT

# 禁止其它连接到内网
iptables -A FORWARD -p tcp --syn -m physdev --physdev-in eth1 --physdev-out eth0 -j REJECT


IPSET?
-----

refer <1>


SECURITY GROUP, FWaas?
---------------------

refer <1>中“2. Neutron 防火墙和安全组概述”一节中的表。这个很重要。
其中qbr是连接到br-int上的linux bridge，所以之前的理解有些偏差。
