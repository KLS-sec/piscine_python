def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()

    if (unit == "packets"):
        unit = "packets available"
    elif (unit == "grams"):
        unit = "grams total"
    elif (unit == "area"):
        unit = "square meters"
    else:
        print("Unknown unit type")
    print(seed_type, "seeds:", quantity, unit)
