# Third party
from flask import Flask, render_template, jsonify

# Custom
from modules import last_date
from modules.calculate_temp import calc_temp
from modules.get_station_data import get_station_data
from modules.get_prcp_data import get_prcp_data
from modules.get_tobs_data import get_tobs_data

application = Flask(__name__)
application.config["DEBUG"] = False


@application.route("/")
def index():
    return render_template("index.html")


@application.route("/api/v2.0/precipitation")
def precipitation_endpoint():
    """
    Returns precipitation of each day in Hawaii for the last 12 months
    of data-set.
    """
    prcp_data = get_prcp_data()

    return jsonify(prcp_data)


@application.route("/api/v2.0/stations")
def stations_endpoint():
    """
    Returns weather station IDs of weather stations
    used in data.
    """
    stations = get_station_data()

    return jsonify(stations)


@application.route("/api/v2.0/tobs")
def tobs_endpoint():
    """
    Returns temperature observation data (tobs) for the last
    12 months of data-set. Represents a temperature for each day.
    """
    tobs_data = get_tobs_data()

    return jsonify(tobs_data)


@application.route(
    "/api/v2.0/aggregate/<start>", defaults={"end": last_date}, methods=["GET"]
)
@application.route("/api/v2.0/aggregate/<start>/<end>", methods=["GET"])
def aggregate_endpoint(start, end):
    """
    Returns min, average, and max temperature for the specified date and/or date range.
    """
    start = str(start)
    end = str(end)
    data = calc_temp(start, end)

    return jsonify(data)


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)
