from openfisca_core.model_api import *

from openfisca_paraguay.entities import Persona


class iva_consumo_estimado(Variable):
    value_type = float
    entity = Persona
    label = "Monto estimado de pago de IVA"
    definition_period = YEAR

    # def formula(persona, period, parameters):
    #     return 0
