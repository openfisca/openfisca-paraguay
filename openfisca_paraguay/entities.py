from openfisca_core.entities import GroupEntity, build_entity

Persona = build_entity(
    key="persona",
    plural="personas",
    label="Persona",
    is_person=True,
)

Familia = GroupEntity(
    key="familia",
    plural="familias",
    label="Familia (Núcleo Familiar)",
    doc="Entidad para beneficios como Tekopora",
    roles=[
        {
            "key": "jefe",
            "plural": "jefes",
            "label": "Jefe de familia",
            "max": 1,
        },
        {
            "key": "miembro",
            "plural": "miembros",
            "label": "Miembro",
        },
    ],
)

Hogar = GroupEntity(
    key="hogar",
    plural="hogares",
    label="Hogar",
    doc="Entidad correspondiente al hogar de la EPHC",
    roles=[
        {
            "key": "jefe",
            "plural": "jefes",
            "label": "Jefe de hogar",
            "max": 1,
        },
        {
            "key": "miembro",
            "plural": "miembros",
            "label": "Miembro",
        },
    ],
)

entities = [Persona, Familia, Hogar]
