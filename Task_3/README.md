# Comprehensive Financial Loan Analysis & Risk Assessment

## Executive Summary
This project delivers an end-to-end Exploratory Data Analysis (EDA) on retail financial loan data (`38,576` records across `24` features). The core objective is to analyze portfolio performance, establish underwriting benchmarks, examine risk drivers behind loan defaults (**Charged Off** status), and provide strategic recommendations to mitigate credit loss while optimizing lending operations.

---

## Author & Project Metadata

* **Author:** Aditya Sharma
* **Role:** Data Analytics Intern
* **Deliverable:** Financial Data Analysis & Risk Modeling Report

---

## Key Highlights & Analytical Insights

* **Portfolio Health Distribution:**
  * **Good Loans (Fully Paid / Current):** **86.2%** of the portfolio.
  * **Bad Loans (Charged Off):** **13.8%** of the portfolio, signaling a moderate-to-high credit risk profile compared to conventional retail banking benchmarks.
* **Loan Amount Distribution:**
  * Borrowing predominantly clusters around psychological round figures (**$5,000**, **$10,000**, and **$15,000**), with core density centered between **$10,000** and **$12,000**.
  * Large loans (**$30,000+**) account for a marginal fraction of volume.
* **Credit Grade vs. Default Risk:**
  * A direct monotonic relationship exists between credit grade deterioration and default probability.
  * **Grade A** loans exhibit the lowest default rate at **~6.0%**.
  * Risk escalates sharply through subprime tiers: **Grade E (~27.2%)**, **Grade F (~32.7%)**, and **Grade G (~33.8%)**.
* **Primary Loan Drivers:**
  * **Debt Consolidation** is the primary driver of credit demand by a wide margin, followed by **Credit Card Refinancing**.
  * The vast majority of borrowers leverage personal loans to restructure existing, high-interest obligations.

---

## Repository Structure

```text
├── data/
│   └── financial_loan.csv        # Primary loan portfolio dataset (raw / processed)
├── notebooks/
│   └── Financial.ipynb       # Jupyter notebook containing end-to-end data pipeline & plots
├── visuals/                      # Exported visualization figures
├── README.md                     # Project documentation

