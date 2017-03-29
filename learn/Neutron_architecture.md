1. http://www.aboutyun.com/forum.php?mod=viewthread&tid=16464&highlight=neutron%2B%2B%CF%B5%C1%D0


Basic:
- tenant: the user who use cloud, could use L2, L3 ... resource.
- segmentation ID: used for segment L2 network, reliesed by vxlan-id, vlan-id, gre-id ...
- Virtual router: one VR is only for one tenant's L2 network with no IP overlapping.
- all service is around tenant, as thay pay money.


TBD: DHCP http://www.aboutyun.com/forum.php?mod=viewthread&tid=16464&highlight=neutron%2B%2B%CF%B5%C1%D0


Tenant isolation:
（1）计算节点的 br-int 上，neutron 为每个虚机连接 OVS 的 access port 分配了内部的 VLAN Tag。这种 tag 限制了网络流量只能在 tenant network 之内。
（2）计算节点的 br-tun 上，neutron 将内部的 VLAN Tag 转化为 GRE Tunnel ID，是的不同 network 的流量走不通的 tunnel。
（3）网络节点的 br-tun 上，neutron 将 GRE Tunnel ID 转发了一一对应的 内部 VLAN Tag，使得网络流被不同的服务处理。
（4）网络节点的 br-int 上连接的 DHCP 和 L3 agent 使用 Linux network namespace 进行隔离。
从(2)(3)两步看出来vxlan是对vlan的扩展，也就是在数据中心中，vxlan扩展了vlan的数量，使得overlay网络中能承载更多的segment。


Tenant security:
refer <1>


Tenant HA/scapbility:
- openstack software architecutre: plugin mechanism and REST API...
- use vxlan to extend segmentation number.
- use DVR and Distribute-DHCP to reduce network node traffic load.
- use L2 population and arp responder to reduce BUM.
- HA and extension(LBaas, Fwaas, VPNaas) is now not stable, wait for graduate.
