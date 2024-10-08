import requests
from . import constants
from dagster import asset


@asset
def taxi_trips_file() -> None:
    """The raw parquet files for the taxi trips dataset. Data is sourced from the NYC Taxi and Limousine Commission."""
    month_to_fetch = "2023-02"
    raw_trips = requests.get(
        f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{month_to_fetch}.parquet"
    )

    with open(
        constants.TAXI_TRIPS_TEMPLATE_FILE_PATH.format(month_to_fetch), "wb"
    ) as output_file:
        output_file.write(raw_trips.content)
