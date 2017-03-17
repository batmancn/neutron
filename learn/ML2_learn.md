1. http://www.aboutyun.com/thread-16563-1-1.html
2. http://www.aboutyun.com/forum.php?mod=viewthread&tid=16564&highlight=neutron%2B%2B%CF%B5%C1%D0
3. <openstack understand neutron>
4. https://assafmuller.com/2014/05/21/ovs-arp-responder-theory-and-practice/
5. http://www.aboutyun.com/forum.php?mod=viewthread&tid=16476&highlight=neutron%2B%2B%CF%B5%C1%D0
6. http://www.aboutyun.com/forum.php?mod=viewthread&tid=16500&highlight=neutron%2B%2B%CF%B5%C1%D0

BRIDGE:
br-int: used for connect to VM's linux bridge, use normal mode OVS.
br-tun: used for east/west connection between compute node by tunnel(use flow mode named "secure-mode"); used for arp-proxy. This could be instead by hardware switch like VXLAN-GATEWAY.
br-ex: used for connect to outside, use flow mode.

For different mode, functions of br-XXX is different, above is vxlan-tunnel(<6>) network. For ovs-vlan network(<5>) is as bellow:

refer <5> and Ovs_vlan_metworking.md

ARP-RESPONDER:
<2>, use br-tun as ARP Proxy. The arp entries proxied is only local VM's arp entries, other arp entries is set by neutron L2 population.
<4> and <2> introduce how it works, basically speaking, it's done by LEARN table in br-tun. and ARP responder action is done in table 21's flow:
ARP_RESPONDER_ACTIONS = ('move:NXM_OF_ETH_SRC[]->NXM_OF_ETH_DST[],'
                         'mod_dl_src:%(mac)s,'
                         'load:0x2->NXM_OF_ARP_OP[],'
                         'move:NXM_NX_ARP_SHA[]->NXM_NX_ARP_THA[],'
                         'move:NXM_OF_ARP_SPA[]->NXM_OF_ARP_TPA[],'
                         'load:%(mac)#x->NXM_NX_ARP_SHA[],'
                         'load:%(ip)#x->NXM_OF_ARP_SPA[],'
                         'in_port')

L2 POPULATION:
L2 population is used for restrict BUM flood. Neutron as controller know every VM's arp-entry, then send these to all compute node.
Effeciant problem: depands on message queue.
