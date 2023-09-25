from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    A program that loads the csv file "population_total.csv",
    plots the data of Malaysia, the country of 42KL, which is my 42 campus
    and compares it to another country of my choice, which is "country"
    """

    # load the file
    population_df = load("population_total.csv")

    # countries to compare
    country_one = "Malaysia"
    country_two = "South Korea"

    # make a boolean array for filtering
    country_filter = population_df["country"].isin([country_one, country_two])

    # filter the DataFrame and only keep years 1800 to 2050
    filtered_df = population_df.loc[country_filter, :"2050"]

    # extract the country names for the columns
    country_names = filtered_df["country"]
    country_names.name = None

    # transpose the DataFrame and remove the country
    countries_data = filtered_df.T[1:]

    # set the columns
    countries_data.columns = country_names

    # function to convert numbers with short forms (k, M, B) to integers
    def convert_number(number_string: str) -> int:
        if type(number_string) is str:
            if (number_string[-1] == "k"):
                return int(float(number_string[:-1]) * 1000)
            if (number_string[-1] == "M"):
                return int(float(number_string[:-1]) * 1000000)
            if (number_string[-1] == "B"):
                return int(float(number_string[:-1]) * 1000000000)
        return number_string

    # convert the values to integers
    countries_data = countries_data.map(convert_number)

    # plot the data with a title and legends for both x and y axes
    countries_data.plot(
        title="Population Projections",
        xlabel="Year",
        ylabel="Population")

    # extract the y ticks and transform to numbers with M short form
    locs, labels = plt.yticks()
    plt.yticks(locs[1:], [f"{int(n / 1000000)}M" for n in locs[1:]])

    # display the plot
    plt.show()


if __name__ == "__main__":
    main()
