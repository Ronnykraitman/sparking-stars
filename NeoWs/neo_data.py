from NeoWs.json_parsing import parse_neo_feed
from NeoWs.neo_functions import _get_hazardous_objects, _get_lowest_value_object, _get_highest_value_object
from NeoWs.py_spark_builder import get_spark_session
from NeoWs.rest_api import get_neo_data_by_dates
from pyspark.sql import DataFrame

spark = get_spark_session()


def get_neo_feed():
    data = get_neo_data_by_dates()
    feed = parse_neo_feed(data, spark)
    return feed


def get_dangerous_asteroids(df: DataFrame):
    df_filtered = _get_hazardous_objects(df)
    df_filtered.show()


def get_closest_asteroid(df: DataFrame):
    df_filtered = _get_lowest_value_object(df, "miss distance (km)", spark)
    df_filtered.show()


def get_fastest_asteroid(df: DataFrame):
    df_filtered = _get_highest_value_object(df, "speed (km/s)", spark)
    df_filtered.show()
