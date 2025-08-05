APPLIANCES = {
    "kettle": {
        "power": 2000,
        "duration": 300,
        "pattern": "rectangular"
    },
    "fridge": {
        "power_range": (40, 60),
        "cycle": 1800,
        "pattern": "sinusoidal"
    }
}

def identify_appliance(power_change, duration):
    for name, params in APPLIANCES.items():
        if "power" in params:
            if abs(power_change - params["power"]) < 50:
                return name
        elif "power_range" in params:
            if params["power_range"][0] <= power_change <= params["power_range"][1]:
                return name
    return "unknown"