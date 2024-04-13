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

        min_year = selected_data['Year'].min()
        max_year = selected_data['Year'].max()

        # Getting user input for start year with validation
        start_year = None
        while start_year is None:
            try:
                start_year = int(input(f"Enter the start year ({min_year}-{max_year}): "))
                if start_year < min_year or start_year > max_year:
                    print(f"Error: Start year must be between {min_year} and {max_year}.")
                    start_year = None
            except ValueError:
                print("Error: Please enter a valid numeric value.")

        # Getting user input for end year with validation
        end_year = None
        while end_year is None:
            try:
                end_year = int(input(f"Enter the end year ({min_year}-{max_year}): "))
                if end_year < min_year or end_year > max_year:
                    print(f"Error: End year must be between {min_year} and {max_year}.")
                    end_year = None
                elif end_year < start_year:
                    print("Error: End year must be greater than or equal to start year.")
                    end_year = None
            except ValueError:
                print("Error: Please enter a valid numeric value.")

        # Filtering data based on user input years
        filtered_data = selected_data[(selected_data['Year'] >= start_year) & (selected_data['Year'] <= end_year)]

        # Calculating interquartile range for TotalWeightedObservations
        Q1 = filtered_data['TotalWeightedObservations'].quantile(0.25)
        Q3 = filtered_data['TotalWeightedObservations'].quantile(0.75)
        IQR = Q3 - Q1

        # Removing outliers
        filtered_data_no_outliers = filtered_data[~((filtered_data['TotalWeightedObservations'] < (Q1 - 1.5 * IQR)) | (filtered_data['TotalWeightedObservations'] > (Q3 + 1.5 * IQR)))]

        # Plotting
        plt.figure(figsize=(12, 6))

        # Plot for GMSL_noGIA
        plt.subplot(1, 2, 1)
        plt.scatter(filtered_data['Year'], filtered_data['GMSL_noGIA'], label='Before Outliers Removal')
        plt.scatter(filtered_data_no_outliers['Year'], filtered_data_no_outliers['GMSL_noGIA'], label='After Outliers Removal')
        plt.xlabel('Year')
        plt.ylabel('GMSL_noGIA')
        plt.title('GMSL_noGIA')
        plt.legend()

        # Plot for GMSL_GIA
        plt.subplot(1, 2, 2)
        plt.scatter(filtered_data['Year'], filtered_data['GMSL_GIA'], label='Before Outliers Removal')
        plt.scatter(filtered_data_no_outliers['Year'], filtered_data_no_outliers['GMSL_GIA'], label='After Outliers Removal')
        plt.xlabel('Year')
        plt.ylabel('GMSL_GIA')
        plt.title('GMSL_GIA')
        plt.legend()

        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError:
        print("Error: Please enter valid numeric values for start and end years.")

option_c()
