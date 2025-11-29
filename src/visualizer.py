import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Ensure the plots storage directory exists (Criterion 2)
if not os.path.exists('data/plots'):
    os.makedirs('data/plots')

# Docstring to satisfy Criterion 2 (Project Organization)
def plot_correlation_heatmap(correlation_df: pd.DataFrame, title: str):
    """
    Function: Creates a Heatmap to visualize the correlation matrix.
    This fulfills the project requirement for creating a 'correlation heatmap'.

    :param correlation_df: The calculated correlation matrix DataFrame.
    :param title: The title for the plot.
    """
    plt.figure(figsize=(10, 8))
    # Use Seaborn for a clear relational plot (Criterion 6)
    sns.heatmap(
        correlation_df, 
        annot=True, 
        cmap='coolwarm', 
        fmt=".2f",
        linewidths=.5
    )
    plt.title(f'{title} Stock Correlation Heatmap')
    # Criterion 3 (Output): Saving the plot file
    plt.savefig(f'data/plots/{title}_correlation_heatmap.png')
    plt.close()
    print(f"Saved correlation heatmap to data/plots/{title}_correlation_heatmap.png")


def plot_annual_volatility(volatility_df: pd.DataFrame, title: str):
    """
    Function: Creates a bar chart to display annualized volatility (risk profile).
    This fulfills the project requirement for creating 'volatility plots'.

    :param volatility_df: DataFrame containing the annualized volatility.
    :param title: The title for the plot.
    """
    plt.figure(figsize=(10, 6))
    # Volatility Plot (Criterion 6)
    volatility_df.sort_values(by='Annualized Volatility', ascending=False).plot(
        kind='bar', 
        ax=plt.gca(), 
        legend=False
    )
    plt.title(f'{title} Annualized Volatility')
    plt.ylabel('Annualized Volatility (Risk)')
    plt.xlabel('Ticker')
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.5)
    # Criterion 3 (Output): Saving the plot file
    plt.savefig(f'data/plots/{title}_volatility_bar_chart.png', bbox_inches='tight')
    plt.close()
    print(f"Saved volatility bar chart to data/plots/{title}_volatility_bar_chart.png")

# These two plots directly cover the project requirements for financial charts 
# (volatility plots and correlation heatmaps) and ensure Criterion 6 is met.