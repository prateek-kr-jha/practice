from analyzer import StockAnalyzer

def main():
    # Initialize analyzer
    analyzer = StockAnalyzer('RELIANCE.NS')
    
    # Perform analysis
    analyzer.fetch_data('2023-01-01', '2024-01-01')
    analyzer.calculate_indicators()
    analyzer.generate_signals()
    
    # Display results
    analyzer.plot_analysis()

if __name__ == "__main__":
    main()