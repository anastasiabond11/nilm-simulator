import matplotlib.pyplot as plt


def plot_power_data(df, filename="power_plot.png"):
    plt.figure(figsize=(12, 6))

    # General plot
    plt.plot(df["time"], df["power"], label="Total Power", color='blue', linewidth=1)

    # Settings
    plt.title("NILM Simulator: Power Consumption", pad=20)
    plt.xlabel("Time (seconds)", labelpad=10)
    plt.ylabel("Power (W)", labelpad=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # Saving
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()
