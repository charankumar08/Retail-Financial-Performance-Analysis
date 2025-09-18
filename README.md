Retail Financial Performance Analysis using Python
Project Overview
This project performs an in-depth financial analysis of a retail stores dataset. The primary objective is to identify key performance indicators, uncover sales trends, and provide actionable insights for business growth. The analysis is framed as a performance review for a network of distributors for a major FMCG company like Nestlé India, showcasing how raw data can be transformed into strategic business intelligence.

Dataset
The dataset used for this analysis is the "Indian Stores Pincode Area and Sales Data" sourced from Kaggle. It contains transactional data for 896 retail stores, including store area, items available, daily customer count, and total sales.

Tech Stack
Language: Python

Libraries:

Pandas: For data loading, cleaning, and manipulation.

Matplotlib & Seaborn: For data visualization and generating insightful plots.

Project Workflow
1. Data Loading and Cleaning
The project began by loading the Stores.csv dataset into a Pandas DataFrame. The column names were standardized (e.g., removing spaces) to ensure easy access and manipulation throughout the analysis. A preliminary check confirmed that the dataset was clean with no missing values.

2. Feature Engineering
To enable a deeper financial analysis, new metrics were engineered from the existing data based on logical business assumptions:

A Profit column was created by assuming a uniform 15% profit margin on Store_Sales. This allows for a profitability analysis of each store.

A Sales per Customer metric was calculated (Store_Sales / Daily_Customer_Count) to measure the average transaction value and efficiency of each store.

3. Exploratory Data Analysis (EDA) and Visualization
A series of visualizations were created to answer key business questions and uncover patterns in the data.

Insight 1: Top 10 Most Profitable Stores
A bar chart was generated to identify the top 10 stores contributing the most to the company's profit. This helps in recognizing and focusing on high-value partners.
(Ikkada top_10_profitable_stores.png image ni insert chey)

Insight 2: Relationship between Store Area and Sales
A scatter plot was used to analyze the correlation between the physical size of a store (Store_Area) and its sales performance. This helps in understanding whether investing in larger-format stores is a viable strategy for revenue growth.
(Ikkada area_vs_sales.png image ni insert chey)

Insight 3: Relationship between Product Variety and Sales
Another scatter plot was created to explore the link between the number of items available in a store (Items_Available) and its total sales. This provides insights into inventory and product assortment strategies.
(Ikkada items_vs_sales.png image ni insert chey)

Key Findings & Business Recommendations
Finding: A small subset of stores (the top 10) accounts for a significant portion of the total profit.

Recommendation: The business should create strategic partnerships with these top-performing stores, potentially offering them better margins or marketing support to further boost growth.

Finding: The analysis revealed a moderate positive correlation between store area and sales, but many smaller stores also demonstrated high sales figures.

Recommendation: This indicates that store size is not the only driver of success. The business should conduct further analysis to identify the success factors of high-performing small stores and replicate those strategies across the network.

Finding: The number of items available shows a stronger correlation with sales than store area.

Recommendation: Focusing on optimizing product assortment and ensuring high-demand items are always in stock could be a more effective strategy than simply increasing store size.
