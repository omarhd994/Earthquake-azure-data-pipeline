-- Select the first 100 rows from the gold-layer Parquet files in Azure Data Lake
SELECT
    TOP 100 *  -- Limit the result to the first 100 rows (for preview or sampling)

FROM
    -- Read data directly from the specified folder in Azure Data Lake
    OPENROWSET(
        BULK 'https://dataomar123.dfs.core.windows.net/gold/earthquake_events_gold/**',  -- Path to all Parquet files under the folder
        FORMAT = 'PARQUET'  -- Specify that the files are in Parquet format
    ) AS [result];  -- Alias for the dataset loaded from the files

--------------

-- Select the country code and count of earthquakes by significance class
SELECT
    country_code,

    -- Count number of earthquakes classified as 'low' significance
    COUNT(CASE WHEN LOWER(sig_class) = 'low' THEN 1 END) AS low_count,

    -- Count number of earthquakes classified as 'moderate' significance
    COUNT(CASE WHEN LOWER(sig_class) = 'moderate' THEN 1 END) AS moderate_count,

    -- Count number of earthquakes classified as 'high' significance
    COUNT(CASE WHEN LOWER(sig_class) = 'high' THEN 1 END) AS high_count

FROM
    -- Read data from the 'gold' layer in Azure Data Lake (in Parquet format)
    OPENROWSET(
        BULK 'https://dataomar123.dfs.core.windows.net/gold/earthquake_events_gold/**',  -- Path to Parquet files
        FORMAT = 'PARQUET'  -- Specify file format
    ) AS [result]

-- Group results by country to get counts per country
GROUP BY 
    country_code;
