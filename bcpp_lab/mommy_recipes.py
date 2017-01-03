from model_mommy.recipe import Recipe

from edc_base_test.utils import get_utcnow
from .models import SubjectRequisition, Aliquot


subjectrequisition = Recipe(
    SubjectRequisition,
    report_datetime=get_utcnow,
)

aliquot = Recipe(
    Aliquot
)
