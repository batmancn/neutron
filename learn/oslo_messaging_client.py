from oslo import messaging

transport = messaging.get_transport(cfg.CONF)
target = messaging.Target('test')
client = messaging.RPCClient(transport, target)
ret = client.call(ctxt = {}, method = 'test', arg = 'arg')

cctxt = client.prepare(namespace='control', version = '2.0')
cctxt.cast({}, 'stop')
