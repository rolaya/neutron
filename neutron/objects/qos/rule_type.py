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
from neutron_lib.plugins import constants
from neutron_lib.plugins import directory
from neutron_lib.services.qos import constants as qos_consts
from oslo_utils import versionutils
from oslo_versionedobjects import exception
from oslo_versionedobjects import fields as obj_fields

from neutron.objects import base
from neutron.common import log_utils

LOG = log.getLogger(__name__)


class RuleTypeField(obj_fields.BaseEnumField):
    LOG.info('%s(): caller(): %s', log_utils.get_fname(1), log_utils.get_fname(2))

    def __init__(self, **kwargs):
        LOG.info('%s(): caller(): %s', log_utils.get_fname(1), log_utils.get_fname(2))
        self.AUTO_TYPE = obj_fields.Enum(
            valid_values=qos_consts.VALID_RULE_TYPES)
        super(RuleTypeField, self).__init__(**kwargs)


@base.NeutronObjectRegistry.register
class QosRuleType(base.NeutronObject):
    LOG.info('%s(): caller(): %s', log_utils.get_fname(1), log_utils.get_fname(2))
    # Version 1.0: Initial version
    # Version 1.1: Added QosDscpMarkingRule
    # Version 1.2: Added QosMinimumBandwidthRule
    # Version 1.3: Added drivers field
    VERSION = '1.3'

    fields = {
        'type': RuleTypeField(),
        'drivers': obj_fields.ListOfObjectsField(
            'QosRuleTypeDriver', nullable=True)
    }

    synthetic_fields = ['drivers']

    # we don't receive context because we don't need db access at all
    @classmethod
    def get_object(cls, rule_type_name, **kwargs):
        LOG.info('%s(): caller(): %s', log_utils.get_fname(1), log_utils.get_fname(2))
        plugin = directory.get_plugin(alias=constants.QOS)
        drivers = plugin.supported_rule_type_details(rule_type_name)
        drivers_obj = [QosRuleTypeDriver(
            name=driver['name'],
            supported_parameters=driver['supported_parameters'])
            for driver in drivers]

        return cls(type=rule_type_name, drivers=drivers_obj)

    # we don't receive context because we don't need db access at all
    @classmethod
    def get_objects(cls, validate_filters=True, **kwargs):
        LOG.info('%s(): caller(): %s', log_utils.get_fname(1), log_utils.get_fname(2))
        if validate_filters:
            cls.validate_filters(**kwargs)

        rule_types = (
            directory.get_plugin(alias=constants.QOS).supported_rule_types)

        # TODO(ihrachys): apply filters to returned result
        return [cls(type=type_) for type_ in rule_types]

    # we don't receive context because we don't need db access at all
    @classmethod
    def get_values(cls, field, **kwargs):
        LOG.info('%s(): caller(): %s', log_utils.get_fname(1), log_utils.get_fname(2))
        return [getattr(obj, field) for obj in cls.get_objects(**kwargs)]

    def obj_make_compatible(self, primitive, target_version):
        LOG.info('%s(): caller(): %s', log_utils.get_fname(1), log_utils.get_fname(2))
        _target_version = versionutils.convert_version_to_tuple(target_version)
        if _target_version < (1, 3):
            raise exception.IncompatibleObjectVersion(
                objver=target_version, objtype=self.__class__.__name__)


@base.NeutronObjectRegistry.register
class QosRuleTypeDriver(base.NeutronObject):
    LOG.info('%s(): caller(): %s', log_utils.get_fname(1), log_utils.get_fname(2))
    # Version 1.0: Initial version
    VERSION = '1.0'

    fields = {
        'name': obj_fields.StringField(),
        'supported_parameters': common_types.ListOfDictOfMiscValuesField()
    }

    def to_dict(self):
        LOG.info('%s(): caller(): %s', log_utils.get_fname(1), log_utils.get_fname(2))
        return {
            'name': self.name,
            'supported_parameters': self.supported_parameters}

    @classmethod
    def get_objects(cls, context, **kwargs):
        raise NotImplementedError()
