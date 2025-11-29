
from src.data_loader import load_historical_data, SECTOR_TICKERS
from src.data_processor import calculate_financial_metrics
from src.visualizer import plot_correlation_heatmap, plot_annual_volatility

def main():
    """
    Function: The entry point and execution sequence for the Market Pulse analysis.
    """
    # Input Settings
    sector = "Technology" # You can change this to "Finance" or "Energy"
    tickers = SECTOR_TICKERS.get(sector)
    start_date = "2022-01-01"
    end_date = "2024-12-31"

    if not tickers:
        print(f"Error: No tickers found for sector {sector}")
        return

    # Step 1: Data Loading (Criterion 3)
    price_data = load_historical_data(tickers, start_date, end_date)
    
    if price_data.empty:
        print("Analysis stopped due to data loading failure.")
        return

    # Step 2: Data Manipulation and Scientific Computing (Criteria 4 & 5)
    analysis_results = calculate_financial_metrics(price_data)
    
    volatility_df = analysis_results['volatility']
    correlation_df = analysis_results['correlation']
    
    print("\n--- Summary Results ---")
    print("Annualized Volatility (Risk):\n", volatility_df)

    # Step 3: Visualization (Criterion 6)
    plot_correlation_heatmap(correlation_df, sector)
    plot_annual_volatility(volatility_df, sector)
    
    print("\nAnalysis Complete. Check the 'data/' folder for output files and plots.")


if __name__ == '__main__':
    main()