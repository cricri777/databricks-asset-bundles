CREATE TABLE IF NOT EXISTS gtfs_landing.feed_info (
    feed_publisher_name string,
    feed_publisher_url string,
    feed_lang string,
    default_lang string,
    feed_start_date string,
    feed_end_date string,
    feed_version string,
    feed_contact_email string,
    feed_contact_url string,
    landing_date date
)
USING DELTA CLUSTER BY (landing_date)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#feed_infotxt';