《1》：openstack设计与实现
《2》：doc_summary.md
《3》：https://www.ustack.com/blog/neutron_intro/
《4》：《openstack understand neutron》
《5》：

1. 安装好之后，代码在：如果使用devstack安装代码在/opt/stack/中；如果使用手工安装，代码在/usr/lib/python2.7/dist-packages/。

2. 入手点在setup.py和setup.cfg中的entry points，解释见《1》《2》。setuptool读取配置之后，使用配置见《1》P36。console_script是特殊的entry points，是命令行直接执行的脚本。

3. 单元测试Tox，tox.ini；Mock。

4. oslo库：
    1）oslo.messing，用于RPC与notification。https://docs.openstack.org/developer/oslo.messaging/。参考./oslo_messing*.py。
    2）SQLAlchemy与ORM。看《1》P94与oslo_sqlalchemy_demo.py。
    3) RESTFull开发：
        - URL mapping是将URL对应到json字符串，与WSGI规范两码事，openstack中使用的URL mapping是routes模块，routes(http://routes.readthedocs.org)，参考《1》P97。
        - 一个controller对应了一个资源，也就是一个URL，action包括GET等，另外还可以带参数。TBD P97(131)
        - WSGI demo见/MyLife/Demos/python_demo/server_demo/wsgi_server_demo。
        - 不同的WSGI中间件使用不同的包装，openstack使用Paste的Deploy(http://pythonpaste.org/deploy/)。
        - Paste文件的格式见《1》。

5. neutron网络抽象：
    - L3 router：代码是L3-Agent。用于抽象路由器，DVR-L3-Agent用于抽象在DVR模式下的路由器。
    - L2 network：代码在ml2, l2pop。其中ml2是用于组建L2-network，支持LB、OVS等mechinism driver；l2pop用于vxlan这样的tunnel模式下大两层的搭建。
    - port：这个参考《3》，是虚拟机（租户）与路由器挂接网络的挂接点。
    - 目前neutron支持五种网络模式(type-driver)：
        -- flat：所有租户在同一个lan中。
        -- vlan/vxlan/gre：《4》

6. neutron架构：
    - neutron只有一个服务进程（neutron-server），在控制节点，提供HTTP RESTFull API，neutron-server最后使用agent完成请求。
    - Plugin的区分：
        -- neutron中的资源分为两类：core、extension resource。
        -- 由于有多种Mechanism Driver、Type Driver，所以neutron使用plugin的方式组织不同种类的driver API。
        -- 基于此，plugin被区分为core plugin(plugins/ml2/*)、service plugin(service/*，例如service/firewall/*，L3 Router Service Plugin(neutron/service/l3_router/l3_router_plugin.py)专门提供router服务)。
    - Agent：一个Agent完成一个功能（例如L3 router）

7. neutron代码：参看《1》P247
.
├── bin：基于oslo.rootwrap提供访问权限配置
│?? └── neutron-rootwrap-xen-dom0
├── doc
├── etc
│?? ├── api-paste.ini：Paste Deploy配置文件（参看4.3节）
│?? ├── bgp_dragent.ini.sample
│?? ├── dhcp_agent.ini.sample：DHCP Agent配置信息，这些ini文件内容自动从代码中提取
│?? ├── l3_agent.ini.sample
│?? ├── metadata_agent.ini.sample
│?? ├── metering_agent.ini.sample
│?? ├── neutron
│?? ├── neutron.conf.sample
│?? ├── oslo-config-generator
│?? ├── policy.json
│?? ├── README.txt
│?? └── rootwrap.conf
├── neutron
│?? ├── agent：所有Agent代码，例如firewall、DHCP Agent。
│?? ├── api：neutron api
│?? ├── callbacks：callback库
│?? ├── cmd：辅助工具
│?? ├── common：配置、异常、常量、日志、通信等通用库
│?? ├── db：数据库模型（各种插件所用的数据库模型）及其API。一般plugin操作都是pre_commit、do_sth、commit、post_commit。
│?? ├── debug：调试辅助工具
│?? ├── extensions：extension api
│?? ├── hacking：编码规范检查
│?? ├── locale：多语言支持
│?? ├── manager.py：解析配置文件、加载core plugin
│?? ├── neutron_plugin_base_v2.py：所有neutron plugin的抽象基类
│?? ├── notifiers：通知nova网络变化
│?? ├── openstack
│?? ├── plugins：core plugin
│?? ├── scheduler：用于调度、负载均衡。每个租户都需要L3、DHCP功能，那么不能所有租户都使用一个L3、DHCP Agent吧，所以需要这里进行调度，也就是通过《5》.scheduler一节介绍的API提供这样的功能，使得一组租户映射到一个L3、DHCP Agent上。
|   |    ├── dhcp_agent_scheduler.py
|   |    └── l3_agent_scheduler.py
│?? ├── server：neutron-server
│?? ├── service.py：所以service的基类
│?? ├── services：service plugin
│?? ├── tests：单元测试
├── setup.cfg
├── setup.py
├── tools：安装、格式检查等工具
└── tox.ini

8. setup.cfg
    - console_script：neutron-server、各种agent、辅助工具的入口点。这些都是需要作为进程单独运行。腳本工具包括：
        -- neutron-db-manager，參考neutron/db/migration/README
        -- neutron-debug，neutron/debug/README
        -- neutron-netns-cleanup
        -- neutron-ovs-cleanup
        -- neutron-sanity-check
    - neutron.core_plugin：所有core plugin的入口点，例如ml2。
    - neutron.service_plugin：

9. Neutron API：openstack使用HTTP REST API作為資源管理的入口，core api对应network/subnet/port，extension api对应其他。具体解释见《1》P249。
