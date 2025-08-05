APPLIANCES = {
    "kettle": {
        "power": 2000,
        "duration": 300,
        "pattern": "rectangular",
        "color": "#FF5733"
    },
    "fridge": {
        "power_range": (40, 60),
        "cycle": 1800,
        "pattern": "sinusoidal",
        "color": "#33FF57"
    },
    "microwave": {
        "power": 800,
        "duration_range": (60, 300),
        "pattern": "intermittent",
        "color": "#3357FF"
    },
    "washing_machine": {
        "power_phases": [
            {"power": 500, "duration": 900},   # Washing phase
            {"power": 2000, "duration": 600},  # Heating phase
            {"power": 100, "duration": 300}    # Spinning phase
        ],
        "color": "#F833FF"
    }
}

def identify_appliance(power_change, duration_samples):
    """Improved appliance identification with better thresholds"""
    duration_seconds = duration_samples / 10

    if 1900 <= power_change <= 2100 and 200 <= duration_seconds <= 400:
        return "kettle"
    elif 700 <= power_change <= 900 and 50 <= duration_seconds <= 350:
        return "microwave"
    elif 100 <= power_change <= 200 and 500 <= duration_seconds <= 1500:
        return "fridge"
    return "unknown"