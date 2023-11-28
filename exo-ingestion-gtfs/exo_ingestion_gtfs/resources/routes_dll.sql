CREATE TABLE IF NOT EXISTS gtfs_landing.routes (
    route_id string,
    agency_id string,
    route_short_name string,
    route_long_name string,
    route_desc string,
    route_type string,
    route_url string,
    route_color string,
    route_text_color string,
    route_sort_order string,
    continuous_pickup string,
    continuous_drop_off string,
    landing_date date
)
USING DELTA CLUSTER BY (landing_date)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#routestxt';
