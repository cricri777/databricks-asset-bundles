import os

from pyspark.sql.functions import current_date, col
from requests import get
from io import BytesIO
from zipfile import ZipFile
import pandas as pd
import fire
import pyspark.pandas as ps

from databricks.sdk import WorkspaceClient
from databricks.connect import DatabricksSession
os.environ["PYARROW_IGNORE_TIMEZONE"] = '1'

def run(env="dev"):
    w = WorkspaceClient()
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

    list_exo_url = {
        "autobus_chambly": "https://exo.quebec/xdata/citcrc/google_transit.zip",
        "autobus_saintlaurent": "https://exo.quebec/xdata/cithsl/google_transit.zip",
        "autobus_laurentides": "https://exo.quebec/xdata/citla/google_transit.zip",
        "autobus_presquile": "https://exo.quebec/xdata/citpi/google_transit.zip",
        "autobus_richelain": "https://exo.quebec/xdata/citlr/google_transit.zip",
        "autobus_roussillon": "https://exo.quebec/xdata/citrous/google_transit.zip",
        "autobus_sorel_varennes": "https://exo.quebec/xdata/citsv/google_transit.zip",
        "autobus_sudouest": "https://exo.quebec/xdata/citso/google_transit.zip",
        "autobus_richelieu": "https://exo.quebec/xdata/citvr/google_transit.zip",
        "autobus_assomption": "https://exo.quebec/xdata/mrclasso/google_transit.zip",
        "autobus_terrebonne_mascouche": "https://exo.quebec/xdata/mrclm/google_transit.zip",
        "trains_exo": "https://exo.quebec/xdata/trains/google_transit.zip",
        "autobus_sainte_julie": "https://exo.quebec/xdata/omitsju/google_transit.zip",
        "autobus_richelain_roussillon": "https://exo.quebec/xdata/lrrs/google_transit.zip"
    }

    agency_df = pd.DataFrame()
    stops_df = pd.DataFrame()
    routes_df = pd.DataFrame()
    trips_df = pd.DataFrame()
    stop_times_df = pd.DataFrame()
    calendar_df = pd.DataFrame()
    calendar_dates_df = pd.DataFrame()
    fare_rules_df = pd.DataFrame()
    shapes_df = pd.DataFrame()
    feed_info_df = pd.DataFrame()

    for name, exo_urls in list_exo_url.items():
        print(f"querying [{exo_urls}]")
        request = get(exo_urls)
        zip_file = ZipFile(BytesIO(request.content))
        files = zip_file.namelist()
        for file in files:
            if file == "agency.txt":
                with zip_file.open(file, 'r') as csvfile:
                    agency_df = pd.concat([agency_df, pd.read_csv(BytesIO(csvfile.read()))])
            elif file == "stops.txt":
                with zip_file.open(file, 'r') as csvfile:
                    stops_df = pd.concat([stops_df, pd.read_csv(BytesIO(csvfile.read()))])
            elif file == "routes.txt":
                with zip_file.open(file, 'r') as csvfile:
                    routes_df = pd.concat([routes_df, pd.read_csv(BytesIO(csvfile.read()))])
            elif file == "trips.txt":
                with zip_file.open(file, 'r') as csvfile:
                    trips_df = pd.concat([trips_df, pd.read_csv(BytesIO(csvfile.read()))])
            elif file == "stop_times.txt":
                with zip_file.open(file, 'r') as csvfile:
                    stop_times_df = pd.concat([stop_times_df, pd.read_csv(BytesIO(csvfile.read()))])
            elif file == "calendar.txt":
                with zip_file.open(file, 'r') as csvfile:
                    calendar_df = pd.concat([calendar_df, pd.read_csv(BytesIO(csvfile.read()))])
            elif file == "calendar_dates.txt":
                with zip_file.open(file, 'r') as csvfile:
                    calendar_dates_df = pd.concat([calendar_dates_df, pd.read_csv(BytesIO(csvfile.read()))])
            elif file == "fare_rules.txt":
                with zip_file.open(file, 'r') as csvfile:
                    fare_rules_df = pd.concat([fare_rules_df, pd.read_csv(BytesIO(csvfile.read()))])
            elif file == "shapes.txt":
                with zip_file.open(file, 'r') as csvfile:
                    shapes_df = pd.concat([shapes_df, pd.read_csv(BytesIO(csvfile.read()))])
            elif file == "feed_info.txt":
                with zip_file.open(file, 'r') as csvfile:
                    feed_info_df = pd.concat([feed_info_df, pd.read_csv(BytesIO(csvfile.read()))])

    agency_df = agency_df.astype("string")
    stops_df = stops_df.astype("string")
    routes_df = routes_df.astype("string")
    trips_df = trips_df.astype("string")
    stop_times_df = stop_times_df.astype("string")
    calendar_df = calendar_df.astype("string")
    calendar_dates_df = calendar_dates_df.astype("string")
    fare_rules_df = fare_rules_df.astype("string")
    shapes_df = shapes_df.astype("string")
    feed_info_df = feed_info_df.astype("string")

    spark_agency_df = session.createDataFrame(agency_df).withColumn("landing_date", current_date())
    spark_stops_df = session.createDataFrame(stops_df).withColumn("landing_date", current_date())
    spark_routes_df = session.createDataFrame(routes_df).withColumn("landing_date", current_date())
    spark_trips_df = session.createDataFrame(trips_df).withColumn("landing_date", current_date())
    spark_stop_times_df = session.createDataFrame(stop_times_df).withColumn("landing_date", current_date())
    spark_calendar_df = session.createDataFrame(calendar_df).withColumn("landing_date", current_date())
    spark_calendar_dates_df = session.createDataFrame(calendar_dates_df).withColumn("landing_date", current_date())
    spark_fare_rules_df = session.createDataFrame(fare_rules_df).withColumn("landing_date", current_date())
    spark_shapes_df = session.createDataFrame(shapes_df).withColumn("landing_date", current_date())
    spark_feed_info_df = session.createDataFrame(feed_info_df).withColumn("landing_date", current_date())

    spark_agency_df.write.mode("overwrite").option("replaceWhere", "landing_date = current_date()").saveAsTable(f"exo_{env}.gtfs_landing.agency")
    spark_stops_df.write.mode("overwrite").option("replaceWhere", "landing_date = current_date()").saveAsTable(f"exo_{env}.gtfs_landing.stops")
    spark_routes_df.write.mode("overwrite").option("replaceWhere", "landing_date = current_date()").saveAsTable(f"exo_{env}.gtfs_landing.routes")
    spark_trips_df.write.mode("overwrite").option("replaceWhere", "landing_date = current_date()").saveAsTable(f"exo_{env}.gtfs_landing.trips")
    # spark_stop_times_df.write.mode("overwrite").option("replaceWhere", "landing_date = current_date()").saveAsTable(f"exo_{env}.gtfs_landing.stop_times")
    spark_calendar_df.write.mode("overwrite").option("replaceWhere", "landing_date = current_date()").saveAsTable(f"exo_{env}.gtfs_landing.calendar")
    spark_calendar_dates_df.write.mode("overwrite").option("replaceWhere", "landing_date = current_date()").saveAsTable(f"exo_{env}.gtfs_landing.calendar_dates")
    spark_fare_rules_df.write.mode("overwrite").option("replaceWhere", "landing_date = current_date()").saveAsTable(f"exo_{env}.gtfs_landing.fare_rules")
    spark_shapes_df.write.mode("overwrite").option("replaceWhere", "landing_date = current_date()").saveAsTable(f"exo_{env}.gtfs_landing.shapes")
    spark_feed_info_df.write.mode("overwrite").option("replaceWhere", "landing_date = current_date()").saveAsTable(f"exo_{env}.gtfs_landing.feed_info")


if __name__ == '__main__':
    fire.Fire(run)
