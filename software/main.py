import numpy as np
from data_generator import generate_power_data
from software.appliance_db import identify_appliance
from software.event_detector import detect_events
from software.visualization import plot_power_data

if __name__ == "__main__":
    # 1. Data generation with custom parameters
    print("1. Starting data generation...")
    data = generate_power_data(duration=600, sample_rate=10)

    # Save raw data to CSV
    print("2. Data generated, saving to CSV...")
    data.to_csv("power_data.csv", index=False)
    print("Data successfully saved to power_data.csv")

    # 2. Event detection with optimized thresholds
    print("3. Detecting events...")
    detected_events = detect_events(
        power_series=data["power"],
        threshold=150,
        min_duration=15
    )
    print(f"Detected {len(detected_events)} events")

    # 3. Visualization with event highlighting
    plot_power_data(
        df=data,
        detected_events=detected_events,
        filename="power_plot.png"
    )

    # 4. Detailed event analysis
    print("\nDetected appliances:")
    for i, (start_idx, end_idx, power_change) in enumerate(detected_events, 1):
        start_time = data["time"].iloc[start_idx]
        end_time = data["time"].iloc[end_idx]
        duration_samples = end_idx - start_idx
        duration_seconds = duration_samples / 10  # Convert samples to seconds
        appliance = identify_appliance(power_change, duration_samples)
        avg_power = data["power"].iloc[start_idx:end_idx].mean()
        energy_used = avg_power * duration_seconds / 3600  # Convert to kWh

        print(f"\nEvent #{i}: {appliance.upper()}")
        print("-" * 40)
        print(f"  Time window:    {start_time:7.1f}s → {end_time:7.1f}s")
        print(f"  Duration:       {duration_seconds:7.1f}s ({duration_seconds / 60:.1f} min)")
        print(f"  Power change:   {power_change:7.1f}W")
        print(f"  Average power:  {avg_power:7.1f}W")
        print(f"  Energy used:    {energy_used:.3f} kWh")

    # 5. Aggregate statistics
    appliance_stats = {
        'kettle': [],
        'microwave': [],
        'fridge': []
    }

    for start_idx, end_idx, power_change in detected_events:
        duration_samples = end_idx - start_idx
        duration_seconds = duration_samples / 10
        avg_power = data["power"].iloc[start_idx:end_idx].mean()
        energy_used = avg_power * duration_seconds / 3600  # kWh
        appliance = identify_appliance(power_change, duration_samples)

        if appliance in appliance_stats:
            appliance_stats[appliance].append(energy_used)

    print("\nSummary Statistics:")
    print("-" * 40)
    print(f"Total events detected:    {len(detected_events)}")
    for appliance, stats in appliance_stats.items():
        print(f"{appliance.capitalize()} activations:   {len(stats):>5}")
        print(f"Total {appliance} energy:    {sum(stats):.3f} kWh")

    total_energy = sum(sum(stats) for stats in appliance_stats.values())
    print(f"\nEstimated monthly usage:  {total_energy * 30:.1f} kWh")

    # 6. Simulation metadata
    print("\nSimulation Parameters:")
    print("-" * 40)
    print(f"Time range:       {data['time'].min():.1f}s → {data['time'].max():.1f}s")
    print(f"Power range:      {data['power'].min():.1f}W → {data['power'].max():.1f}W")
    print(f"Sampling rate:    {10} Hz")
    print("\nSimulation completed successfully!")