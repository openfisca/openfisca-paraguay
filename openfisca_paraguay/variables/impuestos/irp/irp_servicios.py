from openfisca_core.model_api import *

from openfisca_paraguay.entities import Persona


class irp_servicios_ingreso_bruto_anual(Variable):
    value_type = float
    entity = Persona
    label = "Ingreso Bruto Anual gravado por IRP-RSP"
    definition_period = YEAR

    def formula(persona, period, parameters):
        # Sum of salary and independent income
        salario = persona("salario_bruto", period)
        independiente = persona("ingreso_laboral_independiente", period)
        return salario + independiente


class irp_servicios_gastos_deducibles(Variable):
    value_type = float
    entity = Persona
    label = "Gastos deducibles para IRP-RSP"
    definition_period = YEAR

    def formula(persona, period, parameters):
        ips = persona("ips_aporte_empleado", period)
        otros_gastos = persona("irp_servicios_otros_gastos_deducibles", period)
        return ips + otros_gastos


class irp_servicios_otros_gastos_deducibles(Variable):
    value_type = float
    entity = Persona
    label = "Otros gastos deducibles documentados (Salud, educación, etc.)"
    definition_period = YEAR


class irp_servicios_base_imponible(Variable):
    value_type = float
    entity = Persona
    label = "Renta Neta Imponible IRP-RSP"
    definition_period = YEAR

    def formula(persona, period, parameters):
        ingreso = persona("irp_servicios_ingreso_bruto_anual", period)
        gastos = persona("irp_servicios_gastos_deducibles", period)
        mna = parameters(period).impuestos.irp.rentas_servicios.mna

        # Check if threshold is met
        # Usually checking threshold is for BECOMING a taxpayer, but here we calculate tax if liable
        # Simplified: if income > MNA, then tax is calculated on Net Income (Income - Expenses)
        # Note: The legislation says "Taxpayers who exceed... will settle tax on total gross income minus deductible expenses"

        es_contribuyente = ingreso > mna

        renta_neta = max_(0, ingreso - gastos)
        return where(es_contribuyente, renta_neta, 0)


class irp_servicios_monto(Variable):
    value_type = float
    entity = Persona
    label = "Monto del Impuesto a la Renta Personal - Servicios"
    definition_period = YEAR

    def formula(persona, period, parameters):
        base = persona("irp_servicios_base_imponible", period)
        bareme = parameters(period).impuestos.irp.rentas_servicios.bareme

        return bareme.calc(base)
