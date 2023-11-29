import os

from pyspark.sql.functions import current_date
from requests import get
from io import BytesIO
from zipfile import ZipFile
import pandas as pd
import fire

from databricks.connect import DatabricksSession
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)


def run(env="dev", is_dry_run=True):
    session = DatabricksSession.builder.getOrCreate()
    session.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
    session.conf.set("spark.sql.execution.arrow.pyspark.fallback.enabled", "true")

    session.sql(f"CREATE CATALOG IF NOT EXISTS exo_{env} COMMENT 'Catalog pour les données GTFS Exo env [{env}]'")

    session.sql(f"CREATE SCHEMA IF NOT EXISTS exo_{env}.gtfs_landing COMMENT 'Schema landing pour les données GTFS Exo env [{env}]'")

    session.sql(f"USE CATALOG exo_{env}")

    dll_resource_path = os.path.abspath(os.path.join(os.getcwd(), 'resources/'))
    for dll_file in os.listdir(dll_resource_path):
        with open(os.path.join(dll_resource_path, dll_file), 'r') as query_sql:
            print(f"execute sql [{dll_file}]")
            session.sql(query_sql.read())

    list_exo_url = [
        "https://exo.quebec/xdata/citcrc/google_transit.zip",
        "https://exo.quebec/xdata/cithsl/google_transit.zip",
        "https://exo.quebec/xdata/citla/google_transit.zip",
        "https://exo.quebec/xdata/citpi/google_transit.zip",
        "https://exo.quebec/xdata/citlr/google_transit.zip",
        "https://exo.quebec/xdata/citrous/google_transit.zip",
        "https://exo.quebec/xdata/citsv/google_transit.zip",
        "https://exo.quebec/xdata/citso/google_transit.zip",
        "https://exo.quebec/xdata/citvr/google_transit.zip",
        "https://exo.quebec/xdata/mrclasso/google_transit.zip",
        "https://exo.quebec/xdata/mrclm/google_transit.zip",
        "https://exo.quebec/xdata/trains/google_transit.zip",
        "https://exo.quebec/xdata/omitsju/google_transit.zip",
        "https://exo.quebec/xdata/lrrs/google_transit.zip"
    ]

    dict_exo_gtfs_df = {
        "agency": pd.DataFrame(),
        "stops": pd.DataFrame(),
        "routes": pd.DataFrame(),
        "trips": pd.DataFrame(),
        "stop_times": pd.DataFrame(),
        "calendar": pd.DataFrame(),
        "calendar_dates": pd.DataFrame(),
        "fare_rules": pd.DataFrame(),
        "shapes": pd.DataFrame(),
        "feed_info": pd.DataFrame()
    }

    for exo_urls in list_exo_url:
        print(f"querying [{exo_urls}]")
        request = get(exo_urls)
        zip_file = ZipFile(BytesIO(request.content))
        files = zip_file.namelist()
        for file in files:
            if file == "agency.txt":
                with zip_file.open(file, 'r') as csvfile:
                    dict_exo_gtfs_df["agency"] = pd.concat([dict_exo_gtfs_df["agency"], pd.read_csv(BytesIO(csvfile.read()))])
            elif file == "stops.txt":
                with zip_file.open(file, 'r') as csvfile:
                    dict_exo_gtfs_df["stops"] = pd.concat([dict_exo_gtfs_df["stops"], pd.read_csv(BytesIO(csvfile.read()))])
            elif file == "routes.txt":
                with zip_file.open(file, 'r') as csvfile:
                    dict_exo_gtfs_df["routes"] = pd.concat([dict_exo_gtfs_df["routes"], pd.read_csv(BytesIO(csvfile.read()))])
            elif file == "trips.txt":
                with zip_file.open(file, 'r') as csvfile:
                    dict_exo_gtfs_df["trips"] = pd.concat([dict_exo_gtfs_df["trips"], pd.read_csv(BytesIO(csvfile.read()))])
            elif file == "stop_times.txt":
                with zip_file.open(file, 'r') as csvfile:
                    dict_exo_gtfs_df["stop_times"] = pd.concat([dict_exo_gtfs_df["stop_times"], pd.read_csv(BytesIO(csvfile.read()))])
            elif file == "calendar.txt":
                with zip_file.open(file, 'r') as csvfile:
                    dict_exo_gtfs_df["calendar"] = pd.concat([dict_exo_gtfs_df["calendar"], pd.read_csv(BytesIO(csvfile.read()))])
            elif file == "calendar_dates.txt":
                with zip_file.open(file, 'r') as csvfile:
                    dict_exo_gtfs_df["calendar_dates"] = pd.concat([dict_exo_gtfs_df["calendar_dates"], pd.read_csv(BytesIO(csvfile.read()))])
            elif file == "fare_rules.txt":
                with zip_file.open(file, 'r') as csvfile:
                    dict_exo_gtfs_df["fare_rules"] = pd.concat([dict_exo_gtfs_df["fare_rules"], pd.read_csv(BytesIO(csvfile.read()))])
            elif file == "shapes.txt":
                with zip_file.open(file, 'r') as csvfile:
                    dict_exo_gtfs_df["shapes"] = pd.concat([dict_exo_gtfs_df["shapes"], pd.read_csv(BytesIO(csvfile.read()))])
            elif file == "feed_info.txt":
                with zip_file.open(file, 'r') as csvfile:
                    dict_exo_gtfs_df["feed_info"] = pd.concat([dict_exo_gtfs_df["feed_info"], pd.read_csv(BytesIO(csvfile.read()))])

    for gtfs_exo_name, gtfs_exo_df in dict_exo_gtfs_df.items():
        gtfs_exo_df = gtfs_exo_df.astype("string")
        if gtfs_exo_name == "stop_times":
            df_1 = gtfs_exo_df.iloc[:300000, :]
            df_2 = gtfs_exo_df.iloc[300000:, :]
            spark_stop_times_df1 = session.createDataFrame(df_1).withColumn("landing_date", current_date())
            spark_stop_times_df2 = session.createDataFrame(df_2).withColumn("landing_date", current_date())
            if not is_dry_run:
                spark_stop_times_df1.union(spark_stop_times_df2).write.mode("overwrite").option("replaceWhere","landing_date = current_date()").saveAsTable(f"exo_{env}.gtfs_landing.{gtfs_exo_name}")

        else:
            gtfs_exo_pyspark_df = session.createDataFrame(gtfs_exo_df).withColumn("landing_date", current_date())
            if not is_dry_run:
                gtfs_exo_pyspark_df.write.mode("overwrite").option("replaceWhere", "landing_date = current_date()").saveAsTable(f"exo_{env}.gtfs_landing.{gtfs_exo_name}")


if __name__ == '__main__':
    fire.Fire(run)
