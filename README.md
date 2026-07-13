# 🏦 FinHealth AI - MSME Financial Health Card

**AI-Powered Financial Assessment for MSMEs using Alternate Data Sources**

An intelligent credit assessment platform that evaluates the financial health of Micro, Small, and Medium Enterprises (MSMEs) using alternate digital data sources. Designed to help banks conduct rapid, data-driven credit decisions for New-to-Credit (NTC) and New-to-Bank (NTB) MSMEs.

## 🌟 Features

### Core Capabilities
- **Financial Health Score** - Comprehensive 0-100 scoring algorithm based on 5 key metrics
- **Credit Rating System** - AAA to BB credit ratings with risk classification
- **Risk Assessment** - Probability of default calculation and risk level classification
- **AI Credit Analysis** - Intelligent recommendations powered by business intelligence
- **Loan Eligibility** - Automated loan amount recommendation based on financial metrics
- **Financial Analytics** - Interactive dashboards with visualizations and insights

### Data Source Integration
✅ **GSTN** (GST Network) - Revenue tracking and tax compliance
✅ **UPI** - Digital transaction history and payment patterns
✅ **Account Aggregator (AA)** - Aggregated financial data access
✅ **EPFO** - Employee payroll and workforce verification
✅ **OCEN Ready** - Open Credit Enablement Network compatible
✅ **ULI Ready** - Unified Lending Interface compatible

## 📊 Dashboard Sections

### 1. **Executive Summary**
- Business size classification
- Business age
- Credit rating
- Risk assessment
- Key financial indicators (revenue, profit, employees, bank balance)

### 2. **Analytics Tab**
- Revenue distribution (GST vs UPI)
- Financial metrics radar chart
- Business performance metrics
- Strengths and risk indicators
- Comprehensive business assessment

### 3. **Credit Decision Tab**
- Loan underwriting decision
- Eligibility status (Approved/Conditionally Approved/Deferred)
- Recommended financial products
- Bank officer remarks
- Sanction amount recommendation

### 4. **AI Insights Tab**
- AI-powered financial assessment
- Executive summary and business snapshot
- Loan recommendation matrix
- Product eligibility status

## 🧮 Scoring Engine

### Financial Score Breakdown (Out of 100)

| Component | Max Score | Criteria |
|-----------|-----------|----------|
| **Revenue Stability** | 25 | Total revenue from GST and UPI |
| **Cash Flow** | 25 | Profit after payroll and EMI |
| **GST Compliance** | 20 | Tax filing compliance percentage |
| **Employee Stability** | 15 | Workforce size and consistency |
| **Debt Burden** | 15 | Outstanding loan to revenue ratio |

### Credit Ratings

| Score | Rating | Risk Level | Loan Eligibility |
|-------|--------|-----------|------------------|
| ≥ 90 | AAA | 🟢 Very Low | ✅ Approved |
| 80-89 | AA | 🟢 Low | ✅ Approved |
| 70-79 | A | 🟡 Moderate | ⚠️ Conditional |
| 60-69 | BBB | 🟠 Medium | ⚠️ Deferred |
| < 60 | BB | 🔴 High | ❌ Deferred |

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/adityamacto/fin_health.git
   cd fin_health
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## 📋 Usage

1. **Enter Business Details** (Sidebar)
   - Business Name
   - Business Type (Manufacturing, Retail, Restaurant, IT Services, etc.)
   - Years in Business (1-30)
   - Number of Employees (5-500)
   - Business Location

2. **Generate Financial Health Card**
   - Click the "Generate Financial Health Card" button
   - System connects to alternate data sources (simulated)
   - Financial analysis is performed

3. **Review Results**
   - View executive summary
   - Analyze financial metrics
   - Review detailed analytics
   - Get credit decision and recommendations

## 🛠️ Project Structure

```
fin_health/
├── app.py                    # Main Streamlit application
├── score_engine.py           # Financial scoring algorithm
├── ai_recommendation.py      # AI recommendation engine
├── charts.py                 # Data visualization components
├── mock_data.py              # Mock financial data generator
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

### File Descriptions

- **app.py** - Main Streamlit application with UI/UX, handles business input and displays results
- **score_engine.py** - Calculates financial health score based on 5-factor model
- **ai_recommendation.py** - Generates AI-powered financial assessment and recommendations
- **charts.py** - Creates interactive Plotly visualizations (gauge, pie, radar charts)
- **mock_data.py** - Generates realistic mock financial data based on business type and parameters

## 📦 Dependencies

```
streamlit          # Web application framework
plotly             # Interactive data visualization
pandas             # Data manipulation
numpy              # Numerical computing
```

## 💡 Key Algorithms

### 1. Financial Health Score
Multi-factor scoring model that weights:
- Revenue stability and consistency
- Profitability and cash flow generation
- Tax compliance (GST)
- Workforce stability
- Debt management (debt-to-revenue ratio)

### 2. Probability of Default (PD)
```
PD = (100 - Score) × 0.35
```

### 3. Loan Eligibility Amount
```
Recommended Loan = Total Monthly Revenue × 0.60
```

## 🎯 Use Cases

### For Banks
- Rapid credit assessment for MSMEs
- Data-driven lending decisions
- Reduced manual verification time
- Digital-first credit evaluation

### For MSMEs
- Quick credit eligibility assessment
- Financial health benchmarking
- Product recommendations
- Risk awareness

## 🔐 Data Privacy

This prototype version uses mock data for demonstration. In production deployment:
- Data will be fetched from actual GSTN, UPI, AA, and EPFO APIs
- All personal and financial data will be encrypted
- Compliance with RBI and data protection regulations
- Secure authentication and authorization mechanisms

## 🏆 Innovation Highlights

✔ **Alternate Data-Based Assessment** - Leverages GST, UPI, EPFO instead of traditional credit history
✔ **Real-Time Evaluation** - Near real-time credit scoring
✔ **AI-Assisted Underwriting** - Intelligent recommendations and insights
✔ **Risk Classification** - Automated risk categorization
✔ **MSME Focused** - Designed specifically for small business needs
✔ **Digital Ecosystem Ready** - Compatible with OCEN and ULI standards

## 🎓 Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Visualization**: Plotly (Interactive charts)
- **Data Processing**: Pandas, NumPy
- **Scoring Engine**: Custom Python algorithm
- **AI Recommendation**: Rule-based intelligence system

## 📈 Performance Metrics

- Financial Health Score Range: 0-100
- Processing Time: < 2 seconds per evaluation
- Supported Business Types: 8 categories
- Credit Rating Categories: 5 tiers
- Risk Levels: 5 classifications

## 🔄 API Integration Ready

The platform is designed to integrate with:
- **GSTN API** - For GST return data
- **RBI Account Aggregator** - For financial account data
- **UPI Data** - For transaction history
- **EPFO API** - For employee records
- **OCEN/ULI** - For loan disbursement workflows

## 📝 Sample Business Types

- Manufacturing
- Retail
- Restaurant
- IT Services
- Healthcare
- Wholesale
- Textile
- Construction

## 🐛 Known Limitations

1. **Mock Data** - Current version uses simulated financial data
2. **Single User** - Prototype designed for single-user demonstration
3. **No Data Persistence** - Results are not saved between sessions
4. **Simplified Scoring** - Production would include additional factors
5. **No Multi-Language** - Currently English only

## 🚧 Future Enhancements

- [ ] Real API integration with GSTN, UPI, AA, EPFO
- [ ] User authentication and account management
- [ ] Historical trend analysis
- [ ] Batch credit assessment
- [ ] Mobile application
- [ ] Multi-language support
- [ ] Advanced ML-based scoring
- [ ] Portfolio management dashboard

## 📄 License

This project was developed as a prototype submission. Please check with the repository owner for licensing details.

## 👥 Contributors

**Aditya** - Original Developer

Developed for **IDBI Bank Hackathon**

## 📞 Support & Feedback

For issues, suggestions, or questions, please open a GitHub issue or contact the development team.

## 🔗 Related Standards & Initiatives

- **OCEN** (Open Credit Enablement Network) - RBI's credit delivery platform
- **ULI** (Unified Lending Interface) - Standardized lending interface
- **AA** (Account Aggregator) - RBI's financial data aggregation framework
- **GSTN** - India's GST network
- **EPFO** - Employees' Provident Fund Organisation

---

### 📅 Version Information

**Current Version**: 1.0 (Prototype)  
**Last Updated**: 2026  
**Status**: Active Development

© 2026 FinHealth AI - Powered by Alternate Data Intelligence
