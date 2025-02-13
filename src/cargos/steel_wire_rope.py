from cargo import Cargo

cargo = Cargo(
    id="steel_wire_rope",
    type_name="string(STR_CARGO_NAME_STEEL_WIRE_ROPE)",
    unit_name="string(STR_CARGO_NAME_STEEL_WIRE_ROPE)",
    type_abbreviation="string(STR_CID_STEEL_WIRE_ROPE)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="SWRP",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_STEEL_WIRE_ROPE)",
    penalty_lowerbound="30",
    single_penalty_length="42",
    price_factor=160,
    capacity_multiplier="1",
    icon_indices=(6, 6),
    sprites_complete=True,
)
