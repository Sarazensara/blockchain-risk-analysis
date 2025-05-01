import matplotlib.pyplot as plt

# Function to plot a bar chart of risk frequencies
def plot_bar_chart(frequencies, title='Bar Chart', xlabel='Categories', ylabel='Frequency'):
    """
    Plots a bar chart for the given frequencies.

    Parameters:
    - frequencies (pd.Series): A Pandas Series containing the frequency of risk tags.
    - title (str): Title of the chart (default is 'Bar Chart').
    - xlabel (str): Label for the x-axis (default is 'Categories').
    - ylabel (str): Label for the y-axis (default is 'Frequency').
    """
    # Create a new figure with the specified size
    plt.figure(figsize=(12, 6))
    
    # Sort the frequencies in descending order and plot the bar chart
    frequencies.sort_values(ascending=False).plot(kind='bar', color='skyblue')
    
    # Set chart title and axis labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=90)
    
    # Ensure the layout fits into the figure area
    plt.tight_layout()
    
    # Add grid lines to the y-axis for better visualization
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Display the chart
    plt.show()

# Function to plot the frequency of True values for each risk tag
def plot_risk_frequencies(frequencies):
    """
    Creates a specific bar chart showing the frequency of 'True' values for each risk tag.

    Parameters:
    - frequencies (pd.Series): A Pandas Series containing the frequency of risk tags.
    """
    # Call the plot_bar_chart function with specific title and axis labels
    plot_bar_chart(
        frequencies,
        title='Frequency of True Values for Each Risk Tag',
        xlabel='Risk Tags',
        ylabel='Frequency of True'
    )