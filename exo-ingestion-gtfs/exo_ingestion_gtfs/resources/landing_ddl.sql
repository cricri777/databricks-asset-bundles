CREATE TABLE IF NOT EXISTS agency (
    agency_id string,
    agency_name string NOT NULL,
    agency_url string NOT NULL,
    agency_timezone string NOT NULL,
    agency_lang string,
    agency_phone string,
    agency_fare_url string,
    agency_email string
)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#agencytxt';

CREATE TABLE IF NOT EXISTS stops (
    stop_id string NOT NULL,
    stop_code string,
    stop_name string NOT NULL,
    stop_desc string,
    stop_lat string NOT NULL,
    stop_lon string NOT NULL,
    zone_id string NOT NULL,
    stop_url string,
    location_type string,
    parent_station string,
    stop_timezone string,
    wheelchair_boarding string,
    level_id string,
    platform_code string
)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#stopstxt';


CREATE TABLE IF NOT EXISTS routes (
    route_id string NOT NULL,
    agency_id string,
    route_short_name string,
    route_long_name string,
    route_desc string,
    route_type string NOT NULL,
    route_url string,
    route_color string,
    route_text_color string,
    route_sort_order integer,
    continuous_pickup string,
    continuous_drop_off string
)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#routestxt';


CREATE TABLE IF NOT EXISTS trips (
    route_id string NOT NULL,
    service_id string NOT NULL,
    trip_id string NOT NULL,
    trip_headsign string,
    trip_short_name string,
    direction_id string,
    block_id string,
    shape_id string,
    wheelchair_accessible string,
    bikes_allowed string
)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#tripstxt';

CREATE TABLE IF NOT EXISTS stop_times(
    trip_id string NOT NULL,
    arrival_time string,
    departure_time string,
    stop_id string NOT NULL,
    stop_sequence integer NOT NULL,
    stop_headsign string,
    pickup_type string,
    drop_off_type string,
    continuous_pickup string,
    continuous_drop_off string,
    shape_dist_traveled double,
    timepoint double
)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#tripstxt';

CREATE TABLE IF NOT EXISTS calendar (
    service_id string NOT NULL,
    monday string NOT NULL,
    tuesday string NOT NULL,
    wednesday string NOT NULL,
    thursday string NOT NULL,
    friday string NOT NULL,
    saturday string NOT NULL,
    sunday string NOT NULL,
    start_date date NOT NULL,
    end_date date NOT NULL
)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#calendartxt';

CREATE TABLE IF NOT EXISTS calendar_dates (
    service_id string NOT NULL,
    date date NOT NULL,
    exception_type string NOT NULL
)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#calendar_datestxt';

CREATE TABLE IF NOT EXISTS fare_attributes (
    fare_id string NOT NULL,
    price double NOT NULL,
    currency_type string NOT NULL,
    payment_method string NOT NULL,
    transfers string NOT NULL,
    agency_id string,
    transfer_duration integer
)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#fare_attributestxt';

CREATE TABLE IF NOT EXISTS fare_rules (
    fare_id string NOT NULL,
    route_id string,
    origin_id string,
    destination_id string,
    contains_id string
)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#fare_rulestxt';

CREATE TABLE IF NOT EXISTS shapes (
    shape_id string NOT NULL,
    shape_pt_lat string NOT NULL,
    shape_pt_lon string NOT NULL,
    shape_pt_sequence integer NOT NULL,
    shape_dist_traveled string
)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#shapestxt';

CREATE TABLE IF NOT EXISTS frequencies (
    trip_id string NOT NULL,
    start_time string NOT NULL,
    end_time string NOT NULL,
    headway_secs integer NOT NULL,
    exact_times string
)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#frequenciestxt';

CREATE TABLE IF NOT EXISTS transfers (
    from_stop_id string NOT NULL,
    to_stop_id string NOT NULL,
    transfer_type string NOT NULL,
    min_transfer_time integer
)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#transferstxt';

CREATE TABLE IF NOT EXISTS pathways (
    pathway_id string NOT NULL,
    from_stop_id string NOT NULL,
    to_stop_id string NOT NULL,
    pathway_mode string NOT NULL,
    is_bidirectional string NOT NULL,
    length double,
    traversal_time integer,
    stair_count integer,
    max_slope double,
    min_width double,
    signposted_as string,
    reversed_signposted_as string
)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#pathwaystxt';

CREATE TABLE IF NOT EXISTS feed_info (
    feed_publisher_name string NOT NULL,
    feed_publisher_url string NOT NULL,
    feed_lang string NOT NULL,
    default_lang string,
    feed_start_date date,
    feed_end_date date,
    feed_version string,
    feed_contact_email string,
    feed_contact_url string
)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#feed_infotxt';

CREATE TABLE IF NOT EXISTS translations (
    table_name string NOT NULL,
    field_name string NOT NULL,
    language string NOT NULL,
    translation string NOT NULL,
    record_id string,
    record_sub_id string,
    field_value string
)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#translationstxt';

CREATE TABLE IF NOT EXISTS attributions (
    attribution_id string,
    agency_id string,
    route_id string,
    trip_id string,
    organization_name string NOT NULL,
    is_producer string,
    is_operator string,
    is_authority string,
    attribution_url string,
    attribution_email string,
    attribution_phone string
)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#attributionstxt';
