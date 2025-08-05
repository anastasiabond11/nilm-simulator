import pandas as pd
import matplotlib.pyplot as plt
from software.appliance_db import identify_appliance, APPLIANCES


def plot_power_data(df, detected_events=None, filename="power_plot.png"):
    plt.figure(figsize=(14, 7))

    # Main power plot
    plt.plot(df["time"], df["power"], label="Total Power",
             color='black', linewidth=1, alpha=0.7)

    if detected_events:
        handled_appliances = set()

        for start, end, change in detected_events:
            appliance = identify_appliance(change, end - start)
            color = APPLIANCES.get(appliance, {}).get("color", "#CCCCCC")

            label = f'{appliance} event' if appliance not in handled_appliances else None
            if label:
                handled_appliances.add(appliance)

            plt.axvspan(df["time"].iloc[start], df["time"].iloc[end],
                        color=color, alpha=0.3, label=label)

    for start, end, change in detected_events:
        if change > 500:
            appliance = identify_appliance(change, end - start)
            mid_time = (df["time"].iloc[start] + df["time"].iloc[end]) / 2
            plt.annotate(appliance,
                         (mid_time, df["power"].iloc[start] + 100),
                         ha='center', va='bottom', fontsize=9)

    plt.title("NILM Simulator: Power Consumption Analysis", pad=20, fontsize=14)
    plt.xlabel("Time (seconds)", fontsize=12)
    plt.ylabel("Power (W)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(loc='upper right')

    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()