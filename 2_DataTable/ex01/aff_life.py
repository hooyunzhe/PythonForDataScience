from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    A program that loads the csv file "life_expectancy.csv"
    and plots the country data of my 42 campus, which is Malaysia
    """

    # load the file
    df = load("life_expectancy_years.csv")

    # the country to plot
    country_to_plot = "Malaysia"

    # filter the DataFrame and remove the country column
    filtered_df = df.loc[df["country"] == country_to_plot, "1800":]

    # convert the DataFrame to a Series by squeezing
    country_data = filtered_df.squeeze()

    # set the title and legends for both x and y axes
    plt.title(f"{country_to_plot} Life Expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")

    # plot the data and display the plot
    country_data.plot()
    plt.show()


if __name__ == "__main__":
    main()
