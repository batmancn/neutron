1. https://docs.openstack.org/developer/neutron/devref/layer3.html
2. <openstack_understand_neutron>

For <1>, DVR is simple: qr-XXX of br-int connect to IP stack, this IP stack route is from L3 Agent which enabled DVR. Flow to east/west and to outside is routing here. Then route entry is qg-VVV of br-ext. This br-ext is response for outside, like vxlan tunnel or vlan tagging.

That's not correct above. Doc said it's configured by L3 Agent???
