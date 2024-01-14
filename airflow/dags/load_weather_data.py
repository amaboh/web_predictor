import requests
import datetime
import json
import os

from dotenv import load_dotenv
from google.cloud.storage.client import Client as storage_client 
from google.cloud.bigquery.client import Client as bigquery_client 
from google.cloud.exceptions import Conflict

import pandas as pd
from xgboost import XGBRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from helper.weather import WeatherPipline

import os
import sys
load_dotenv()
WORK_DIR = os.environ["WORK_DIR"]
sys.path.append(f"{WORK_DIR}/airflow")



PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")
path_to_local_home = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")

STORAGE_CLIENT = storage_client()
BIGQUERY_CLIENT = bigquery_client()
CURRENT_DATE = datetime.datetime.now().strftime("%Y-%m-%d").replace("-","_")


locations = ["London", "Tokyo", "Sydney", "Paris", "Berlin", "Moscow", "Madrid", "Rome", "Cairo"]
weather = WeatherPipline(locations)

default_args = {
    'owner': 'airflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id = 'load_weather_data',
    default_args=default_args, 
    start_date = datetime(2023,7,20), 
    schedule_interval='@hourly', 
    catchup=False
) as dag:

    # Task #1 - Extract data
    @task
    def extract_weather_data():
        weather.extract_weather_data()

    # Task #2 - load_to_cloudStorage
    @task
    def load_to_cloudStorage():
        weather.load_to_cloudStorage()

    # Task #3 - load_to_bigquery
    @task
    def load_to_bigquery(dataset_name, table_name):
        df = weather.process_data()
        weather.load_to_bigquery(df, dataset_name, table_name)


    # Dependencies
    extract_weather_data() >> load_to_cloudStorage() >> load_to_bigquery("weather", "weather")