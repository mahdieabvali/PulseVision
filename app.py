import streamlit as st
from src.data_loader import load_historical_data, SECTOR_TICKERS
from src.data_processor import calculate_financial_metrics
import matplotlib.pyplot as plt
import seaborn as sns # Added import for consistent heatmap generation

# Main page configuration
st.set_page_config(page_title='Market Pulse Analysis', layout='wide')

st.title('📈 Market Pulse: Financial Market Analysis')
st.markdown('Explore stock performance, risk profiles, and correlations across different market sectors.')

# User inputs in the sidebar
with st.sidebar:
    st.header("Analysis Settings")
    sector_options = list(SECTOR_TICKERS.keys())
    selected_sector = st.selectbox('Select Market Sector:', sector_options)
    
    # Using st.text_input for date inputs
    start_date = st.text_input('Start Date (YYYY-MM-DD)', '2022-01-01')
    end_date = st.text_input('End Date (YYYY-MM-DD)', '2024-12-31')
    
    run_button = st.button('Run Analysis')

if run_button:
    tickers = SECTOR_TICKERS.get(selected_sector)
    
    if not tickers:
        st.error(f"Error: Tickers list is empty for sector {selected_sector}")
        st.stop()
        
    # Data loading and processing
    # Calls functions from src/data_loader and src/data_processor (Criteria 3, 4, 5)
    with st.spinner('Fetching and processing data...'):
        price_data = load_historical_data(tickers, start_date, end_date)
        
        if price_data.empty:
            st.error("Could not load financial data. Check dates or network connection.")
            st.stop()
            
        analysis_results = calculate_financial_metrics(price_data)
        volatility_df = analysis_results['volatility']
        correlation_df = analysis_results['correlation']
        
    st.success("Data analysis complete!")

    # Displaying results (Criterion 6)
    st.header(f"Results for {selected_sector} Sector")
    
    # 1. Historical Price Trend (Visualization - Criterion 6)
    st.subheader("1. Historical Price Trend")
    st.line_chart(price_data) 

    # 2. Volatility and Risk (Scientific Computing - Criterion 5)
    st.subheader("2. Annualized Volatility (Risk Profile)")
    st.dataframe(volatility_df)
    
    # 3. Correlation Heatmap (Visualization - Criterion 6)
    st.subheader("3. Stock Correlation Heatmap")
    
    # Using pyplot for Streamlit display
    fig_corr, ax_corr = plt.subplots(figsize=(8, 7))
    # Using seaborn for the heatmap (Criterion 6)
    sns.heatmap(correlation_df, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, ax=ax_corr)
    ax_corr.set_title(f'{selected_sector} Correlation Heatmap')
    st.pyplot(fig_corr)

# How to run the Streamlit app:
# In the terminal, navigate to the main project folder and execute:
# streamlit run app.py