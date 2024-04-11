import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import mplcursors

def option_c():
    try:
        file_path = r'C:\Users\Patrick Baccay\sealevel.csv'
        sea_level_data = pd.read_csv(file_path)

        # Selecting required columns
        selected_columns = ['Year', 'TotalWeightedObservations', 'GMSL_noGIA', 'GMSL_GIA']
        selected_data = sea_level_data[selected_columns]

        start_year = int(input("Enter the start year: "))
        end_year = int(input("Enter the end year: "))

        # Filtering data based on user input years
        filtered_data = selected_data[(selected_data['Year'] >= start_year) & (selected_data['Year'] <= end_year)]

        # Calculating average values
        avg_total_weighted_obs = filtered_data['TotalWeightedObservations'].mean()
        avg_gmsl_noGIA = filtered_data['GMSL_noGIA'].mean()
        avg_gmsl_GIA = filtered_data['GMSL_GIA'].mean()

        # Calculating interquartile range for TotalWeightedObservations
        Q1 = filtered_data['TotalWeightedObservations'].quantile(0.25)
        Q3 = filtered_data['TotalWeightedObservations'].quantile(0.75)
        IQR = Q3 - Q1

        # Removing outliers
        filtered_data_no_outliers = filtered_data[~((filtered_data['TotalWeightedObservations'] < (Q1 - 1.5 * IQR)) | (filtered_data['TotalWeightedObservations'] > (Q3 + 1.5 * IQR)))]

        # Recalculating average after removing outliers
        avg_total_weighted_obs_no_outliers = filtered_data_no_outliers['TotalWeightedObservations'].mean()
        avg_gmsl_noGIA_no_outliers = filtered_data_no_outliers['GMSL_noGIA'].mean()
        avg_gmsl_GIA_no_outliers = filtered_data_no_outliers['GMSL_GIA'].mean()

        # Displaying the results
        print(f"Average Total Weighted Observations from {start_year} to {end_year}: {avg_total_weighted_obs:.2f}")
        print(f"Average GMSL_noGIA from {start_year} to {end_year}: {avg_gmsl_noGIA:.2f}")
        print(f"Average GMSL_GIA from {start_year} to {end_year}: {avg_gmsl_GIA:.2f}")
        print(f"IQR for TotalWeightedObservations: {IQR:.2f}")
        print(f"Average Total Weighted Observations (without outliers): {avg_total_weighted_obs_no_outliers:.2f}")
        print(f"Average GMSL_noGIA (without outliers): {avg_gmsl_noGIA_no_outliers:.2f}")
        print(f"Average GMSL_GIA (without outliers): {avg_gmsl_GIA_no_outliers:.2f}")

        # Plotting the data
        years = filtered_data['Year']
        plt.figure(figsize=(10, 6))
        plt.plot(years, filtered_data['TotalWeightedObservations'], label='Total Weighted Observations')
        plt.plot(years, filtered_data['GMSL_noGIA'], label='GMSL_noGIA')
        plt.plot(years, filtered_data['GMSL_GIA'], label='GMSL_GIA')
        plt.xlabel('Year')
        plt.ylabel('Sea Level')
        plt.title('Sea Level Over Time')
        plt.legend()
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError:
        print("Error: Please enter valid numeric values for start and end years.")

option_c()