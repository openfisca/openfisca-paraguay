from openfisca_core.model_api import *

from openfisca_paraguay.entities import Persona


class ingreso_laboral_independiente(Variable):
    value_type = float
    entity = Persona
    label = "Ingreso mensual por trabajo independiente (Servicios Personales)"
    definition_period = MONTH
