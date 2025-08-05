import pandas as pd  # Добавьте эту строку в начало файла
import numpy as np
from random import randint, uniform, choice


def generate_power_data(duration=600, sample_rate=10):
    """Power data generation"""
    time = np.arange(0, duration, 1 / sample_rate)

    # Базовая нагрузка (холодильник + шум)
    base_power = 50 + 5 * np.sin(2 * np.pi * time / 1800)
    base_power += np.random.normal(0, 2, len(time))

    # Четко определенные события приборов
    appliance_power = np.zeros_like(time)

    # Чайник (2000W, 300s)
    kettle_start = 201
    appliance_power[(time >= kettle_start) & (time < kettle_start+300)] = 2000

    # Микроволновка (800W, 120s)
    microwave_start = 300
    appliance_power[(time >= microwave_start) & (time < microwave_start+180)] = 800

    # Случайные скачки (не более 50W)
    spikes = np.random.uniform(0, 50, len(time)) * (np.random.random(len(time)) > 0.99)

    return pd.DataFrame({
        "time": time,
        "power": np.clip(base_power + appliance_power + spikes, 0, 3000)
    })