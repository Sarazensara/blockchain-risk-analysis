import matplotlib.pyplot as plt

def plot_bar_chart(frequencies, title='Bar Chart', xlabel='Categories', ylabel='Frequency'):
    plt.figure(figsize=(12, 6))
    frequencies.sort_values(ascending=False).plot(kind='bar', color='skyblue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def plot_risk_frequencies(frequencies):
    plot_bar_chart(
        frequencies,
        title='Frequency of True Values for Each Risk Tag',
        xlabel='Risk Tags',
        ylabel='Frequency of True'
    )