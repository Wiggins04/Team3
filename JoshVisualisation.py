def option_d():
    # Read csv
    file_path = r'https://raw.githubusercontent.com/Wiggins04/Team3/Sam-cockayne-Visualisation/sealevel.csv'
    data = pd.read_csv(file_path)

    # Use columns 'Year', 'GMSL_noGIA', and 'GMSL_GIA'
    data = data[['Year', 'GMSL_noGIA', 'GMSL_GIA']]

    # Validate UI for years
    def validate_year_input(year, data):
        available_years = data['Year'].unique()
        if year in available_years:
            return True
        else:
            return False

    # Ask user to input start year
    while True:
        start_year = input("Enter the start year: ")
        if start_year.isdigit() and validate_year_input(int(start_year), data):
            start_year = int(start_year)
            break
        else:
            print("Invalid input. Please enter a valid start year (between 1993-2021).")
            option_d()

    # Ask user to input end year
    while True:
        end_year = input("Enter the end year: ")
        if end_year.isdigit() and validate_year_input(int(end_year), data):
            end_year = int(end_year)
            break
        else:
            print("Invalid input. Please enter a valid end year (between 1993-2021).")
            option_d()

    # Filter the dataset based on UI
    filtered_data = data[(data['Year'] >= start_year) & (data['Year'] <= end_year)]

    # Melt the DataFrame to make it suitable for boxplot
    melted_data = pd.melt(filtered_data, id_vars=['Year'], 
                          value_vars=['GMSL_noGIA', 'GMSL_GIA'], 
                          var_name='Variable', value_name='Value')

    # Plot box plots
    plt.figure(figsize=(12, 8))
    sns.boxplot(data=melted_data, x='Year', y='Value', hue='Variable', palette='pastel')
    plt.title('Sea Level Comparison between GMSL_noGIA and GMSL_GIA')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (mm)')
    plt.legend(title='Dataset')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Calculate percentage change due to GIA
    percentage_change_GIA = (filtered_data['GMSL_GIA'].iloc[-1] - filtered_data['GMSL_noGIA'].iloc[-1]) / filtered_data['GMSL_noGIA'].iloc[-1] * 100

    # Print percentage change due to GIA
    print(f"The percentage change due to the GIA filter is: {percentage_change_GIA:.2f}%")
    mainMenu()
