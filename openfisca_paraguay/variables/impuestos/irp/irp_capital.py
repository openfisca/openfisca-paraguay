from openfisca_core.model_api import *

from openfisca_paraguay.entities import Persona


class irp_capital_ingreso_gravado(Variable):
    value_type = float
    entity = Persona
    label = "Ingreso gravado por IRP-RGC"
    definition_period = YEAR

    def formula(persona, period, parameters):
        divid = persona("ingreso_dividendos", period)
        alq = persona("ingreso_alquileres", period)
        intereses = persona("ingreso_intereses", period)
        # Note: Some interests are exempt, but assuming taxable for now
        return divid + alq + intereses


class irp_capital_base_imponible(Variable):
    value_type = float
    entity = Persona
    label = "Base Imponible IRP-RGC (Simplificado)"
    definition_period = YEAR

    def formula(persona, period, parameters):
        ingreso = persona("irp_capital_ingreso_gravado", period)
        return ingreso


class irp_capital_monto(Variable):
    value_type = float
    entity = Persona
    label = "Monto del Impuesto a la Renta Personal - Capital"
    definition_period = YEAR

    def formula(persona, period, parameters):
        base = persona("irp_capital_base_imponible", period)
        tasa = parameters(period).impuestos.irp.rentas_capital.tasa
        return base * tasa
