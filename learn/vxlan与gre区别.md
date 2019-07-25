vxlan与gre在tunnul中的区别
--------------------------

http://bingotree.cn/?p=654
由于gre需要建立点对点连接，vxlan不需要（而是由控制器下发vxlan entry），所以在新增计算节点host的时候gre需要新增节点与每个节点建立tunnel，进而增加每个计算节点host的payload。