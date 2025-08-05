import numpy as np


def detect_events(power_series, threshold=100, min_duration=10):
    """
        Detection of power surges.

        Parameters:
            power_series: pd.Series with power data
            threshold: minimum surge for detection (W)
            min_duration: minimum event duration (samples)

        Returns:
        list of tuples: (start_index, end_index, power_change)
    """
    events = []
    in_event = False
    for i in range(1, len(power_series)):
        delta = power_series.iloc[i] - power_series.iloc[i - 1]

        if not in_event and abs(delta) > threshold:
            start = i
            prev_power = power_series.iloc[i - 1]
            in_event = True
        elif in_event and abs(power_series.iloc[i] - prev_power) < threshold / 2:
            if i - start >= min_duration:
                power_change = power_series.iloc[start:i].mean() - prev_power
                events.append((start, i, power_change))
            in_event = False

    return events