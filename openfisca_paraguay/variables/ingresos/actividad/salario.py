from openfisca_core.model_api import *

from openfisca_paraguay.entities import Persona


class salario_bruto(Variable):
    value_type = float
    entity = Persona
    label = "Salario bruto mensual"
    definition_period = MONTH


class salario_imponible_ips(Variable):
    value_type = float
    entity = Persona
    label = "Salario base para el cálculo de aportes al IPS"
    definition_period = MONTH

    def formula(persona, period, parameters):
        salario = persona("salario_bruto", period)

        # Calculate cap
        salario_minimo = parameters(period).laboral.salario_minimo.mensual
        tope_cantidad = parameters(
            period
        ).seguridad_social.ips.tope_imponible_cantidad_salarios_minimos
        tope_valor = salario_minimo * tope_cantidad

        return min_(salario, tope_valor)
