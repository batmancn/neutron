《1》：openstack设计与实现
《2》：doc_summary.md

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
