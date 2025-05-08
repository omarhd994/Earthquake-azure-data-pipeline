# Code before Azure Implementation

from datetime import date, timedelta

# Remove this before running Data Factory Pipeline
start_date = date.today() - timedelta(1)

silver_adls = "abfss://silver@dataomar123.dfs.core.windows.net/"
gold_adls = "abfss://gold@dataomar123.dfs.core.windows.net/"

silver_data = f"{silver_adls}earthquake_events_silver/"
from pyspark.sql.functions import when, col, udf
from pyspark.sql.types import StringType
# This library has to be installed on the cluster, not using pip install...
import reverse_geocoder as rg
from datetime import date, timedelta
df = spark.read.parquet(silver_data).filter(col('time') > start_date)
df = df.limit(100) 
# added to speed up processings as during testing it was proving a bottleneck
# The problem is caused by the Python UDF (reverse_geocoder) being a bottleneck due to its non-parallel nature and high computational cost per task

def get_country_code(lat, lon):
    """
    Retrieve the country code for a given latitude and longitude.

    Parameters:
    lat (float or str): Latitude of the location.
    lon (float or str): Longitude of the location.

    Returns:
    str: Country code of the location, retrieved using the reverse geocoding API.

    Example:
    >>> get_country_details(48.8588443, 2.2943506)
    'FR'
    """
    try:
        coordinates = (float(lat), float(lon))
        result = rg.search(coordinates)[0].get('cc')
        print(f"Processed coordinates: {coordinates} -> {result}")
        return result
    except Exception as e:
        print(f"Error processing coordinates: {lat}, {lon} -> {str(e)}")
        return None
# registering the udfs so they can be used on spark dataframes
get_country_code_udf = udf(get_country_code, StringType())
# Trial Example
get_country_code(48.8588443, 2.2943506)
# adding country_code and city attributes
df_with_location = \
                df.\
                    withColumn("country_code", get_country_code_udf(col("latitude"), col("longitude")))
df.printSchema()
df_with_location.printSchema()
df.head()
df_with_location.head()
# adding significance classification
df_with_location_sig_class = \
                            df_with_location.\
                                withColumn('sig_class', 
                                            when(col("sig") < 100, "Low").\
                                            when((col("sig") >= 100) & (col("sig") < 500), "Moderate").\
                                            otherwise("High")
                                            )
df_with_location_sig_class.printSchema()
# Save the transformed DataFrame to the Silver container
gold_output_path = f"{gold_adls}earthquake_events_gold/"
# Append DataFrame to Silver container in Parquet format
df_with_location_sig_class.write.mode('append').parquet(gold_output_path)
