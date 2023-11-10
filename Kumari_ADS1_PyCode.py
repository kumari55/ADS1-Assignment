import pandas as pd
import matplotlib.pyplot as plt


#Data cleaning
data = pd.read_csv("FertilityData.csv")
data.head()

# Checking for missing values
missing_data = data.isnull().sum()
print(missing_data)

# Filling missing values with zeros
data = data.fillna(0)

# Renaming columns
data = data.rename(columns={'Indicator Name': 'Indicator', 'Indicator Code': 'Indicator_Code'})

# Converting year columns to integers
year_columns = [str(year) for year in range(1960, 2023)]  # Taking 2023 is the last year
data[year_columns] = data[year_columns].astype(float)

data.info()  # Checking data types and non-null counts
data.head()  # Verifying the first few rows of the cleaned dataset

data.to_csv('cleaned_dataset.csv', index=False)



#graph 1
# Load the Cleaned Dataset


def plot_fertility_comparison(data, countries, years):
    
    plt.figure(figsize=(12, 6))

    for country in countries:
        country_data = data[data['Country Name'] == country]
        plt.plot(years, country_data[years].values[0], marker='o', linestyle='-', label=country)

    plt.title('Fertility Rate Comparison (1960-2022) for Selected Countries')
    plt.xlabel('Year')
    plt.ylabel('Fertility Rate')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()


data = pd.read_csv("cleaned_dataset.csv")

# Select countries for comparison
selected_countries = ['United Kingdom', 'Ireland', 'France', 'Germany', 'Netherlands', 'Belgium', 'United States']

# Select Relevant Columns for Years 1960 to 2022
selected_years = [str(year) for year in range(1960, 2023)]
selected_fertility_data = data[selected_years]

# Call the function to plot fertility comparison
plot_fertility_comparison(data, selected_countries, selected_years)



#graph 2


def plot_fertility_comparison_2020(data, countries):
    
    selected_year = '2020'

    # Filter the data for the selected countries
    fertility_2020 = data[data['Country Name'].isin(countries)][['Country Name', selected_year]]

    # Sort countries by fertility rate
    fertility_2020 = fertility_2020.sort_values(by=selected_year, ascending=False)

    # Create a bar chart with improved aesthetics
    plt.figure(figsize=(10, 6))
    bars = plt.bar(fertility_2020['Country Name'], fertility_2020[selected_year])

    # Customize bar colors
    colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightseagreen']
    for bar, color in zip(bars, colors):
        bar.set_color(color)

    # Add data labels above the bars
    for bar in bars:
        height = bar.get_height()
        plt.annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 3),
                     textcoords="offset points", ha='center', va='bottom')

    plt.title(f'Fertility Rate Comparison ({selected_year}) for Selected Countries')
    plt.xlabel('Country')
    plt.ylabel('Fertility Rate')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.ylim(0, max(fertility_2020[selected_year]) + 1)  # Adjust the y-axis limits
    plt.tight_layout()
    plt.show()


data = pd.read_csv("cleaned_dataset.csv")

# Select countries for comparison
selected_countries = ['United Kingdom', 'Ireland', 'France', 'Belgium', 'Netherlands']

# Call the function to plot fertility comparison for the year 2020
plot_fertility_comparison_2020(data, selected_countries)



#graph 3


def plot_scatter_fertility_comparison(data, selected_year, countries):
    
    # Filter the data for the selected countries
    filtered_data = data[data['Country Name'].isin(countries)][['Country Name', selected_year]]

    # Sort countries by fertility rate
    filtered_data = filtered_data.sort_values(by=selected_year, ascending=False)

    # Create a scatter plot with improved aesthetics
    plt.figure(figsize=(12, 6))
    plt.scatter(filtered_data[selected_year], filtered_data[selected_year], label='Fertility Rate vs. Fertility Rate', color='b', s=100)

    # Add labels and title
    plt.title(f'Scatter Plot: Fertility Rate vs. Fertility Rate ({selected_year}) for Selected Countries')
    plt.xlabel('Fertility Rate')
    plt.ylabel('Fertility Rate')
    plt.grid(True, linestyle='--', alpha=0.7)

    # Add country labels to data points with better placement
    for i, country in enumerate(countries):
        x, y = filtered_data[selected_year].iloc[i], filtered_data[selected_year].iloc[i]
        plt.annotate(country, (x, y), fontsize=10, xytext=(-20, -5), textcoords='offset points')

    plt.legend()
    plt.tight_layout()
    plt.show()


data = pd.read_csv("cleaned_dataset.csv")

# Select a specific year for comparison
selected_year = '2021'
# Select countries for comparison
selected_countries = ['United Kingdom', 'Ireland', 'France', 'Belgium', 'Netherlands', 'Germany', 'Spain', 'Italy', 'Sweden', 'United States']

# Call the function to plot the scatter plot for fertility comparison
plot_scatter_fertility_comparison(data, selected_year, selected_countries)


#graph 4
def plot_pie_fertility_proportion(data, selected_year, countries):
    
    # Filter the data for the selected countries
    filtered_data = data[data['Country Name'].isin(countries)][['Country Name', selected_year]]

    # Create a pie chart to visualize the proportion of fertility rates
    plt.figure(figsize=(8, 8))
    plt.pie(filtered_data[selected_year], labels=filtered_data['Country Name'], autopct='%1.1f%%', startangle=140,
            colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2', '#c2e6f3', '#f0f0c2', '#e6c2f3'])

    # Add title
    plt.title(f'Fertility Rate Proportion ({selected_year}) for Selected Countries')

    plt.show()


data = pd.read_csv("cleaned_dataset.csv")

# Select a specific year for comparison
selected_year = '2021'
# Select countries for comparison
selected_countries = ['United Kingdom', 'Ireland', 'France', 'Belgium', 'Netherlands', 'Germany', 'Spain', 'Italy', 'Sweden', 'United States']

# Call the function to plot the pie chart for fertility proportion
plot_pie_fertility_proportion(data, selected_year, selected_countries)
