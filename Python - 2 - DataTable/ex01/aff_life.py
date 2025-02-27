import matplotlib.pyplot as plt
from load_csv import load


def plot_life_expectancy(country, filepath='life_expectancy_years.csv'):
    """Data manipulation and creating the plot"""
    df = load(filepath)

    df.set_index('country', inplace=True)

    if country not in df.index:
        raise ValueError(f"{country} not found in dataset")

    country_data = df.loc[country]
    country_data.index = country_data.index.astype(int)
    country_data = country_data.astype(float)

    plt.plot(list(country_data.index), country_data.values, linestyle='-')
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.title("Austria Life Expectancy Over Time")

    plt.show()


if __name__ == "__main__":
    """""Main script"""
    try:
        plot_life_expectancy("France")
    except ValueError as e:
        print(f"{e}")
    except Exception:
        pass
