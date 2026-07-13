def generate_ai_recommendation(
    business_name,
    business_type,
    revenue,
    loan,
    employees,
    score,
):

    if score >= 90:

        return f"""
## 🟢 AI Financial Assessment

**Business:** {business_name}

The enterprise demonstrates outstanding financial health with excellent revenue stability and low financial risk.

### Strengths
- Strong GST transaction history
- Healthy digital payment ecosystem
- Stable workforce
- Excellent repayment capability

### Credit Recommendation
Eligible for higher working capital limits and term loans.

### Suggested Products
- MSME Working Capital Loan
- Machinery Loan
- Business Expansion Loan

### Risk Level
🟢 Low Risk
"""

    elif score >= 75:

        return f"""
## 🟡 AI Financial Assessment

The enterprise is financially healthy with stable business operations.

### Strengths
- Good revenue consistency
- Satisfactory GST compliance
- Moderate debt burden

### Areas for Improvement
- Improve cash reserves
- Increase average account balance
- Reduce outstanding liabilities

### Credit Recommendation
Eligible for MSME business loans after standard verification.

### Risk Level
🟡 Moderate Risk
"""

    elif score >= 55:

        return f"""
## 🟠 AI Financial Assessment

The business has moderate financial health.

### Observations
- Revenue is acceptable
- Cash flow fluctuations observed
- Debt ratio is relatively high

### Suggestions
- Improve digital transaction volume
- Maintain better liquidity
- Reduce EMI burden

### Credit Recommendation
Recommend smaller working capital loans with monitoring.

### Risk Level
🟠 Medium Risk
"""

    else:

        return f"""
## 🔴 AI Financial Assessment

The enterprise currently shows weak financial indicators.

### Issues Identified
- High debt burden
- Weak cash flow
- Limited repayment capacity

### Suggestions
- Improve GST turnover
- Increase digital transactions
- Strengthen financial discipline

### Credit Recommendation
Loan approval is not recommended until financial health improves.

### Risk Level
🔴 High Risk
"""