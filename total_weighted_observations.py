import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import mplcursors

def option_c():
    try:
        file_path = r'https://raw.githubusercontent.com/Wiggins04/Team3/main/sealevel.csv'
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

        # Calculating average values
        avg_total_weighted_obs = filtered_data['TotalWeightedObservations'].mean()
        avg_gmsl_noGIA = filtered_data['GMSL_noGIA'].mean()
        avg_gmsl_GIA = filtered_data['GMSL_GIA'].mean()

        # Calculating interquartile range for TotalWeightedObservations
        Q1 = filtered_data['TotalWeightedObservations'].quantile(0.25)
        Q3 = filtered_data['TotalWeightedObservations'].quantile(0.75)
        IQR = Q3 - Q1

        # Removing outliers
        filtered_data_no_outliers = filtered_data[~((filtered_data['TotalWeightedObservations'] < (Q1 - 1.5 * IQR)) |
                                                   (filtered_data['TotalWeightedObservations'] > (Q3 + 1.5 * IQR)))]

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
        fig, axes = plt.subplots(2, 2, figsize=(12, 12))
        
        # Plot for GMSL_noGIA with outliers
        ax1 = axes[0, 0]
        ax1.plot(filtered_data['Year'], filtered_data['GMSL_noGIA'], 'bo', label='With Outliers')
        ax1.set_xlabel('Year')
        ax1.set_ylabel('GMSL_noGIA')
        ax1.set_title('GMSL_noGIA with Outliers')
        slope, intercept, _, _, _ = linregress(filtered_data['Year'], filtered_data['GMSL_noGIA'])
        ax1.plot(filtered_data['Year'], intercept + slope * filtered_data['Year'], 'r--')
        ax1.legend()
        ax1.grid(True)

        # Plot for GMSL_noGIA without outliers
        ax2 = axes[0, 1]
        ax2.plot(filtered_data_no_outliers['Year'], filtered_data_no_outliers['GMSL_noGIA'], 'ro', label='Without Outliers')
        ax2.set_xlabel('Year')
        ax2.set_ylabel('GMSL_noGIA')
        ax2.set_title('GMSL_noGIA without Outliers')
        slope_no_outliers, intercept_no_outliers, _, _, _ = linregress(filtered_data_no_outliers['Year'], filtered_data_no_outliers['GMSL_noGIA'])
        ax2.plot(filtered_data_no_outliers['Year'], intercept_no_outliers + slope_no_outliers * filtered_data_no_outliers['Year'], 'b--')
        ax2.legend()
        ax2.grid(True)

        # Plot for GMSL_GIA with outliers
        ax3 = axes[1, 0]
        ax3.plot(filtered_data['Year'], filtered_data['GMSL_GIA'], 'bo', label='With Outliers')
        ax3.set_xlabel('Year')
        ax3.set_ylabel('GMSL_GIA')
        ax3.set_title('GMSL_GIA with Outliers')
        slope, intercept, _, _, _ = linregress(filtered_data['Year'], filtered_data['GMSL_GIA'])
        ax3.plot(filtered_data['Year'], intercept + slope * filtered_data['Year'], 'r--')
        ax3.legend()
        ax3.grid(True)

        # Plot for GMSL_GIA without outliers
        ax4 = axes[1, 1]
        ax4.plot(filtered_data_no_outliers['Year'], filtered_data_no_outliers['GMSL_GIA'], 'ro', label='Without Outliers')
        ax4.set_xlabel('Year')
        ax4.set_ylabel('GMSL_GIA')
        ax4.set_title('GMSL_GIA without Outliers')
        slope_no_outliers, intercept_no_outliers, _, _, _ = linregress(filtered_data_no_outliers['Year'], filtered_data_no_outliers['GMSL_GIA'])
        ax4.plot(filtered_data_no_outliers['Year'], intercept_no_outliers + slope_no_outliers * filtered_data_no_outliers['Year'], 'b--')
        ax4.legend()
        ax4.grid(True)

        # Add hover functionality
        mplcursors.cursor(ax1, hover=True).connect("add", lambda sel: sel.annotation.set_text(f"Year: {sel.target[0]}, GMSL_noGIA: {sel.target[1]:.2f}"))
        mplcursors.cursor(ax2, hover=True).connect("add", lambda sel: sel.annotation.set_text(f"Year: {sel.target[0]}, GMSL_noGIA: {sel.target[1]:.2f}"))
        mplcursors.cursor(ax3, hover=True).connect("add", lambda sel: sel.annotation.set_text(f"Year: {sel.target[0]}, GMSL_GIA: {sel.target[1]:.2f}"))
        mplcursors.cursor(ax4, hover=True).connect("add", lambda sel: sel.annotation.set_text(f"Year: {sel.target[0]}, GMSL_GIA: {sel.target[1]:.2f}"))

        plt.tight_layout()
        plt.show()
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError:
        print("Error: Please enter valid numeric values for start and end years.")

option_c()
