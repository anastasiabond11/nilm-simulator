import numpy as np
import matplotlib.pyplot as plt
from data_generator import generate_power_data
from software.appliance_db import identify_appliance
from software.event_detector import detect_events
from visualization import plot_power_data

if __name__ == "__main__":
    # 1. Generation of data with custom parameters
    data = generate_power_data(
        duration=7200,
        sample_rate=10
    )

    # 2. Visualization via a separate module
    plot_power_data(
        df=data,
        filename="power_plot.png",
    )

    # 3. Detection of events
    events = detect_events(data["power"], threshold=150, min_duration=15)

    print("\nDetected appliances:")
    for start, end, change in events:
        start_time = data["time"].iloc[start]
        end_time = data["time"].iloc[end]
        duration = end_time - start_time

        # Identifying the device
        appliance = identify_appliance(change, duration)

        print(f"- {appliance.upper()}:")
        print(f"  Time: {start_time:.1f}s to {end_time:.1f}s")
        print(f"  Duration: {duration:.1f}s")
        print(f"  Power change: {change:.1f}W")
        print(f"  Avg power: {data['power'].iloc[start:end].mean():.1f}W")

    # 4. Simulation info
    print("\nSimulation completed successfully!")
    print(f"- Time range: {data['time'].min():.1f}s to {data['time'].max():.1f}s")
    print(f"- Power range: {data['power'].min():.1f}W to {data['power'].max():.1f}W")
    print(f"- Detected {len(events)} power events")
    print("- Plot saved as 'power_plot.png'")