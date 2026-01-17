from openfisca_core.model_api import *

from openfisca_paraguay.entities import Familia, Persona


class tekopora_monto_total(Variable):
    value_type = float
    entity = Familia
    label = "Monto total de transferencia Tekoporã"
    definition_period = MONTH

    def formula(familia, period, parameters):
        elegible = familia("tekopora_elegible", period)

        monto_base = parameters(period).beneficios_sociales.tekopora.monto_base

        # Sum bonuses
        # Need to iterate over members to calc bonuses
        # Simplified: Calculating per family components
        # Note: OpenFisca usually aggregates from person to family

        bono_salud = familia.members("tekopora_bono_salud_individual", period).sum(
            familia
        )
        bono_educ = familia.members("tekopora_bono_educacion_individual", period).sum(
            familia
        )

        total = monto_base + bono_salud + bono_educ

        tope = parameters(period).beneficios_sociales.tekopora.limite_hogar

        return where(elegible, min_(total, tope), 0)


class tekopora_elegible(Variable):
    value_type = bool
    entity = Familia
    label = "Elegibilidad para Tekoporã"
    definition_period = MONTH

    def formula(familia, period, parameters):
        ingreso_per_capita = familia(
            "ingreso_familiar_per_capita", period
        )  # Placeholder variable
        linea = parameters(period).beneficios_sociales.tekopora.umbral_pobreza_extrema

        es_pobre_extremo = ingreso_per_capita < linea
        # Include logic for demographics (pregnant, disabled, kids, etc)
        # Simplified:
        tiene_menores = familia.members("es_menor", period).any(familia)

        return es_pobre_extremo & tiene_menores


class tekopora_bono_salud_individual(Variable):
    value_type = float
    entity = Persona
    label = "Bono salud individual"
    definition_period = MONTH

    def formula(persona, period, parameters):
        edad = persona("edad", period)
        monto = parameters(period).beneficios_sociales.tekopora.bono_salud
        return where(edad < 6, monto, 0)


class tekopora_bono_educacion_individual(Variable):
    value_type = float
    entity = Persona
    label = "Bono educación individual"
    definition_period = MONTH

    def formula(persona, period, parameters):
        edad = persona("edad", period)
        monto = parameters(period).beneficios_sociales.tekopora.bono_educacion
        return where((edad >= 6) & (edad <= 18), monto, 0)


# Helper vars
class edad(Variable):
    value_type = int
    entity = Persona
    label = "Edad de la persona"
    definition_period = MONTH


class es_menor(Variable):
    value_type = bool
    entity = Persona
    definition_period = MONTH

    def formula(persona, period, parameters):
        return persona("edad", period) < 18


class ingreso_familiar_per_capita(Variable):
    value_type = float
    entity = Familia
    definition_period = MONTH

    def formula(familia, period, parameters):
        ingreso_total = familia.members("salario_bruto", period).sum(
            familia
        )  # Simplified income
        tamano = familia.members("ingreso_dividendos", period).count(
            familia
        )  # Just need count
        # Hack to get size: use any variable count
        tamano = familia.nb_persons(period)
        return ingreso_total / tamano
