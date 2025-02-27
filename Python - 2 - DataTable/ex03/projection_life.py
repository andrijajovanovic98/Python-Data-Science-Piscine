import matplotlib.pyplot as plt
from load_csv import load


def plot_life_vs_gdp(filepath_gdp, filepath_life, year="1900"):
    """Plots GDP vs. life expectancy for a given year."""

    gdp_df = load(filepath_gdp)
    life_df = load(filepath_life)

    if gdp_df.empty or life_df.empty:
        raise ValueError("One of the data files is empty!")

    if 'country' not in gdp_df.columns:
        raise ValueError("In the GDP file 'country' column is not found.")
    if 'country' not in life_df.columns:
        raise ValueError(
            "There is no column called 'country' in the life expectancy file.")

    if year not in gdp_df.columns:
        raise ValueError(f"No column named '{year}' in the GDP file!")
    if year not in life_df.columns:
        raise ValueError(f"No column named '{year}' in the life file!")

    gdp_year = gdp_df[['country', year]].dropna()
    life_year = life_df[['country', year]].dropna()

    gdp_year.columns = ['country', 'gdp']
    life_year.columns = ['country', 'life']

    gdp_dict = {row[0]: row[1] for row in gdp_year.values}
    life_dict = {row[0]: row[1] for row in life_year.values}

    common_countries = set(gdp_dict.keys()) & set(life_dict.keys())

    merged = [{'country': country, 'gdp': gdp_dict[country],
               'life': life_dict[country]}
              for country in common_countries]

    if not merged:
        raise ValueError("No common countries found for the given year!")

    plt.figure(figsize=(6, 5))
    plt.scatter(
        [row['gdp'] for row in merged],
        [row['life'] for row in merged],
        alpha=0.7,
        color='#0066CC',
    )

    plt.xscale('log')
    plt.xticks([300, 1000, 10000], labels=["300", "1k", "10k"])
    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Life Expectancy")
    plt.title(f"{year}")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    try:
        plot_life_vs_gdp(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv",
            "life_expectancy_years.csv",
            year="1900"
        )
    except ValueError as e:
        print(f"{e}")
    except Exception:
        pass
