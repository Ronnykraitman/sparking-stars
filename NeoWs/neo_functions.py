from pyspark.sql import DataFrame
from pyspark.sql.functions import col, max as pyspark_max, min as pyspark_min, avg


def _get_hazardous_objects(df: DataFrame):
    return df.filter(col("hazardous asteroid") == True)


def _get_highest_value_object(df: DataFrame, col_name: str):
    max_value = df.agg(pyspark_max(col_name)).collect()[0][0]
    return df.filter(col(col_name) == max_value)


def _get_lowest_value_object(df: DataFrame, col_name: str):
    min_value = df.agg(pyspark_min(col_name)).collect()[0][0]
    return df.filter(col(col_name) == min_value)


def _get_objects_in_between_values(df: DataFrame, col_name: str):
    min_speed = input(f"Please enter the min {col_name}: ")
    max_speed = input(f"Please enter the max {col_name}: ")
    return df.filter(col(col_name).between(min_speed, max_speed))


def _sort_by(df: DataFrame, col_name: str, asc=True):
    return df.sort(col(col_name), ascending=asc)


def _get_elements_count(df: DataFrame):
    return df.count()


def _get_avg_by_col(df: DataFrame, col_name: str):
    return df.agg(avg(col_name)).collect()[0][0]


def _get_below_or_above_avg_by_col(df: DataFrame, col_name: str, above=True, avg_value=None):
    if not avg_value:
        avg_value = _get_avg_by_col(df, col_name)

    return df.filter(col(col_name) > avg_value) if above else df.filter(col(col_name) < avg_value)
