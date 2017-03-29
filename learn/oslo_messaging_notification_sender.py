from oslo.config import cfg
from oslo import messaging
from oslo import log

transport = messaging.get_transport(cfg.CONF)
notifier = messaging.Notifier(transport, driver = 'messaging',
    topic = 'notifications')
notifier_compute = notifier.prepare(publisher_id = 'compute')
notifier_compute.error(ctxt = {}, event_type = 'my_type',
    payload = {'content': 'error occured'})
