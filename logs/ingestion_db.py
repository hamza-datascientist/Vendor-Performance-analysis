import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename = 'logs/ingestion_db.log',
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    filemode = 'a'
)

engine = create_engine('sqlite:///inventory_db.db')

def ingest_db(df, table_name, engine):
    '''This function will ingest the dataframe into Database Table'''
    df.to_sql(table_name, con=engine, if_exists='replace', index = False)
    
def load_row_data():
    '''This Function will load the CSV as DataFrame and ingest into Database'''
    start_time = time.time()
    for file in os.listdir('data'):
        if file.endswith('.csv'):
            df = pd.read_csv('data/'+file)
            logging.info(f'ingesting {file} in database')
            ingest_db(df, file[:-4], engine)
    end_time = time.time()
    total_time = (end_time - start_time) / 60
    logging.info('-------ingestion complete---------')

    logging.info(f'\nTotal Time Taken: {total_time} minute')

if __name__ == '__main__':
    load_row_data()