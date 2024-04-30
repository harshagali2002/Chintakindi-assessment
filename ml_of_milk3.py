def convert_liters_to_milliliters(liters):
    milliliters = liters * 1000
    return milliliters

liters = 2.5678

milliliters = convert_liters_to_milliliters(liters)

print(f"The amount of milk in {liters} liters is {milliliters} milliliters.")