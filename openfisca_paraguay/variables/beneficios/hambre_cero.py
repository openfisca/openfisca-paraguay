from openfisca_core.model_api import *

from openfisca_paraguay.entities import Persona


class hambre_cero_valor_mensual(Variable):
    value_type = float
    entity = Persona
    label = "Valor monetario mensual del beneficio de alimentación escolar"
    definition_period = MONTH

    def formula(persona, period, parameters):
        edad = persona("edad", period)
        valor_diario = parameters(
            period
        ).beneficios_sociales.escolar.hambre_cero.valor_diario

        # Assumption: 20 school days
        dias_escolares = 20

        es_estudiante = (edad >= 5) & (edad <= 18)  # Simplified school age

        return where(es_estudiante, valor_diario * dias_escolares, 0)
