from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    A program that loads the csv file "life_expectancy.csv" and
    plots the data of Malaysia, the country of 42KL, which is my 42 campus
    """

    # load the file
    life_expectancy_df = load("life_expectancy_years.csv")

    # country of 42KL
    country_to_plot = "Malaysia"

    # make a boolean array for filtering
    country_filter = life_expectancy_df["country"] == country_to_plot

    # filter the DataFrame and remove the country column
    filtered_df = life_expectancy_df.loc[country_filter, "1800":]

    # convert the DataFrame to a Series by slicing it with .iloc
    # another way is to .squeeze() it, but it returns Any as it's more flexible
    country_data = filtered_df.iloc[0]

    # plot the data with a title and legends for both x and y axes
    country_data.plot(
        title=f"{country_to_plot} Life Expectancy Projections",
        xlabel="Year",
        ylabel="Life Expectancy")

    # alternative way of setting titles and legends
    # plt.title(f"{country_to_plot} Life Expectancy Projections")
    # plt.xlabel("Year")
    # plt.ylabel("Life Expectancy")

    # display the plot
    plt.show()


if __name__ == "__main__":
    main()
