#!/usr/bin/env python
# coding: utf-8

# Third party
from sqlalchemy import func

# Custom
from . import Measurement, session


def get_station_data():
    station_activity = (
        session.query(Measurement.station, func.count(Measurement.station))
        .group_by(Measurement.station)
        .order_by(func.count(Measurement.station).desc())
        .all()
    )

    return [{"station": x, "station_id": y} for x, y in station_activity]
