import numpy as np
import matplotlib.pyplot as plt
from data_generator import generate_power_data
from visualization import plot_power_data

if __name__ == "__main__":
    # 1. Generation of data with custom parameters
    data = generate_power_data(
        duration=7200,
        sample_rate=10
    )

    # 2. visualization via a separate module
    plot_power_data(
        df=data,
        filename="power_plot.png",
    )

    print("\nSimulation completed successfully!")
    print(f"- Time range: {data['time'].min():.1f}s to {data['time'].max():.1f}s")
    print(f"- Power range: {data['power'].min():.1f}W to {data['power'].max():.1f}W")
    print("- Plot saved as 'advanced_power_plot.png'")