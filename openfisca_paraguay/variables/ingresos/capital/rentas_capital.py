from openfisca_core.model_api import *

from openfisca_paraguay.entities import Persona


class ingreso_dividendos(Variable):
    value_type = float
    entity = Persona
    label = "Ingresos por dividendos y utilidades"
    definition_period = MONTH


class ingreso_alquileres(Variable):
    value_type = float
    entity = Persona
    label = "Ingresos por alquiler de inmuebles"
    definition_period = MONTH


class ingreso_intereses(Variable):
    value_type = float
    entity = Persona
    label = "Ingresos por intereses o rendimientos financieros"
    definition_period = MONTH
