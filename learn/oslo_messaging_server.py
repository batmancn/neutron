from oslo import messaging

class ServerControlEndpoint(object):
    target = messaging.Target(namespace = 'control', version = '2.0')

    def __init__(self, server):
        self.server = server

    def stop(self, ctx):
        if (self.server):
            self.server.stop()


class TestEndpoint(object):
    def test(self, ctx, arg):
        return arg


tarnsport = messaging.get_transport(cfg.CONF)
target = messaging.Target(topic = 'test', server = 'server1')

endpoints = [
    ServerControlEndpoint(None),
    TestEndpoint(),
]

server = messaging.get_rpc_server(transport, target, endpoints, excutor = 'blocking')

server.start()
server.wait()
