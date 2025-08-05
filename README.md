# 🏠 NILM Energy Monitor Simulator  
**Non-intrusive load monitoring system**  

This project is a **NILM (Non-Intrusive Load Monitoring)** simulator - a technology that analyzes total household power consumption and identifies which electrical appliances are active **without individual sensors** on each device.  

## **🔧 Technical Foundation**  
- **Python** + **NumPy/Pandas** - data generation and processing  
- **Matplotlib** - power consumption visualization  
- **Detection algorithms** - voltage spike analysis for appliance identification  

## **📊 Key Features**  
1. Generates **synthetic power consumption data** (simulating real smart meter data)  
2. Detects **appliance activation/deactivation** (kettle, refrigerator, etc.)  
3. Creates **visualizations** and exports data to **CSV**  

## **🛠 Project Structure**  
```
nilm-simulator/
├── data_generator.py    # Synthetic data generator (voltage, current, power, frequency)
├── event_detector.py    # Event detection algorithm
├── visualization.py     # Data visualization
├── appliance_db.py      # Appliance characteristics database
├── main.py              # Main executable script
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
                       
```