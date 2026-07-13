def calculate_score(
    gst_revenue,
    upi_revenue,
    payroll,
    outstanding_loan,
    emi,
    gst_compliance,
    employees
):
    """
    Returns:
        total_score (0-100)
        breakdown dictionary
    """

    breakdown = {}

    ####################################
    # 1. Revenue Stability (25)
    ####################################

    total_revenue = gst_revenue + upi_revenue

    if total_revenue >= 2000000:
        revenue_score = 25
    elif total_revenue >= 1500000:
        revenue_score = 22
    elif total_revenue >= 1000000:
        revenue_score = 18
    elif total_revenue >= 700000:
        revenue_score = 14
    else:
        revenue_score = 8

    breakdown["Revenue Stability"] = revenue_score

    ####################################
    # 2. Cash Flow (25)
    ####################################

    profit = total_revenue - payroll - emi

    if profit >= 1000000:
        cashflow_score = 25
    elif profit >= 700000:
        cashflow_score = 21
    elif profit >= 400000:
        cashflow_score = 17
    elif profit >= 150000:
        cashflow_score = 12
    else:
        cashflow_score = 6

    breakdown["Cash Flow"] = cashflow_score

    ####################################
    # 3. GST Compliance (20)
    ####################################

    gst_score = round((gst_compliance / 100) * 20)

    breakdown["GST Compliance"] = gst_score

    ####################################
    # 4. Employee Stability (15)
    ####################################

    if employees >= 100:
        emp_score = 15
    elif employees >= 50:
        emp_score = 13
    elif employees >= 20:
        emp_score = 10
    elif employees >= 10:
        emp_score = 7
    else:
        emp_score = 4

    breakdown["Employee Stability"] = emp_score

    ####################################
    # 5. Debt Burden (15)
    ####################################

    debt_ratio = outstanding_loan / total_revenue

    if debt_ratio <= 0.25:
        debt_score = 15
    elif debt_ratio <= 0.50:
        debt_score = 12
    elif debt_ratio <= 0.75:
        debt_score = 9
    elif debt_ratio <= 1:
        debt_score = 6
    else:
        debt_score = 3

    breakdown["Debt Burden"] = debt_score

    ####################################
    # Final Score
    ####################################

    total_score = sum(breakdown.values())

    return total_score, breakdown   