import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def calculate_average_sea_level_change_one_year(year):
    filtered_data = filter_dataset_by_year(year)
    average_noGIA = calculate_average(filtered_data['GMSL_noGIA'])
    average_GIA = calculate_average(filtered_data['GMSL_GIA'])
    return average_noGIA, average_GIA

def calculate_average_sea_level_change_multiple_years(start_year, end_year):
    filtered_data = filter_dataset_by_year_range(start_year, end_year)
    average_noGIA = calculate_average(filtered_data['GMSL_noGIA'])
    average_GIA = calculate_average(filtered_data['GMSL_GIA'])
    return average_noGIA, average_GIA

def filter_dataset_by_year(year):
    filtered_data = dataset[dataset['Year'] == year]
    return filtered_data

def filter_dataset_by_year_range(start_year, end_year):
    filtered_data = dataset[(dataset['Year'] >= start_year) & (dataset['Year'] <= end_year)]
    return filtered_data

def calculate_average(data):
    return sum(data) / len(data)

def plot_sea_level_change_over_time():
    plt.figure(figsize=(10, 6))
    plt.plot(dataset['Year'], dataset['GMSL_noGIA'], label='Sea Level Change without GIA')
    plt.plot(dataset['Year'], dataset['GMSL_GIA'], label='Sea Level Change with GIA')
    plt.xlabel('Year')
    plt.ylabel('Sea Level Change (mm)')
    plt.title('Sea Level Change Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":

    dataset = pd.read_csv("sealevel.csv")

    option = input("Would you like to see the graph (type 'graph') or input a year/range (type 'year')? ").lower()

    if option == 'graph':

        plot_sea_level_change_over_time()
    elif option == 'year':
 
        target_year = int(input("Enter the target year: "))
        average_noGIA_one_year, average_GIA_one_year = calculate_average_sea_level_change_one_year(target_year)
        print("Average sea level change for year {} without GIA: {}".format(target_year, average_noGIA_one_year))
        print("Average sea level change for year {} with GIA: {}".format(target_year, average_GIA_one_year))


        start_year = int(input("Enter the start year: "))
        end_year = int(input("Enter the end year: "))
        average_noGIA_multiple_years, average_GIA_multiple_years = calculate_average_sea_level_change_multiple_years(start_year, end_year)
        print("Average sea level change for years {}-{} without GIA: {}".format(start_year, end_year, average_noGIA_multiple_years))
        print("Average sea level change for years {}-{} with GIA: {}".format(start_year, end_year, average_GIA_multiple_years))
    else:
        print("Invalid option. Please type 'graph' or 'year'.")
