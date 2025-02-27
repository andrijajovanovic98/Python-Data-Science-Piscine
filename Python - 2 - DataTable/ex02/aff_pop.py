import matplotlib.pyplot as plt
from load_csv import load


def get_country_data(data, country_name):
    """Return years and population data (in millions)
    for a given country from the dataset."""

    years = list(map(int, data.columns[1:]))

    country_row = data[data['country'] == country_name]

    if country_row.empty:
        raise ValueError(f"{country_name} not found in dataset")

    country_values = [
        float(value.replace('M', ''))
        for value in country_row.iloc[:, 1:].values.flatten()
    ]

    return years, country_values


def plot_population(country1, country2, filepath='population_total.csv'):
    """Calculating the values and creating the plot"""
    data = load(filepath)

    years, values1 = get_country_data(data, country1)
    _, values2 = get_country_data(data, country2)

    filtered_years = [y for y in years if y <= 2050]
    filtered_values1 = [v for y, v in zip(years, values1) if y <= 2050]
    filtered_values2 = [v for y, v in zip(years, values2) if y <= 2050]

    plt.figure(figsize=(8, 5))

    plt.plot(filtered_years, filtered_values1,
             linestyle='-', label=country1)
    plt.plot(filtered_years, filtered_values2,
             linestyle='-', label=country2)

    plt.xlim(1790, 2060)
    plt.xticks(range(1800, 2050, 40))

    plt.ylim(0, 70)
    plt.yticks([20, 40, 60], ["20M", "40M", "60M"])

    plt.xlabel('Year')
    plt.ylabel('Population (millions)')
    plt.title('Population Projections')

    plt.legend()

    plt.show()


if __name__ == "__main__":
    """Main script"""
    try:
        plot_population("Belgium", "France")
    except ValueError as e:
        print(f"{e}")
    except Exception:
        pass
