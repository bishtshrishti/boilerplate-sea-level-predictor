
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Create first line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    years = pd.Series(range(1880, 2051))
    predictions = slope * years + intercept
    ax.plot(years, predictions, color="red")

    # Create second line of best fit using data from 2000 onward
    recent_df = df[df["Year"] >= 2000]

    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(
        recent_df["Year"],
        recent_df["CSIRO Adjusted Sea Level"]
    )

    recent_years = pd.Series(range(2000, 2051))
    recent_predictions = slope_recent * recent_years + intercept_recent
    ax.plot(recent_years, recent_predictions, color="green")

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
