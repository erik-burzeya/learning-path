# CHAPTER 3: Visualising Data: Practice
def Task_VISUALISING_DATA_1():
    # Task 3.1 — Create a Simple Line Chart with Matplotlib

    # OOBJECTIVE:
    # Learn how to create a basic data visualisation in Python using the matplotlib library.
    # This exercise focuses on plotting numerical data, customizing a chart, and exporting the final visualisation as an image file.

    # INSTRUCTIONS:
    # Using the provided GDP dataset:
    # Import matplotlib.pyplot correctly.
    # Create two Python lists:
    # - years
    # - gdp
    # Generate a line chart with:
    # - green color
    # - circular markers
    # - solid line style
    # Add:
    # - a chart title
    # - a label for the y-axis
    # Save the chart as a .png file inside an im / directory.
    # Display the chart using plt.show().

    # LEARNING GOALS:
    # After completing this task, you should understand how to:
    # create simple data visualisations in Python
    # work with lists as datasets
    # customize chart appearance
    # label charts professionally
    # export figures as image files

    # TECHNOLOGIES USED:
    # Python
    # Matplotlib

    # EXPECTED OUTPUT:
    # A professional-looking line chart visualising nominal GDP growth over time.
    print()


def Work():
    print()
    from matplotlib import pyplot as plt

    years = [1980, 1981, 1982, 1983, 1984]
    gdp = [100, 120.5, 170.9, 500, 924]

    # Chart:
    plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

    # Title:
    plt.title("GDP/YEAR - 1980-1984")

    # Label:
    plt.ylabel("Billions of €")

    # Displaying the chart:
    plt.show()


Work()
