import math

def joules_to_carbon_emissions(heat_energy_joules, emissions_factor_joules_per_kg):
    carbon_emissions_kg = heat_energy_joules / emissions_factor_joules_per_kg
    return carbon_emissions_kg

# Example usage:
heat_energy = 1e9  # 1 gigajoule (1,000,000,000 joules) of heat energy
emissions_factor = 2.5e7  # Example emissions factor (joules per kilogram of carbon)

carbon_emissions = joules_to_carbon_emissions(heat_energy, emissions_factor)
print(f"Carbon Emissions: {carbon_emissions} kilograms")
