def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit == "packets"):
        unit = "packets available"
    if (unit == "grams"):
        unit = "grams total"
    if (unit == "area"):
        unit = "square meters"
    print(seed_type, "seeds:", quantity, unit)
