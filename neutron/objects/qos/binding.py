# Copyright 2017 Intel Corporation.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_log import log
from neutron_lib.objects import common_types

from neutron.db.qos import models as qos_db_model
from neutron.objects import base
from neutron.common import log_utils

LOG = log.getLogger(__name__)

@base.NeutronObjectRegistry.register
class QosPolicyPortBinding(base.NeutronDbObject):
    LOG.info('%s(): caller(): %s', log_utils.get_fname(1), log_utils.get_fname(2))
    # Version 1.0: Initial version
    VERSION = '1.0'

    db_model = qos_db_model.QosPortPolicyBinding

    fields = {
        'policy_id': common_types.UUIDField(),
        'port_id': common_types.UUIDField()
    }

    primary_keys = ['port_id']
    fields_no_update = ['policy_id', 'port_id']


@base.NeutronObjectRegistry.register
class QosPolicyNetworkBinding(base.NeutronDbObject):
    LOG.info('%s(): caller(): %s', log_utils.get_fname(1), log_utils.get_fname(2))
    # Version 1.0: Initial version
    VERSION = '1.0'

    db_model = qos_db_model.QosNetworkPolicyBinding

    fields = {
        'policy_id': common_types.UUIDField(),
        'network_id': common_types.UUIDField()
    }

    primary_keys = ['network_id']
    fields_no_update = ['policy_id', 'network_id']


@base.NeutronObjectRegistry.register
class QosPolicyFloatingIPBinding(base.NeutronDbObject):
    LOG.info('%s(): caller(): %s', log_utils.get_fname(1), log_utils.get_fname(2))
    # Version 1.0: Initial version
    VERSION = '1.0'

    db_model = qos_db_model.QosFIPPolicyBinding

    fields = {
        'policy_id': common_types.UUIDField(),
        'fip_id': common_types.UUIDField()
    }

    primary_keys = ['policy_id', 'fip_id']
    fields_no_update = ['policy_id', 'fip_id']


@base.NeutronObjectRegistry.register
class QosPolicyRouterGatewayIPBinding(base.NeutronDbObject):
    LOG.info('%s(): caller(): %s', log_utils.get_fname(1), log_utils.get_fname(2))
    # Version 1.0: Initial version
    VERSION = '1.0'

    db_model = qos_db_model.QosRouterGatewayIPPolicyBinding

    fields = {
        'policy_id': common_types.UUIDField(),
        'router_id': common_types.UUIDField()
    }

    primary_keys = ['policy_id', 'router_id']
    fields_no_update = ['policy_id', 'router_id']
