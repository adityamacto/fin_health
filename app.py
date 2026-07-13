import streamlit as st
from mock_data import generate_business_data
import time
from score_engine import calculate_score
from charts import gauge_chart, revenue_pie_chart, radar_chart
from ai_recommendation import generate_ai_recommendation

# --------------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------------

st.set_page_config(
    page_title="FinHealth AI",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------------

st.markdown("""
<style>

html, body, [class*="css"]{
    font-family: 'Segoe UI';
}

.main{
    background:#f5f8fc;
}

h1{
    color:#003366;
}

h2,h3{
    color:#003366;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:15px;
    padding:18px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.12);
    border-left:6px solid #005BAC;
}

.stButton>button{
    width:100%;
    background:#005BAC;
    color:white;
    border-radius:10px;
    height:50px;
    font-size:17px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#003366;
}

.block-container{
    padding-top:1rem;
}

</style>
""",unsafe_allow_html=True)

# --------------------------------------------------------
# HEADER
# --------------------------------------------------------

st.title("🏦 FinHealth AI")

st.markdown("""
### AI Powered MSME Financial Health Card

Leveraging Alternate Data Sources for Intelligent Credit Assessment

**Connected Ecosystem**

✅ GSTN

✅ UPI

✅ Account Aggregator (AA)

✅ EPFO

✅ OCEN Ready

✅ ULI Ready

---
""")

# --------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------

st.sidebar.image(
    "https://img.icons8.com/color/96/bank-building.png",
    width=80
)

st.sidebar.title("Loan Underwriting")

business_name = st.sidebar.text_input(
    "Business Name",
    "ABC Industries"
)

business_type = st.sidebar.selectbox(
    "Business Type",
    [
        "Manufacturing",
        "Retail",
        "Restaurant",
        "IT Services",
        "Healthcare",
        "Wholesale",
        "Textile",
        "Construction"
    ]
)

years = st.sidebar.slider(
    "Years in Business",
    1,
    30,
    5
)

employees = st.sidebar.slider(
    "Number of Employees",
    5,
    500,
    25
)

location = st.sidebar.selectbox(
    "Business Location",
    [
        "Bangalore",
        "Mumbai",
        "Delhi",
        "Hyderabad",
        "Chennai",
        "Pune",
        "Kolkata"
    ]
)

st.sidebar.markdown("---")

fetch = st.sidebar.button("Generate Financial Health Card")

# --------------------------------------------------------
# INTELLIGENT DATA GENERATOR
# --------------------------------------------------------

if fetch:

    with st.spinner("Connecting to GST Network..."):
        time.sleep(0.8)

    st.success("GST Connected")

    with st.spinner("Fetching UPI Transaction History..."):
        time.sleep(0.8)

    st.success("UPI Connected")

    with st.spinner("Connecting Account Aggregator..."):
        time.sleep(0.8)

    st.success("Account Aggregator Connected")

    with st.spinner("Reading EPFO Records..."):
        time.sleep(0.8)

    st.success("EPFO Connected")

    st.success("Alternate Data Successfully Retrieved")

    # -------------------------------------
    # BUSINESS SIZE
    # -------------------------------------

    if employees <= 15:
        company_size = "Small"

    elif employees <= 75:
        company_size = "Medium"

    else:
        company_size = "Large"

    # -------------------------------------
    # GENERATE MOCK BUSINESS DATA
    # -------------------------------------

    data = generate_business_data(
        business_type,
        employees,
        years
    )

    gst_revenue = data["gst_revenue"]
    upi_revenue = data["upi_revenue"]
    bank_balance = data["bank_balance"]
    payroll = data["payroll"]
    outstanding_loan = data["loan"]
    emi = data["emi"]
    gst_compliance = data["gst"]
    total_revenue = data["total_revenue"]
    company_size = data["size"]

    monthly_profit = total_revenue - payroll - emi
    # --------------------------------------------------------
    # CALCULATE SCORE
    # --------------------------------------------------------

    score, breakdown = calculate_score(
        gst_revenue,
        upi_revenue,
        payroll,
        outstanding_loan,
        emi,
        gst_compliance,
        employees
    )

    # --------------------------------------------------------
    # CREDIT RATING & RISK
    # --------------------------------------------------------

    if score >= 90:
        rating = "AAA"
        risk = "🟢 Very Low"

    elif score >= 80:
        rating = "AA"
        risk = "🟢 Low"

    elif score >= 70:
        rating = "A"
        risk = "🟡 Moderate"

    elif score >= 60:
        rating = "BBB"
        risk = "🟠 Medium"

    else:
        rating = "BB"
        risk = "🔴 High"

    probability_default = round((100 - score) * 0.35, 2)

    recommended_loan = int(total_revenue * 0.60)

    # --------------------------------------------------------
    # EXECUTIVE SUMMARY
    # --------------------------------------------------------

    st.header("📊 Executive Summary")

    s1, s2, s3, s4 = st.columns(4)

    s1.metric(
        "Business Size",
        company_size
    )

    s2.metric(
        "Business Age",
        f"{years} Years"
    )

    s3.metric(
        "Credit Rating",
        rating
    )

    s4.metric(
        "Risk",
        risk
    )

    st.divider()

    # --------------------------------------------------------
    # KPI DASHBOARD
    # --------------------------------------------------------

    st.header("📈 Key Financial Indicators")

    k1, k2, k3, k4 = st.columns(4)

    k1.metric(
        "Monthly Revenue",
        f"₹{total_revenue:,}",
        "+8.6%"
    )

    k2.metric(
        "Monthly Profit",
        f"₹{monthly_profit:,}",
        "+5.2%"
    )

    k3.metric(
        "Employees",
        employees,
        "+2"
    )

    k4.metric(
        "Avg Bank Balance",
        f"₹{bank_balance:,}",
        "+12%"
    )

    st.divider()

    # --------------------------------------------------------
    # DATA SOURCE STATUS
    # --------------------------------------------------------

    st.subheader("Connected Alternate Data Sources")

    c1, c2, c3, c4 = st.columns(4)

    c1.success("✅ GSTN\n\nLast Sync: 15 sec ago")
    c2.success("✅ UPI\n\nLast Sync: 10 sec ago")
    c3.success("✅ Account Aggregator\n\nLive")
    c4.success("✅ EPFO\n\nVerified")

    st.divider()

    # --------------------------------------------------------
    # TABS
    # --------------------------------------------------------

    overview, analytics, decision, ai = st.tabs(
        [
            "📈 Overview",
            "📊 Analytics",
            "🏦 Credit Decision",
            "🤖 AI Insights"
        ]
    )

    # ========================================================
    # OVERVIEW TAB
    # ========================================================

    with overview:

        st.subheader("Financial Health Overview")

        left, right = st.columns([1, 1])

        with left:

            st.plotly_chart(
                gauge_chart(score),
                use_container_width=True
            )

        with right:

            st.metric(
                "Overall Financial Score",
                f"{score}/100"
            )

            st.metric(
                "Credit Rating",
                rating
            )

            st.metric(
                "Probability of Default",
                f"{probability_default}%"
            )

            st.metric(
                "Risk Level",
                risk
            )

            st.markdown("### Score Breakdown")

            max_scores = {
                "Revenue Stability": 25,
                "Cash Flow": 25,
                "GST Compliance": 20,
                "Employee Stability": 15,
                "Debt Burden": 15
            }

            for key, value in breakdown.items():

                st.write(
                    f"**{key} : {value}/{max_scores[key]}**"
                )

                st.progress(
                    value / max_scores[key]
                )
        # ========================================================
    # ANALYTICS TAB
    # ========================================================

    with analytics:

        st.subheader("Financial Analytics Dashboard")

        a1, a2 = st.columns(2)

        with a1:

            st.plotly_chart(
                revenue_pie_chart(
                    gst_revenue,
                    upi_revenue
                ),
                use_container_width=True
            )

        with a2:

            st.plotly_chart(
                radar_chart(
                    breakdown
                ),
                use_container_width=True
            )

        st.divider()

        st.subheader("Business Performance")

        perf1, perf2, perf3 = st.columns(3)

        perf1.metric(
            "GST Revenue",
            f"₹{gst_revenue:,}"
        )

        perf2.metric(
            "UPI Revenue",
            f"₹{upi_revenue:,}"
        )

        perf3.metric(
            "GST Compliance",
            f"{gst_compliance}%"
        )

        st.divider()

        st.subheader("Business Strengths")

        strengths = []

        if score >= 85:
            strengths.append("Excellent Financial Stability")

        if gst_compliance >= 90:
            strengths.append("Excellent GST Compliance")

        if outstanding_loan < total_revenue * 0.40:
            strengths.append("Healthy Debt Ratio")

        if employees >= 20:
            strengths.append("Stable Workforce")

        if monthly_profit > 300000:
            strengths.append("Strong Positive Cash Flow")

        if bank_balance > 300000:
            strengths.append("Healthy Average Bank Balance")

        if len(strengths) == 0:
            st.info("No major strengths detected.")

        for item in strengths:
            st.success(item)

        st.divider()

        st.subheader("Risk Indicators")

        risks = []

        if outstanding_loan > total_revenue:
            risks.append("High Outstanding Debt")

        if gst_compliance < 85:
            risks.append("GST Compliance Requires Improvement")

        if monthly_profit < 100000:
            risks.append("Weak Cash Flow")

        if employees < 10:
            risks.append("Limited Workforce")

        if score < 60:
            risks.append("Overall Financial Health Needs Improvement")

        if len(risks) == 0:
            st.success("No significant financial risks identified.")

        for r in risks:
            st.warning(r)

    # ========================================================
    # CREDIT DECISION TAB
    # ========================================================

    with decision:

        st.subheader("Loan Underwriting Decision")

        d1, d2, d3 = st.columns(3)

        d1.metric(
            "Eligible Loan",
            f"₹{recommended_loan:,}"
        )

        d2.metric(
            "Credit Rating",
            rating
        )

        d3.metric(
            "Probability of Default",
            f"{probability_default}%"
        )

        st.divider()

        if score >= 85:

            st.success("""
### ✅ APPROVED

This MSME demonstrates excellent financial health based on alternate data.

### Recommended Products

• Working Capital Loan

• Machinery Finance

• Business Expansion Loan

• Cash Credit Facility
""")

        elif score >= 70:

            st.warning("""
### 🟡 CONDITIONALLY APPROVED

Business is financially stable.

Recommend standard banking verification before sanction.

### Suggested Products

• MSME Working Capital Loan

• Term Loan

• Trade Finance
""")

        else:

            st.error("""
### 🔴 APPROVAL DEFERRED

Business currently presents elevated financial risk.

### Recommendations

• Improve GST Compliance

• Increase Cash Flow

• Reduce Outstanding Debt

• Maintain Higher Average Balance
""")

        st.divider()

        st.subheader("Bank Officer Remarks")

        st.info(f"""
Business Name : {business_name}

Sector : {business_type}

Business Age : {years} Years

Location : {location}

Employees : {employees}

Overall assessment indicates a **{risk}** profile with a credit rating of **{rating}**.

Recommended sanction amount: **₹{recommended_loan:,}**

This recommendation is generated using alternate digital data including GST, UPI, EPFO and Account Aggregator records.
""")
        # ========================================================
    # AI INSIGHTS TAB
    # ========================================================

    with ai:

        st.subheader("🤖 AI Credit Assessment Engine")

        recommendation = generate_ai_recommendation(
            business_name,
            business_type,
            total_revenue,
            outstanding_loan,
            employees,
            score
        )

        st.markdown(recommendation)

        st.divider()

        st.subheader("Executive Financial Summary")

        summary = f"""
### Business Snapshot

| Parameter | Value |
|-----------|-------|
| Business Name | {business_name} |
| Sector | {business_type} |
| Business Age | {years} Years |
| Employees | {employees} |
| Location | {location} |
| Monthly Revenue | ₹{total_revenue:,} |
| Outstanding Loan | ₹{outstanding_loan:,} |
| Financial Health Score | {score}/100 |
| Credit Rating | {rating} |
| Risk Category | {risk} |

---

### AI Summary

The business demonstrates a **{risk}** risk profile with a
financial health score of **{score}/100**.

Revenue consistency, GST compliance,
cash flow behaviour and debt burden were
evaluated using alternate financial indicators.

The underwriting engine estimates a recommended
credit exposure of **₹{recommended_loan:,}**.

The enterprise appears suitable for MSME
credit products subject to banking norms.
"""

        st.markdown(summary)

        st.divider()

        st.subheader("Loan Recommendation Matrix")

        matrix = {
            "Working Capital Loan": "✅ Eligible" if score >= 70 else "⚠ Review",
            "Machinery Loan": "✅ Eligible" if score >= 80 else "⚠ Review",
            "Business Expansion": "✅ Eligible" if score >= 85 else "❌ Not Recommended",
            "Cash Credit": "✅ Eligible" if score >= 75 else "⚠ Review",
            "Overdraft": "✅ Eligible" if score >= 65 else "❌ Not Recommended",
        }

        for loan_type, status in matrix.items():
            st.write(f"**{loan_type}** : {status}")

    # ========================================================
    # FINAL DASHBOARD
    # ========================================================

    st.divider()

    st.header("🏦 Final Credit Decision Dashboard")

    f1, f2, f3, f4 = st.columns(4)

    f1.metric(
        "Financial Score",
        f"{score}/100"
    )

    f2.metric(
        "Credit Rating",
        rating
    )

    f3.metric(
        "Risk",
        risk
    )

    f4.metric(
        "Loan Eligibility",
        f"₹{recommended_loan:,}"
    )

    st.divider()

    st.success("✔ Alternate Data Sources Successfully Verified")

    s1, s2, s3, s4 = st.columns(4)

    s1.success("GST Network")
    s2.success("UPI")
    s3.success("Account Aggregator")
    s4.success("EPFO")

    st.divider()

    st.info("""
### Innovation Highlights

✔ Alternate Data Based Credit Assessment

✔ Financial Health Score Engine

✔ Intelligent Risk Classification

✔ MSME Credit Recommendation

✔ AI Assisted Underwriting

✔ Near Real-Time Credit Evaluation

✔ Ready for OCEN / ULI / AA Integration
""")

    st.divider()

    st.caption(
        """
© 2026 FinHealth AI

Developed for IDBI Bank Hackathon

AI Powered MSME Financial Health Card

Prototype Version 1.0
"""
    )

# ========================================================
# HOME SCREEN
# ========================================================

else:

    st.markdown("""
# 👋 Welcome to FinHealth AI

## AI Powered MSME Financial Health Card

This solution helps banks evaluate
New-to-Credit (NTC) and New-to-Bank (NTB)
MSMEs using Alternate Data Sources.

### Data Sources

- GST Network
- UPI Transactions
- Account Aggregator
- EPFO
- OCEN Ready
- ULI Ready

---

### Features

- Financial Health Score
- Risk Classification
- Credit Rating
- Probability of Default
- AI Credit Assessment
- Loan Recommendation
- Financial Analytics Dashboard

---

👈 Enter business details from the sidebar and click

## **Generate Financial Health Card**
""")