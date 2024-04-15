import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import mplcursors
import seaborn as sns

print ("Welcome")

def option_a():
    try:
        file_path = r'https://raw.githubusercontent.com/Wiggins04/Team3/main/sealevel.csv'

        sea_level_data = pd.read_csv(file_path)

        # Get the list of years available in the dataset
        available_years = sea_level_data['Year'].unique()

        year = int(input("Enter a year to calculate the average GMSL_noGIA(1993-2021): "))

        # Check if the entered year is available in the dataset
        if year not in available_years:
            print("The entered year is not available in the dataset.")
            option_a()
        else:
            data_for_year = sea_level_data[sea_level_data['Year'] == year]

            # calculate average GMSL_noGIA for the specified year
            avg_gmsl_noGIA = data_for_year['GMSL_noGIA'].mean()
            print(f"Average GMSL_noGIA for the year {year}: {avg_gmsl_noGIA:.2f} mm")

            # plot a graph of data values against total observations
            plt.figure(figsize=(10, 6))
            scatter = plt.scatter(data_for_year['TotalWeightedObservations'], data_for_year['GMSL_noGIA'], marker='o')
            plt.title(f'Sea Level Values for Year {year}')
            plt.xlabel('Total Weighted Observations')
            plt.ylabel('Sea Level (mm)')
            plt.grid(True)

            # Add hover functionality
            mplcursors.cursor(scatter, hover=True).connect("add", lambda sel: sel.annotation.set_text(f"Total Weighted Observations: {sel.target[0]}, GMSL_noGIA: {sel.target[1]:.2f} mm"))

            plt.show()
            mainMenu()

    except Exception as e:
        print("An error occurred:", e)

option_a()
