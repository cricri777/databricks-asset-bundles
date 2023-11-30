CREATE TABLE IF NOT EXISTS gtfs_landing.agency (
    agency_id string,
    agency_name string,
    agency_url string,
    agency_timezone string,
    agency_lang string,
    agency_phone string,
    agency_fare_url string,
    agency_email string,
    landing_date date
)
USING DELTA CLUSTER BY (landing_date)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#agencytxt';