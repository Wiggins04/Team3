import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import mplcursors

while True:
    try:
        # Read data file
        file_path = r'C:\Users\caiar\OneDrive\Desktop\UniServerZ\UniServerZ\www\422COMP\sealevel.csv'
        sea_level_data = pd.read_csv(file_path)

        # Validate data columns
        if not all(col in sea_level_data.columns for col in ['Year', 'GMSL_noGIA', 'GMSL_GIA']):
            raise ValueError("Data missing expected columns (Year, GMSL_noGIA, GMSL_GIA)")

        # Get start and end years
        start_year = int(input("Enter the start year (1993-2021): "))
        end_year = int(input("Enter the end year (1993-2021): "))
        
        # Check if end year is within range
        if end_year > 2021:
            print("End year cannot exceed 2021. Please enter a valid end year.")
            continue  # Restart the loop
        
        # Group data by year and calculate the average sea level values
        grouped_data = sea_level_data[(sea_level_data['Year'] >= start_year) & (sea_level_data['Year'] <= end_year)].groupby('Year').mean().reset_index()

        # Plot sea level values against the years for GMSL_noGIA
        plt.figure(figsize=(10, 6))
        scatter = plt.scatter(grouped_data['Year'], grouped_data['GMSL_noGIA'], label='GMSL_noGIA', marker='o')

        # Add hover functionality
        mplcursors.cursor(scatter, hover=True).connect("add", lambda sel: sel.annotation.set_text(f"Year: {sel.target[0]}, GMSL_noGIA: {sel.target[1]:.2f} mm"))

        # Calculate line of best fit for GMSL_noGIA
        slope_noGIA, intercept_noGIA, _, _, _ = linregress(grouped_data['Year'], grouped_data['GMSL_noGIA'])
        line_noGIA = slope_noGIA * grouped_data['Year'] + intercept_noGIA

        #Titles for graph
        plt.plot(grouped_data['Year'], line_noGIA, color='blue', linestyle='--', label='Line of Best Fit (No GIA)')
        plt.title(f'Average Sea Level Values (No GIA) for Years {start_year}-{end_year}')
        plt.xlabel('Year')
        plt.ylabel('Average Sea Level (mm)')
        plt.legend()
        plt.grid(True)
        plt.show()

        # Plot sea level values against the years for GMSL_GIA
        plt.figure(figsize=(10, 6))
        scatter = plt.scatter(grouped_data['Year'], grouped_data['GMSL_GIA'], label='GMSL_GIA', marker='x')

        # Add hover functionality
        mplcursors.cursor(scatter, hover=True).connect("add", lambda sel: sel.annotation.set_text(f"Year: {sel.target[0]}, GMSL_GIA: {sel.target[1]:.2f} mm"))

        # Calculate line of best fit for GMSL_GIA
        slope_GIA, intercept_GIA, _, _, _ = linregress(grouped_data['Year'], grouped_data['GMSL_GIA'])
        line_GIA = slope_GIA * grouped_data['Year'] + intercept_GIA

        #Titles for graph
        plt.plot(grouped_data['Year'], line_GIA, color='orange', linestyle='--', label='Line of Best Fit (GIA)')
        plt.title(f'Average Sea Level Values (GIA) for Years {start_year}-{end_year}')
        plt.xlabel('Year')
        plt.ylabel('Average Sea Level (mm)')
        plt.legend()
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError:
        print("Error: Please enter valid numeric values for start and end years.")
    except Exception as e:
        print("An error occurred:", e)
    
    try:
        # Ask user if they want to continue
        again = input("Do you want to analyze data for another period? (yes/no): ").lower()
        if again != "yes":
            break
    except Exception as e:
        print("An error occurred:", e)
