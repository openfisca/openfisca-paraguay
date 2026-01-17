from openfisca_core.model_api import *

from openfisca_paraguay.entities import Persona


class paam_monto(Variable):
    value_type = float
    entity = Persona
    label = "Monto de Pensión Alimentaria para Adultos Mayores"
    definition_period = MONTH

    def formula(persona, period, parameters):
        edad = persona("edad", period)
        min_edad = parameters(
            period
        ).beneficios_sociales.adultos_mayores.pension_alimentaria.edad_minima
        monto = parameters(
            period
        ).beneficios_sociales.adultos_mayores.pension_alimentaria.monto

        # Condition: Age >= 65 and No Pension
        tiene_pension = persona("tiene_jubilacion", period)

        elegible = (edad >= min_edad) & (~tiene_pension)

        return where(elegible, monto, 0)


class tiene_jubilacion(Variable):
    value_type = bool
    entity = Persona
    label = "Indica si tiene jubilación contributiva"
    definition_period = MONTH
