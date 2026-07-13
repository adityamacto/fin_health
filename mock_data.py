import random

def generate_business_data(business_type, employees, years):

    # Make output deterministic
    seed = hash(f"{business_type}-{employees}-{years}")
    random.seed(seed)

    # Business Size
    if employees <= 15:
        size = "Small"
        revenue_multiplier = 1

    elif employees <= 75:
        size = "Medium"
        revenue_multiplier = 2

    else:
        size = "Large"
        revenue_multiplier = 4

    # -----------------------------
    # Base Revenue by Industry
    # -----------------------------

    revenue_map = {

        "Manufacturing": (1200000,1800000),

        "Retail": (500000,900000),

        "Restaurant": (450000,800000),

        "IT Services": (900000,1600000),

        "Healthcare": (1300000,2000000),

        "Wholesale": (1800000,2800000),

        "Textile": (1000000,1800000),

        "Construction": (1500000,2600000)
    }

    low, high = revenue_map.get(
        business_type,
        (800000,1500000)
    )

    gst_revenue = random.randint(
        low,
        high
    ) * revenue_multiplier

    # -----------------------------
    # UPI Share
    # -----------------------------

    if business_type in ["Restaurant","Retail"]:

        upi_revenue = int(
            gst_revenue *
            random.uniform(0.45,0.70)
        )

    elif business_type=="IT Services":

        upi_revenue=int(
            gst_revenue*
            random.uniform(0.05,0.15)
        )

    else:

        upi_revenue=int(
            gst_revenue*
            random.uniform(0.10,0.25)
        )

    total_revenue=gst_revenue+upi_revenue

    # -----------------------------
    # Payroll
    # -----------------------------

    salary_map={

        "Manufacturing":28000,

        "Retail":18000,

        "Restaurant":17000,

        "IT Services":60000,

        "Healthcare":45000,

        "Wholesale":25000,

        "Textile":22000,

        "Construction":32000
    }

    avg_salary=salary_map.get(
        business_type,
        25000
    )

    payroll=int(
        employees*
        avg_salary*
        random.uniform(0.9,1.1)
    )

    # -----------------------------
    # GST Compliance
    # -----------------------------

    if years<3:

        gst=random.randint(75,88)

    elif years<7:

        gst=random.randint(85,95)

    else:

        gst=random.randint(92,100)

    # -----------------------------
    # Outstanding Loan
    # -----------------------------

    loan=int(
        total_revenue*
        random.uniform(0.18,0.55)
    )

    emi=int(
        loan/36
    )

    bank_balance=int(
        total_revenue*
        random.uniform(0.10,0.30)
    )

    return {

        "gst_revenue":gst_revenue,

        "upi_revenue":upi_revenue,

        "bank_balance":bank_balance,

        "payroll":payroll,

        "loan":loan,

        "emi":emi,

        "gst":gst,

        "total_revenue":total_revenue,

        "size":size
    }