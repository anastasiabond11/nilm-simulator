import numpy as np
import pandas as pd


def generate_power_data(duration=3600, sample_rate=10):
    """Generation of synthetic energy consumption data"""
    time = np.arange(0, duration, 1 / sample_rate)

    # Basic consumption (refrigerator + background)
    base_power = 50 + 10 * np.sin(2 * np.pi * time / 1800)

    # Turning on the kettle (2000W for 5 minutes)
    kettle = np.zeros_like(time)
    for start in range(300, duration, 1800):
        end = start + 300
        mask = (time >= start) & (time < end)
        kettle[mask] = 2000

    return pd.DataFrame({
        "time": time,
        "power": base_power + kettle
    })