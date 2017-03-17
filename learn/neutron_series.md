### Reference.

1. <linux内核源码注释 TCPIP 1>


### Neutron系列:

Neutron 所实现的虚拟化网络：
1.为什么要网络虚拟化？
2.Neutron network 可以分为哪几种？什么是provider:network_type，provider:segmentation_id，provider:physical_network？
3.Provider network 和 Tenant network 的区别是什么？
4.OpenStack 内部网络有哪些？
5.虚拟二层网络有哪几种实现方法？
6.Neutron 租户网络是怎样隔离的？
7.什么是虚拟路由？

使用 Open vSwitch + VLAN 组网：
1.VLAN是什么？
2.二层交换机最基本的功能有哪些？
3.Address Resolution Protocol (ARP) 原理是什么？
4.实现OVS+VLAN组网，基本拓扑是什么？怎样配置Neutron(版本变化？？？)？配置生效的过程是？L2-plugin代码？L2-Agent代码？
5.怎样创建虚拟网络和子网（即L3操作）？Nova做了哪些配置？L2-Agent做了什么？
6.compute节点的网络拓扑是什么样？Neutron做了哪些工作？Nova做了哪些工作？
7.OVS+VLAN组网不能使用DVR？
8.Neutron 的虚拟网络分类有哪些？

使用Open vSwitch + GRE/VxLAN 组网：
1、什么是Overlay 网络？GRE是P2P-tunnel、如何封装、如何配置、哪些不足？VXLAN不是P2P封装、如何封装、如何配置、比GRE好的地方在于可以使用多播？
2.什么是VTEP、VXLAN GATEWAY、VXLAN IP GATEWAY？
3、如何使用vxlan设计Overlay方案？混合overlay方案如何部署？
4、如何实现VXLAN？vxlan报文格式？vtep如何寻址？
5、Neutron 如何通过OVS对GRE和VXLAN进行支持？不启用L2POP如何使用多播、广播部署vxlan？启用L2POP如何部署vxlan？OVS自带的VTEPD如何工作？部署之后拓扑见下一个问题。
6.MTU问题？neutron如何自动配置？
7、为什么H3C 选择VxLAN？什么是VXLAN Fabric网络？

Neutron OVS OpenFlow 流表 和 L2 Population：
1.怎样使用arp_responder？ARP responder相关多表编程是什么样的？
2.怎样搭建l2pop环境？端口与bridge信息如何update？
3.neutron怎样的代码流程，如何更新了如下（Tunnel port、 FLOOD_TO_TUN （table 22）flow、 ARP responder flow、UCAST_TO_TUN （table 20） flow）这些L2POP相关配置到OVS上？neutron中ovs_neutron_agent.py中tunnel_sync函数如何理解？
4.实验环境具体配置如何？TBD？？？

Neutron 是如何向 Nova 虚机分配固定IP地址的：
1.怎么去理解Linux network namespace？什么是veth pair端口？
2.怎么去区分netfilter/iptables 基本概念？






Neutron L3 Agent HA 之 虚拟路由冗余协议（VRRP）:
1.虚拟路由冗余协议是什么？
2.什么是Keepalived？Keepalive如何实现VRRP？
3.如何创建 HA Router？Neutron如何实现VRRP？DB中如何操纵？
4.HA Router如何调度？
5.Juno VRRP 实现需要注意什么？
6.Neutron Kilo 新版本都有什么？

OpenStack 高可用和灾备方案 [OpenStack HA and DR]：
1.什么是高可用？
2.HA和DR有什么关系？
3.什么是OpenStack HA?
4.RDD HA的部署方案都有哪些？
5.什么是A/A 方案？
6.网易 OpenStack 云的 HA 方案是什么？
