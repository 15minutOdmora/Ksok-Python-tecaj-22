"""
Module for converting different types of data.
"""


def dollars_to_euro(dollar_value: str):
    # $1 = 0.95€
    value = int(dollar_value[1:])
    euro_value = value * 0.95
    return f"{round(euro_value)}€"


def lbs_to_kg(lbs_value: str):
    # 1lbs = 0.45359237kg
    value = lbs_value[:-3]
    kg = round(int(value) * 0.45359237)
    return f"{kg}kg"


def imperial_to_metric(imperial_value: str):
    # 1' = 0.3048m
    # 1" = 0.0254m
    feet, inches = imperial_value.split("\'")
    feet, inches = int(feet), int(inches[:-1])
    meters = round(feet * 0.3048 + inches * 0.0254, 2)
    return f"{meters}m"


if __name__ == "__main__":
    # Tests
    print(dollars_to_euro("$456231"))
    print(lbs_to_kg("100lbs"))
    print(imperial_to_metric('6\'10'))