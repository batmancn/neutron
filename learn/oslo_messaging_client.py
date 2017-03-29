"""
这里看到，client端使用RPC主要使用topic/namespace/server/version和
方法的名字，对于持有这个方法的类并不关心。

messagin两种用法，RPC是远程调用方法，notification是发生了事件通知listener。
"""

from oslo import messaging

transport = messaging.get_transport(cfg.CONF)
target = messaging.Target(topic = 'test')
client = messaging.RPCClient(transport, target)
ret = client.call(ctxt = {}, method = 'test', arg = 'arg')

# using prepare to change client's some param,
# here add namespace and version
cctxt = client.prepare(namespace='control', version = '2.0')
cctxt.cast({}, 'stop')
