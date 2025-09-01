import os
import pandas as pd
import numpy as np
from glob import glob

# ---------- CONFIGURATION ----------
# The directory where all temperature CSV files are stored.

TEMP_DIR = os.path.join(".", "temperatures")

# Mapping months to their corresponding Australian meteorological seasons

MONTH_TO_SEASON = {
    "December": "Summer",
    "January": "Summer",
    "February": "Summer",
    "March": "Autumn",
    "April": "Autumn",
    "May": "Autumn",
    "June": "Winter",
    "July": "Winter",
    "August": "Winter",
    "September": "Spring",
    "October": "Spring",
    "November": "Spring",
}


# ---------- DATA LOADING & TRANSFORMATION ----------
def load_and_transform_data(folder: str) -> pd.DataFrame:
    """
    - Converting wide monthly columns into long format (Month → Temperature).
    - Adding 'Year' column (extracted from filename).
    - Mapping each Month into its corresponding Season.
    """

    # Find all CSV files inside the folder
    all_files = glob(os.path.join(folder, "*.csv"))
    if not all_files:
        raise ValueError(f"No CSV files found in {folder}")

    df_list = []
    for file in all_files:
        # Extract year from filename (last part before ".csv")
        year = os.path.basename(file).split("_")[-1].replace(".csv", "")

        try:
            # Load the CSV file
            df = pd.read_csv(file)
        except Exception as e:
            # If a file fails to load, skip it but show an error message
            print(f"Skipping {file}, error: {e}")
            continue

        # Convert wide-format (months as columns) to long-format
        df_long = df.melt(
            id_vars=["STATION_NAME", "STN_ID", "LAT", "LON"],  # keep station details
            value_vars=list(MONTH_TO_SEASON.keys()),            # months become rows
            var_name="Month",
            value_name="Temperature"
        )

        # Add year and season info
        df_long["Year"] = int(year)
        df_long["Season"] = df_long["Month"].map(MONTH_TO_SEASON)

        df_list.append(df_long)

    if not df_list:
        raise ValueError("No usable data found in CSV files.")

    # Merge all years into one DataFrame
    return pd.concat(df_list, ignore_index=True)


# ---------- ANALYSIS FUNCTIONS ----------
def compute_seasonal_averages(df: pd.DataFrame):
    """
    Calculating the average temperature for each season (across all stations & years).
    Saving results to 'average_temp.txt' and also printing them to the terminal.
    """
    seasonal_avg = df.groupby("Season")["Temperature"].mean().round(2)

    with open("average_temp.txt", "w") as f:
        for season, temp in seasonal_avg.items():
            line = f"{season}: {temp}°C"
            print(line)          # show in terminal
            f.write(line + "\n") # save to file


def compute_largest_range(df: pd.DataFrame):
    """
    Finding the station(s) with the largest temperature range (max - min).
    Saving results to 'largest_temp_range_station.txt' and printing them.
    """
    # Calculate min, max, and range per station
    station_stats = df.groupby("STATION_NAME")["Temperature"].agg(["min", "max"])
    station_stats["range"] = station_stats["max"] - station_stats["min"]

    # Identify station(s) with maximum range
    max_range = station_stats["range"].max()
    top_stations = station_stats[station_stats["range"] == max_range]

    with open("largest_temp_range_station.txt", "w") as f:
        for station, row in top_stations.iterrows():
            line = (f"{station}: Range {row['range']:.2f}°C "
                    f"(Max: {row['max']:.2f}°C, Min: {row['min']:.2f}°C)")
            print(line)
            f.write(line + "\n")


def compute_stability(df: pd.DataFrame):
    """
    Calculating which station is most stable (lowest std dev of temperature)
    and which is most variable (highest std dev).
    Saves results to 'temperature_stability_stations.txt' and prints them.
    """
    station_stats = df.groupby("STATION_NAME")["Temperature"].std()

    min_std = station_stats.min()  # lowest variability
    max_std = station_stats.max()  # highest variability

    most_stable = station_stats[station_stats == min_std]
    most_variable = station_stats[station_stats == max_std]

    with open("temperature_stability_stations.txt", "w") as f:
        for station, std in most_stable.items():
            line = f"Most Stable: {station}: StdDev {std:.2f}°C"
            print(line)
            f.write(line + "\n")

        for station, std in most_variable.items():
            line = f"Most Variable: {station}: StdDev {std:.2f}°C"
            print(line)
            f.write(line + "\n")


# ---------- MAIN EXECUTION ----------
def main():
    # Load and transform all CSV data
    df_all = load_and_transform_data(TEMP_DIR)

    # Remove rows where temperature data is missing
    df_all = df_all.dropna(subset=["Temperature"])

    # Run analyses and show/save results
    print("\n=== Seasonal Averages ===")
    compute_seasonal_averages(df_all)

    print("\n=== Largest Temperature Range Station(s) ===")
    compute_largest_range(df_all)

    print("\n=== Temperature Stability ===")
    compute_stability(df_all)

    print("\n Analysis complete! Results also saved to text files.")


if __name__ == "__main__":
    main()
