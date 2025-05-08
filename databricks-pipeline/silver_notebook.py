# Code before Azure Implementation

from datetime import date, timedelta

# Remove this before running Data Factory Pipeline
start_date = date.today() - timedelta(1)

bronze_adls = "abfss://bronze@dataomar123.dfs.core.windows.net/"
silver_adls = "abfss://silver@dataomar123.dfs.core.windows.net/"
from pyspark.sql.functions import col, isnull, when
from pyspark.sql.types import TimestampType
from datetime import date, timedelta
# Load the JSON data into a Spark DataFrame
df = spark.read.option("multiline", "true").json(f"{bronze_adls}{start_date}_earthquake_data.json")
df.head()
df
df.display()

# Reshape earthquake data
df = (
    df
    .select(
        'id',
        col('geometry.coordinates').getItem(0).alias('longitude'),
        col('geometry.coordinates').getItem(1).alias('latitude'),
        col('geometry.coordinates').getItem(2).alias('elevation'),
        col('properties.title').alias('title'),
        col('properties.place').alias('place_description'),
        col('properties.sig').alias('sig'),
        col('properties.mag').alias('mag'),
        col('properties.magType').alias('magType'),
        col('properties.time').alias('time'),
        col('properties.updated').alias('updated')
    )
)
    
df.head()
df.display()

# Validate & clean data frame: Check for missing or null values
df = (
    df
    .withColumn('longitude', when(isnull(col('longitude')), 0).otherwise(col('longitude')))
    .withColumn('latitude', when(isnull(col('latitude')), 0).otherwise(col('latitude')))
    .withColumn('time', when(isnull(col('time')), 0).otherwise(col('time')))
)
df.head()
# Convert 'time' and 'updated' to timestamp from Unix time
df = (
    df
    .withColumn('time', (col('time') / 1000).cast(TimestampType()))
    .withColumn('updated', (col('updated') / 1000).cast(TimestampType()))
)
     
df.head()
# Save the transformed DataFrame in the Silver container
silver_output_path = f"{silver_adls}earthquake_events_silver/"
# Append DataFrame to Silver container in Parquet format
df.write.mode('append').parquet(silver_output_path)
