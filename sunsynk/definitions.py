"""Sunsynk hybrid inverter sensor definitions."""
from .sensor import Sensor

overall_state = Sensor(59, "Overall state")
day_active_power = Sensor(60, "Day Active Power", "Wh", factor=100)
day_reactive_power = Sensor(61, "Day Reactive Power", "Varh", factor=100)
total_active_power = Sensor(
    63, "Total Active Power", "Wh", factor=100, high_register=64
)
battery_charge_day = Sensor(70, "Battery Charge Day", "Wh", factor=100)
battery_discharge_day = Sensor(71, "Battery discharge day", "Wh", factor=100)
total_battery_charge = Sensor(
    72, "Total Battery Charge", "Wh", factor=100, high_register=73
)
total_battery_discharge = Sensor(
    74, "Total Battery Discharge", "Wh", factor=100, high_register=75
)
grid_import_day = Sensor(76, "Grid Import Day", "Wh", factor=100)
grid_export_day = Sensor(77, "Grid Export Day", "Wh", factor=100)
total_grid_buy = Sensor(78, "Total Grid Buy", "Wh", factor=100, high_register=80)
grid_frequency = Sensor(79, "Grid frequency", "Hz", factor=0.01)
total_grid_import = Sensor(81, "Total Grid Import", "Wh", factor=100, high_register=82)
total_load_power = Sensor(85, "Total Load Power", "Wh", factor=100, high_register=86)
year_load_power = Sensor(85, "Year Load Power", "Wh", factor=100, high_register=86)
temp_dc_transformer = Sensor(90, "Temp DC transformer", "C", factor=0.1)
temp_radiator = Sensor(91, "Temp Radiator", "C", factor=0.1)
temperature_environment = Sensor(95, "Temperature Environment", "C", factor=0.1)
total_pv_power = Sensor(96, "Total PV Power", "Wh", factor=100, high_register=97)
grid_export_year = Sensor(98, "Grid Export Year", "Wh", factor=100, high_register=99)
pv_energy_day = Sensor(108, "PV Energy Day", "Wh", factor=100)
pv1_voltage = Sensor(109, "PV1 Voltage", "V", factor=0.1)
pv1_current = Sensor(110, "PV1 Current", "A", factor=0.1)
pv2_voltage = Sensor(111, "PV2 Voltage", "V", factor=0.1)
pv2_current = Sensor(112, "PV2 Current", "A", factor=0.1)
inverter_voltage = Sensor(154, "Inverter Voltage", "V", factor=0.1)
grid_inverter_load = Sensor(167, "Grid Inverter load", "W", factor=1)
grid_ct_load = Sensor(172, "Grid CT load", "W", factor=1)
total_load = Sensor(178, "Total load", "W", factor=1)
temperature_battery = Sensor(182, "Temperature Battery", "C", factor=0.1)
battery_voltage = Sensor(183, "Battery voltage", "V", factor=0.01)
battery_soc = Sensor(184, "Battery SOC", "%", factor=1)
pv1_power = Sensor(186, "PV1 power", "W", factor=1)
pv2_power = Sensor(187, "PV2 power", "W", factor=1)
battery_output_power = Sensor(190, "Battery output power", "W", factor=1)
battery_output_current = Sensor(191, "Battery output current", "A", factor=0.1)
battery_grid_charge = Sensor(230, "Battery Grid Charge", "A", factor=1)
battery_charge = Sensor(312, "Battery charge", "V", factor=0.01)