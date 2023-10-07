# Third party
from sqlalchemy import func

# Custom
from . import Measurement, session


def calc_temp(start_date, end_date):
    """Returns the minimum, average, and maximum temperatures for that range of dates
    This function will accept start date and end date in the format '%Y-%m-%d'
    """
    x = (
        session.query(
            func.min(Measurement.tobs),
            func.avg(Measurement.tobs),
            func.max(Measurement.tobs),
        )
        .filter(Measurement.date >= start_date)
        .filter(Measurement.date <= end_date)
        .all()
    )

    result = x[0]
    data = {"min": result[0], "avg": result[1], "max": result[2]}

    return data
