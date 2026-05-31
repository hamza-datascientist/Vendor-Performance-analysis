import pandas as pd
import sqlite3
import logging
from ingestion_db import ingest_db


logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    filemode='a'
)

def create_vendor_summary(conn):
    '''this function will merge the diffrent tables to get overall vendor summary and add new column in the resultant data'''
    vendor_sales_summary = pd.read_sql_query("""
WITH FreightSummary as(
    SELECT
        VendorNumber,
        SUM(Freight) as FreightCost from vendor_invoice
        group by VendorNumber),
        
PurchaseSummary as (
    SELECT
        p.VendorNumber,
        p.VendorName,
        p.Brand,
        p.Description,
        p.PurchasePrice,
        pp.Price as ActualPrice,
        pp.Volume,
        SUM(p.Quantity) as TotalPurchaseQuantity,
        SUM(p.Dollars) as TotalPurchaseDollars
    from purchases as p
    join purchase_prices as pp
        on p.Brand = pp.Brand
    where p.PurchasePrice>0
group by p.VendorNumber, p.VendorName, p.Brand,p.Description, p.PurchasePrice,pp.Price,pp.Volume
),

SalesSummary as (
    SELECT
        VendorNo,
        Brand,
        SUM(SalesQuantity) as TotalSalesQuantity,
        SUM(SalesDollars) as TotalSalesDollars,
        SUM(SalesPrice) as TotalSalesPrice,
        SUM(ExciseTax) as TotalExciseTax
    from sales as s
    group by VendorNo,Brand)

SELECT
        PS.VendorNumber,
        PS.VendorName,
        PS.Brand,
        PS.Description,
        PS.PurchasePrice,
        PS.ActualPrice,
        PS.Volume,
        PS.TotalPurchaseQuantity,
        PS.TotalPurchaseDollars,
        SS.TotalSalesQuantity,
        SS.TotalSalesDollars,
        SS.TotalSalesPrice,
        SS.TotalExciseTax,
        FS.FreightCost
from PurchaseSummary as PS
    LEFT JOIN SalesSummary as SS
        on PS.VendorNumber = SS.VendorNo
            and PS.Brand = SS.Brand
    LEFT JOIN FreightSummary as FS
        on PS.VendorNumber = FS.VendorNumber
    order by PS.TotalPurchaseDollars DESC""",conn)

    return vendor_sales_summary

def clean_data(df):
    '''This function will clean the data'''

    #changing datatype to float
    df['Volume']= df['Volume'].astype('float64')

    #filling missing value with 0
    df.fillna(0,inplace=True)

    #removing space from categorical columns
    df['VendorName'] = df['VendorName'].str.strip()
    df['VendorName'] = df['VendorName'].str.strip()


    #creating new columns for better analysis
    df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
    df['ProfitMargine'] = (df['GrossProfit']/df['TotalSalesDollars'])*100
    df['StockTurnOver'] = df['TotalSalesQuantity'] / df['TotalPurchaseQuantity']
    df['StockTurnOver'] = df['TotalSalesQuantity'] / df['TotalPurchaseQuantity']
    df['SalesPurchaseRatio'] = df['TotalSalesDollars'] / df['TotalPurchaseDollars']

    return df

if __name__ == '__main__':
    #ceating database connection
    conn = sqlite3.connect(r'C:\Users\hamza\OneDrive\Desktop\Name\inventory_db.db')

    logging.info("Creating Vendor Summary Table....")
    summary_df = create_vendor_summary(conn)
    logging.info(summary_df.head())

    logging.info('cleaning Data.....')
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info('Ingesting data.....')
    ingest_db(clean_df, 'vendor_sales_summary',conn)
    logging.info('Completed')