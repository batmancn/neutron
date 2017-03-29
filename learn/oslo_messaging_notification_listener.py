from oslo.config import cfg
from oslo import messaging
from oslo import log

class NotificationEndpoint(object):
    def warn(self, ctxt, publisher_id, event_type, payload, metadata):
        log.INFO(payload)


class ErrorEndpoint(object):
    def error(self, ctxt, publisher_id, event_type, payload, metadata):
        log.INFO(payload)


transport = messaging.get_transport(cfg.CONF)
target = [
    messaging.Target(topic = 'notifications')
    messaging.Target(topic = 'notifications_bis')
]
endpoints = [
    NotificationEndpoint(),
    ErrorEndpoint()
]
listener = messaging.get_notification_listener(transport,
    target,
    endpoints)
listener.start()
listener.wait()
