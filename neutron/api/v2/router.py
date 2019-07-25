# Copyright (c) 2012 OpenStack Foundation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# 使用的库：
from oslo_config import cfg # oslo_config，用于配置文件解析
from oslo_service import wsgi as base_wsgi # oslo_service.swgi，用于wsgi，一个python http框架
import routes as routes_mapper # python routes库，python的redis routes系统，https://routes.readthedocs.io/en/latest/
import six # url字符串解析用的
import six.moves.urllib.parse as urlparse
import webob # python的WSGI对象解析库，https://webob.org/
import webob.dec
import webob.exc

from neutron.api import extensions # neutron.api的一些common库
from neutron.api.v2 import attributes
from neutron.api.v2 import base
from neutron import manager # ？？？
from neutron import policy # ？？？
from neutron.quota import resource_registry # ？？？
from neutron import wsgi # ？？？

# 下面这一段RESOURCES等定义，是openstack的common的定义资源的方式
# 使用了resource_registry库？？？
# RESOURCES定义了router支持的API，也就是network
# 具体restapi的构造在APIRouter.__init__方法中，通过其中的_map做的，具体参考那里的注释
RESOURCES = {'network': 'networks',
             'subnet': 'subnets',
             'subnetpool': 'subnetpools',
             'port': 'ports'}
SUB_RESOURCES = {}
COLLECTION_ACTIONS = ['index', 'create']
MEMBER_ACTIONS = ['show', 'update', 'delete']
REQUIREMENTS = {'id': attributes.UUID_PATTERN, 'format': 'json'}


class Index(wsgi.Application):
    def __init__(self, resources):
        self.resources = resources

    @webob.dec.wsgify(RequestClass=wsgi.Request)
    def __call__(self, req):
        metadata = {}

        layout = []
        for name, collection in six.iteritems(self.resources):
            href = urlparse.urljoin(req.path_url, collection)
            resource = {'name': name,
                        'collection': collection,
                        'links': [{'rel': 'self',
                                   'href': href}]}
            layout.append(resource)
        response = dict(resources=layout)
        content_type = req.best_match_content_type()
        body = wsgi.Serializer(metadata=metadata).serialize(response,
                                                            content_type)
        return webob.Response(body=body, content_type=content_type)


class APIRouter(base_wsgi.Router):

    @classmethod
    def factory(cls, global_config, **local_config):
        return cls(**local_config)

    def __init__(self, **local_config):
        # get URL mapping facilities, how to use refer to
        # https://routes.readthedocs.io/en/latest/
        #
        # 这里比较重要的一个工作就是构造restapi

        # routes_mapper可以制作
        mapper = routes_mapper.Mapper()
        plugin = manager.NeutronManager.get_plugin() # get plugins
        ext_mgr = extensions.PluginAwareExtensionManager.get_instance()
        ext_mgr.extend_resources("2.0", attributes.RESOURCE_ATTRIBUTE_MAP)

        col_kwargs = dict(collection_actions=COLLECTION_ACTIONS,
                          member_actions=MEMBER_ACTIONS)

        def _map_resource(collection, resource, params, parent=None):
            allow_bulk = cfg.CONF.allow_bulk
            allow_pagination = cfg.CONF.allow_pagination
            allow_sorting = cfg.CONF.allow_sorting
            controller = base.create_resource(
                collection, resource, plugin, params, allow_bulk=allow_bulk,
                parent=parent, allow_pagination=allow_pagination,
                allow_sorting=allow_sorting)
            path_prefix = None
            if parent:
                path_prefix = "/%s/{%s_id}/%s" % (parent['collection_name'],
                                                  parent['member_name'],
                                                  collection)
            mapper_kwargs = dict(controller=controller,
                                 requirements=REQUIREMENTS,
                                 path_prefix=path_prefix,
                                 **col_kwargs)
            return mapper.collection(collection, resource,
                                     **mapper_kwargs)

        mapper.connect('index', '/', controller=Index(RESOURCES))
        # this is to mapping URLs to 'NETWORK' etc resource in
        # attribute.py RESOURCE_ATTRIBUTE_MAP.
        #
        # So if you want to extend URL-resource mapping, change
        # in attribute.py RESOURCE_ATTRIBUTE_MAP.
        for resource in RESOURCES:
            _map_resource(RESOURCES[resource], resource,
                          attributes.RESOURCE_ATTRIBUTE_MAP.get(
                              RESOURCES[resource], dict()))
            resource_registry.register_resource_by_name(resource)

        for resource in SUB_RESOURCES:
            _map_resource(SUB_RESOURCES[resource]['collection_name'], resource,
                          attributes.RESOURCE_ATTRIBUTE_MAP.get(
                              SUB_RESOURCES[resource]['collection_name'],
                              dict()),
                          SUB_RESOURCES[resource]['parent'])

        # Certain policy checks require that the extensions are loaded
        # and the RESOURCE_ATTRIBUTE_MAP populated before they can be
        # properly initialized. This can only be claimed with certainty
        # once this point in the code has been reached. In the event
        # that the policies have been initialized before this point,
        # calling reset will cause the next policy check to
        # re-initialize with all of the required data in place.
        policy.reset()
        super(APIRouter, self).__init__(mapper)
