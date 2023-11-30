CREATE TABLE IF NOT EXISTS gtfs_landing.shapes (
    shape_id string,
    shape_pt_lat string,
    shape_pt_lon string,
    shape_pt_sequence string,
    shape_dist_traveled string,
    landing_date date
)
USING DELTA CLUSTER BY (landing_date)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#shapestxt';