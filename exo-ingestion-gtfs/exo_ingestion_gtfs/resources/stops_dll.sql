CREATE TABLE IF NOT EXISTS gtfs_landing.stops (
    stop_id string,
    stop_code string,
    stop_name string,
    stop_desc string,
    stop_lat string,
    stop_lon string,
    zone_id string,
    stop_url string,
    location_type string,
    parent_station string,
    stop_timezone string,
    wheelchair_boarding string,
    level_id string,
    platform_code string,
    landing_date date
)
USING DELTA CLUSTER BY (landing_date)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#stopstxt'