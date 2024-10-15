from estate.models.enums import TypeFlat, TypeHouse


type_flat_dict = dict.fromkeys([t.name for t in TypeFlat], None)
type_house_dict = dict.fromkeys([t.name for t in TypeHouse], None)