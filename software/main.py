import numpy as np
import matplotlib.pyplot as plt
from data_generator import generate_power_data  # Этот файл создадим следующим

if __name__ == "__main__":
    data = generate_power_data()
    plt.plot(data["time"], data["power"])
    plt.title("NILM Simulator")
    plt.xlabel("Time (s)")
    plt.ylabel("Power (W)")
    plt.savefig("power_plot.png")
    print("Plot is saved in power_plot.png")