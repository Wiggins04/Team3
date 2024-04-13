import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import mplcursors
import seaborn as sns

print ("Welcome")

def validate_data(data, start_year, end_year):
    min_year = data['Year'].min()
    max_year = data['Year'].max()
    return min_year <= start_year <= max_year and min_year <= end_year <= max_year


def option_d():
       # Change path when necessary
    file_path = r'https://raw.githubusercontent.com/Wiggins04/Team3/main/sealevel.csv'

    columns_to_extract = ['Year', 'GMSL_noGIA', 'SmoothedGSML_noGIA', 'GMSL_GIA', 'SmoothedGSML_GIA', 'SmoothedGSML_GIA_sigremoved']

    try:
        # Read csv file into a data frame
        full_data = pd.read_csv(file_path)

        # Get user input for the years they want data from
        start_year = int(input("Enter the start year: "))
        end_year = int(input("Enter the end year: "))

        # Validate user input
        if validate_data(full_data, start_year, end_year):
            filtered_data = full_data.loc[(full_data['Year'] >= start_year) & (full_data['Year'] <= end_year), columns_to_extract]
            # Remove rows where GMSL_noGIA is zero to avoid any errors
            filtered_data_noGIA = filtered_data[filtered_data['GMSL_noGIA'] != 0]
            # Calculate average percentage change of SmoothedGSML_noGIA relative to GMSL_noGIA
            smoothed_noGIA_avg_change = ((filtered_data_noGIA['SmoothedGSML_noGIA'] - filtered_data_noGIA['GMSL_noGIA']) / filtered_data_noGIA['GMSL_noGIA']).mean() * 100
            # Remove rows where GMSL_GIA is zero
            filtered_data_GIA = filtered_data[filtered_data['GMSL_GIA'] != 0]
            # Calculate average percentage change of SmoothedGSML_GIA relative to GMSL_GIA
            smoothed_GIA_avg_change = ((filtered_data_GIA['SmoothedGSML_GIA'] - filtered_data_GIA['GMSL_GIA']) / filtered_data_GIA['GMSL_GIA']).mean() * 100
            # Remove rows where SmoothedGSML_GIA_sigremoved is zero
            filtered_data_GIA_sigremoved = filtered_data[filtered_data['SmoothedGSML_GIA_sigremoved'] != 0]
            # Calcu late average percentage change of SmoothedGSML_GIA_sigremoved relative to SmoothedGSML_GIA
            smoothed_GIA_sigremoved_avg_change = ((filtered_data_GIA_sigremoved['SmoothedGSML_GIA_sigremoved'] - filtered_data_GIA_sigremoved['SmoothedGSML_GIA']) / filtered_data_GIA_sigremoved['SmoothedGSML_GIA']).mean() * 100

            # Display the results
            print(f"Average percentage change of SmoothedGSML_noGIA relative to GMSL_noGIA: {smoothed_noGIA_avg_change:.2f}%")
            print(f"Average percentage change of SmoothedGSML_GIA relative to GMSL_GIA: {smoothed_GIA_avg_change:.2f}%")
            print(f"Average percentage change of SmoothedGSML_GIA_sigremoved relative to SmoothedGSML_GIA: {smoothed_GIA_sigremoved_avg_change:.2f}%")
            
            # Melt the DataFrame to make it suitable for boxplot
            melted_data = pd.melt(filtered_data, id_vars=['Year'], value_vars=['GMSL_noGIA', 'SmoothedGSML_noGIA', 'GMSL_GIA', 'SmoothedGSML_GIA', 'SmoothedGSML_GIA_sigremoved'], var_name='Variable', value_name='Value')

            # Plot box plots for GMSL_noGIA and its smoothed counterpart
            plt.figure(figsize=(12, 8))
            sns.boxplot(data=melted_data[melted_data['Variable'].isin(['GMSL_noGIA', 'SmoothedGSML_noGIA'])], x='Year', y='Value', hue='Variable', palette='pastel')
            plt.title('Effect of Smoothing Filter (No GIA)')
            plt.xlabel('Year')
            plt.ylabel('Sea Level (mm)')
            plt.legend(title='Data Type')
            plt.ylim(bottom=filtered_data['GMSL_noGIA'].min(), top=filtered_data['GMSL_noGIA'].max() * 1.1)  # Adjust the y-axis limits
            plt.show()

            # Plot box plots for GMSL_GIA and its smoothed counterpart
            plt.figure(figsize=(12, 8))
            sns.boxplot(data=melted_data[melted_data['Variable'].isin(['GMSL_GIA', 'SmoothedGSML_GIA'])], x='Year', y='Value', hue='Variable', palette='pastel')
            plt.title('Effect of Smoothing Filter (GIA)')
            plt.xlabel('Year')
            plt.ylabel('Sea Level (mm)')
            plt.legend(title='Data Type')
            plt.ylim(bottom=filtered_data['GMSL_GIA'].min(), top=filtered_data['GMSL_GIA'].max() * 1.1)  # Adjust the y-axis limits
            plt.show()

            # Plot box plots for SmoothedGSML_GIA and SmoothedGSML_GIA_sigremoved
            plt.figure(figsize=(12, 8))
            sns.boxplot(data=melted_data[melted_data['Variable'].isin(['SmoothedGSML_GIA', 'SmoothedGSML_GIA_sigremoved'])], x='Year', y='Value', hue='Variable', palette='pastel')
            plt.title('Effect of Smoothing Filter (GIA vs GIA_sigremoved)')
            plt.xlabel('Year')
            plt.ylabel('Sea Level (mm)')
            plt.legend(title='Data Type')
            plt.ylim(bottom=filtered_data['SmoothedGSML_GIA'].min(), top=filtered_data['SmoothedGSML_GIA'].max() * 1.1)  # Adjust the y-axis limits
            plt.show()

        else:
            print("Error: Start and end years are not within the range of available years in the dataset.")
            option_d()

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

    except ValueError:
        print("Error: Please enter valid numeric values for start and end years.")
        option_d()

option_d()
