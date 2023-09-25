from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    A program that loads the csv files "life_expectancy_years.csv" and
    "income_per_person_gdppercapita_ppp_inflation_adjusted.csv" and plots the
    projected life expectancy against the GDP of the year 1900 for each country
    """

    # load the files
    life_expectancy_df = load("life_expectancy_years.csv")
    gdp_df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    # the year to filter to
    year_to_plot = "1900"

    # filter the DataFrames to the year 1900
    life_expectancy_1900_df = life_expectancy_df[["country", year_to_plot]]
    gdp_1900_df = gdp_df[["country", year_to_plot]]

    # rename the columns
    life_expectancy_1900_df.columns = ["Country", "Life Expectancy"]
    gdp_1900_df.columns = ["Country", "Gross Domestic Product"]

    # combine the DataFrames into one
    combined_df = life_expectancy_1900_df.merge(gdp_1900_df, on="Country")

    # set the title and x ticks
    # use log scaling on x axis to improve viewing experience
    combined_df.plot(
        kind="scatter",
        x="Gross Domestic Product",
        y="Life Expectancy",
        logx=True,
        title=year_to_plot,
    )

    # make the x ticks more readable
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])

    # display the plot
    plt.show()


if __name__ == "__main__":
    main()
