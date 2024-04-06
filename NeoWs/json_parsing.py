import json
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, FloatType, LongType, \
    DoubleType, BooleanType


def parse_neo_feed(feed_as_json, spark):
    schema = StructType([
        StructField('ID',
                    StringType(), True),
        StructField('Name',
                    IntegerType(), True),
        StructField('Date',
                    DateType(), True),
        StructField('ts',
                    StringType(), True),
        StructField('orbiting body',
                    StringType(), True),
        StructField('hazardous asteroid',
                    BooleanType(), True),
        StructField('miss distance (km)',
                    StringType(), True),
        StructField('speed (km/s)',
                    FloatType(), True),
        StructField('min estimated size (km)',
                    DoubleType(), True),
        StructField('max estimated size (km)',
                    DoubleType(), True),
        StructField('absolute magnitude',
                    DoubleType(), True)
    ])

    final_df = spark.createDataFrame([], schema=schema)
    near_earth_objects: dict = feed_as_json.get("near_earth_objects")
    for date, list_of_objects in near_earth_objects.items():
        for space_object in list_of_objects:
            space_object_json = json.dumps(space_object)
            df = spark.read.json(spark.sparkContext.parallelize([space_object_json]))
            selected_df = df.select(
                df.id.alias("ID"),
                df.name.alias("Name"),
                df.close_approach_data.close_approach_date[0].astype(DateType()).alias("Date"),
                df.close_approach_data.epoch_date_close_approach[0].astype(StringType()).alias("ts"),
                df.close_approach_data.orbiting_body[0].astype(StringType()).alias("orbiting body"),
                df.is_potentially_hazardous_asteroid.alias("hazardous asteroid"),
                df.close_approach_data.miss_distance.kilometers[0].astype(StringType()).alias("miss distance (km)"),
                df.close_approach_data.relative_velocity.kilometers_per_second[0].astype(FloatType()).alias("speed (km/s)"),
                df.estimated_diameter.kilometers.estimated_diameter_min.alias("min estimated size"),
                df.estimated_diameter.kilometers.estimated_diameter_max.alias("max estimated size"),
                df.absolute_magnitude_h.alias("absolute magnitude")
            )
            final_df = final_df.union(selected_df)

    return final_df



