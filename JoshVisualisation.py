import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset from the specified file path
file_path = r'C:\Users\csmjhug1\OneDrive - Liverpool John Moores University\Documents\thing\sealevel.csv'
data = pd.read_csv(file_path)

# Extract columns 'Year', 'GMSL_noGIA', and 'GMSL_GIA'
data = data[['Year', 'GMSL_noGIA', 'GMSL_GIA']]

# Function to validate user input
def validate_year_input(year, data):
    available_years = data['Year'].unique()
    if year in available_years:
        return True
    else:
        return False

# Prompt the user to input start year and validate
while True:
    start_year = input("Enter the start year: ")
    if start_year.isdigit() and validate_year_input(int(start_year), data):
        start_year = int(start_year)
        break
    else:
        print("Invalid input. Please enter a valid start year.")

# Prompt the user to input end year and validate
while True:
    end_year = input("Enter the end year: ")
    if end_year.isdigit() and validate_year_input(int(end_year), data):
        end_year = int(end_year)
        break
    else:
        print("Invalid input. Please enter a valid end year.")

# Filter the dataset based on user input
filtered_data = data[(data['Year'] >= start_year) & (data['Year'] <= end_year)]

# Calculate the difference between 'GMSL_noGIA' and 'GMSL_GIA'
difference = filtered_data['GMSL_noGIA'].iloc[-1] - filtered_data['GMSL_GIA'].iloc[-1]

# Create a line plot for the selected data
plt.plot(filtered_data['Year'], filtered_data['GMSL_noGIA'], label='GMSL_noGIA')
plt.plot(filtered_data['Year'], filtered_data['GMSL_GIA'], label='GMSL_GIA')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (mm)')
plt.title('Sea Level Comparison between GMSL_noGIA and GMSL_GIA')
plt.legend()

# Show plot
plt.grid(True)
plt.tight_layout()
plt.show()

