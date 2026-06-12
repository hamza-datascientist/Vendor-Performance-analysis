🥃 Vendor Performance Analysis
Transforming raw liquor retail data into actionable business intelligence.

📌 Problem Statement
A liquor retail company had no visibility into which vendors were profitable, which products were slow-moving, and whether bulk purchasing actually reduced costs. This project answers all of that — with data.

🔍 Key Business Insights
FindingInsight📦 Top 10 vendorsDrive 66% of total purchases → supply chain risk💰 Bulk purchasingReduces unit cost by ~72%📊 Low-volume vendorsHave higher margins (40-42%) vs top vendors (30-31%)✅ Hypothesis Testp < 0.05 → margin difference is statistically significant

🛠️ Tech Stack
Python Pandas SQL SQLite SQLAlchemy Matplotlib Seaborn.

🗂️ Project Structure
vendor-performance-analysis/
│
├── data/                          # 6 raw CSV files
├── ingestion_db.py                # Data pipeline — CSV to SQLite
├── exploratory data analysis.ipynb  # EDA + Hypothesis Testing
├── vendor performance analysis.ipynb # SQL CTEs + Business Q&A
├── vendor_dashboard.html          # Interactive JS Dashboard
└── README.md

Built a unified vendor_sales_summary table using 3 nested CTEs merging purchase, sales, freight & pricing data across 50+ vendors.

**EDA & Hypothesis Testing**

Outlier detection, distribution analysis, correlation heatmaps
t-test to validate margin difference between vendor tiers

**Interactive Dashboard**

Zero-dependency HTML dashboard with live filters, KPI cards, scatter quadrant analysis & bar charts.

📊 Live Dashboard
🔗 View Live Dashboard

💡 **Business Questions Answered**

Which vendors contribute the most to gross profit?
Does bulk purchasing significantly reduce unit cost?
Which brands are Stars, Cash Cows, Niche, or Dogs?
Which vendors have slow-moving / unsold inventory?
Is the profit margin difference between vendor tiers statistically significant?


👤 Author
Hamza — Aspiring Data Analyst
Built with Python, SQL, and an analytical mindset. Data doesn't lie — you just have to ask the right questions.
