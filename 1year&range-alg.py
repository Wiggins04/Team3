import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import mplcursors

# Function to calculate average sea level change for one year
def calculate_average_sea_level_change_one_year(year):
    filtered_data = filter_dataset_by_year(year)
    average_noGIA = calculate_average(filtered_data['GMSL_noGIA'])
    average_GIA = calculate_average(filtered_data['GMSL_GIA'])
    return average_noGIA, average_GIA

# Function to calculate average sea level change for multiple years
def calculate_average_sea_level_change_multiple_years(start_year, end_year):
    filtered_data = filter_dataset_by_year_range(start_year, end_year)
    average_noGIA = calculate_average(filtered_data['GMSL_noGIA'])
    average_GIA = calculate_average(filtered_data['GMSL_GIA'])
    return average_noGIA, average_GIA

# Function to filter dataset by year
def filter_dataset_by_year(year):
    filtered_data = dataset[dataset['Year'] == year]
    return filtered_data

# Function to filter dataset by year range
def filter_dataset_by_year_range(start_year, end_year):
    filtered_data = dataset[(dataset['Year'] >= start_year) & (dataset['Year'] <= end_year)]
    return filtered_data

# Function to calculate average
def calculate_average(data):
    return sum(data) / len(data)

# Main program
if __name__ == "__main__":
    # Load dataset from CSV file
    dataset = pd.read_csv("sealevel.csv")

    # User input for one year
    target_year = int(input("Enter the target year: "))
    average_noGIA_one_year, average_GIA_one_year = calculate_average_sea_level_change_one_year(target_year)
    print("Average sea level change for year {} without GIA: {}".format(target_year, average_noGIA_one_year))
    print("Average sea level change for year {} with GIA: {}".format(target_year, average_GIA_one_year))

    # User input for multiple years
    start_year = int(input("Enter the start year: "))
    end_year = int(input("Enter the end year: "))
    average_noGIA_multiple_years, average_GIA_multiple_years = calculate_average_sea_level_change_multiple_years(start_year, end_year)
    print("Average sea level change for years {}-{} without GIA: {}".format(start_year, end_year, average_noGIA_multiple_years))
    print("Average sea level change for years {}-{} with GIA: {}".format(start_year, end_year, average_GIA_multiple_years))
