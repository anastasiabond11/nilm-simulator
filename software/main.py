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

    # 3. Detection and analysis of events
    events = detect_events(data["power"], threshold=150, min_duration=15)

    print("\nDetected appliances:")
    for i, (start, end, change) in enumerate(events, 1):
        start_time = data["time"].iloc[start]
        end_time = data["time"].iloc[end]
        duration = end_time - start_time
        avg_power = data["power"].iloc[start:end].mean()
        energy_kwh = avg_power * duration / 3600

        appliance = identify_appliance(change, duration)

        print(f"\nEvent #{i}: {appliance.upper()}")
        print("-" * 30)
        print(f"  Start time:    {start_time:7.1f}s ({start_time / 60:.1f} min)")
        print(f"  End time:      {end_time:7.1f}s ({end_time / 60:.1f} min)")
        print(f"  Duration:      {duration:7.1f}s ({duration / 60:.1f} min)")
        print(f"  Power delta:   {change:7.1f}W")
        print(f"  Avg power:     {avg_power:7.1f}W")
        print(f"  Energy used:   {energy_kwh:.3f} kWh")

    # 4. Summary statistics
    kettle_events = [e for e in events
                     if identify_appliance(e[2], e[1] - e[0]) == 'kettle']

    print("\nSummary statistics:")
    print("-" * 30)
    print(f"Total kettle activations: {len(kettle_events)}")
    print(f"Total energy used by kettle: {sum(e[2] * (e[1] - e[0]) / 3600 for e in kettle_events):.3f} kWh")
    print(f"Estimated monthly consumption: {len(kettle_events) * 30 * 0.172:.1f} kWh (30 days)")

    # 5. Simulation info
    print("\nSimulation completed successfully!")
    print(f"- Time range: {data['time'].min():.1f}s to {data['time'].max():.1f}s")
    print(f"- Power range: {data['power'].min():.1f}W to {data['power'].max():.1f}W")
    print(f"- Detected {len(events)} power events")
    print("- Plot saved as 'power_plot.png'")