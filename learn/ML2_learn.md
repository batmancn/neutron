http://www.aboutyun.com/thread-16563-1-1.html

br-int: used for connect to VM's linux bridge, use normal mode OVS.
br-tun: used for tunnel for east/west connection between compute node, use flow mode named "secure-mode".

if no arp-response and DVR, use br-tun for with neutron as controller.

ARP-Proxy: OVS with ARP-Proxy to supply ARP function for VMs.
