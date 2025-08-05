import pandas as pd
import numpy as np
from scipy.signal import find_peaks

def detect_events(power_series, threshold=150, min_duration=10, merge_window=20):
    """
    Optimized event detection with:
    - Vectorized operations
    - Efficient memory usage
    - Progress tracking

    Parameters:
        power_series: pd.Series with power data
        threshold: minimum power change (W)
        min_duration: minimum event duration (samples)
        stability_samples: samples to confirm stabilization

    Returns:
        list of tuples: (start_index, end_index, power_change)
    """
    power_values = power_series.values
    n = len(power_values)

    diffs = np.diff(power_values)
    rising_edges = np.where(diffs > threshold)[0]
    falling_edges = np.where(diffs < -threshold)[0]

    events = []
    current_start = None

    for i in range(n):
        if current_start is None and i in rising_edges:
            current_start = i
        elif current_start is not None and i in falling_edges:
            if i - current_start >= min_duration:
                events.append((current_start, i))
            current_start = None

    if not events:
        return []

    merged = [events[0]]
    for start, end in events[1:]:
        last_start, last_end = merged[-1]
        if start - last_end < merge_window:
            merged[-1] = (last_start, end)
        else:
            merged.append((start, end))

    result = []
    for start, end in merged:
        baseline = np.median(power_values[max(0, start - 50):start])
        avg_power = np.mean(power_values[start:end])
        power_change = avg_power - baseline
        result.append((start, end, power_change))


    print(f"Detected {len(result)} valid events after processing")
    return result