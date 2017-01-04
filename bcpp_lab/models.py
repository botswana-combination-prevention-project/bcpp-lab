from edc_base.model.models import BaseUuidModel
from edc_lab.model_mixins import AliquotModelMixin

from edc_base.model.models import HistoricalRecords
from edc_lab.managers import AliquotManager


class Aliquot(AliquotModelMixin, BaseUuidModel):

    objects = AliquotManager()

    history = HistoricalRecords

    class Meta:
        app_label = 'bcpp_lab'
