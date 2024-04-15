import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import mplcursors

def option_b():
    try:
        # Read data file
        file_path = r'https://raw.githubusercontent.com/Wiggins04/Team3/main/sealevel.csv'

        sea_level_data = pd.read_csv(file_path)

        # Validate data columns
        if not all(col in sea_level_data.columns for col in ['Year', 'GMSL_noGIA', 'GMSL_GIA']):
            raise ValueError("Data missing expected columns (Year, GMSL_noGIA, GMSL_GIA)")

        # Get start and end years
        start_year = int(input("Enter the start year (1993-2021): "))
        end_year = int(input("Enter the end year (1993-2021): "))
        
        # Check if end year is within range
        while end_year > 2021:
            print("End year cannot exceed 2021. Please enter a valid end year.")
            option_b()
        
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
