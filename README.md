# Automated Trade Data Accuracy & Operations Monitoring System

## Project Overview
This project simulates a Core Tech / Front Office trade monitoring system used in financial firms to ensure trade data accuracy, operational reliability, and system health visibility.
It processes mock trade data using Python, identifies data quality issues, generates operational metrics, and visualizes insights using Power BI dashboards.
This project aligns with Core Tech Associate, Front Office Support, and Operations roles in quantitative finance firms.

---

## Key Objectives
- Validate trade data for accuracy and consistency
- Detect operational and data-quality errors
- Generate clean datasets and structured error logs
- Compute KPIs for system health monitoring
- Visualize insights using professional dashboards

---

## Tech Stack
- Python (Pandas, NumPy)
- Power BI
- CSV-based data pipelines
- GitHub for version control

---

## Project Structure
Automated-Trade-Data-Accuracy-Operations-Monitoring/

├── trade_validation.py  
├── README.md  

├── data/  
│   ├── mock_trade_data.csv  
│   ├── clean_trades.csv  
│   ├── error_log.csv  
│   └── metrics_summary.csv  

├── Dashboard/  
│   ├── system_health_overview.png  
│   ├── operational_error_analysis.png  
│   └── trade_operations_overview.png  

---

## Data Validation Logic
The Python script performs the following checks:
- Missing trade prices
- Duplicate Trade IDs
- Invalid trade quantities
- Invalid trade statuses

### Outputs Generated
- Clean trades dataset
- Error log with error-type classification
- Metrics summary for KPI reporting

---

## Power BI Dashboards

### System Health Overview
- Total Trades
- Clean Trades
- Error Records
- Data Accuracy (%)

### Operational Error Analysis
- Error count by error type
- Detailed error-level records

### Trade Operations Overview
- Trades by instrument
- Trade status distribution
- Trade volume trends over time

Dashboard screenshots are available in the Dashboard folder.

---

##  How to Run the Project
1. Clone or download the repository
2. Ensure Python is installed
3. Run the script:
   python trade_validation.py
4. Open Power BI Desktop
5. Load CSV files from the data folder
6. Explore the dashboards

---

##  Key Learnings
- End-to-end trade data validation
- Operational monitoring using KPIs
- Error classification and logging
- Python and Power BI integration
- Financial operations workflow simulation

---

