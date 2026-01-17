from openfisca_core.model_api import *

from openfisca_paraguay.entities import Persona


class ips_aporte_empleado(Variable):
    value_type = float
    entity = Persona
    label = "Aporte del empleado al IPS"
    definition_period = MONTH

    def formula(persona, period, parameters):
        base = persona("salario_imponible_ips", period)
        tasa = parameters(period).seguridad_social.ips.tasa_empleado_general
        return base * tasa


class ips_aporte_empleador(Variable):
    value_type = float
    entity = Persona
    label = "Aporte del empleador al IPS"
    definition_period = MONTH

    def formula(persona, period, parameters):
        base = persona("salario_imponible_ips", period)
        tasa = parameters(period).seguridad_social.ips.tasa_empleador_general
        return base * tasa
