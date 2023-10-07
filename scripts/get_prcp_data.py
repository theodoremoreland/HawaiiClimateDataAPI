# Third party
import pandas as pd
from sqlalchemy import func

# Custom
from . import Measurement, session, one_year_ago


def get_prcp_data():
    prcp_last_12_months = (
        session.query(Measurement.date, Measurement.prcp)
        .order_by(Measurement.date.desc())
        .filter(func.strftime("%Y-%m-%d", Measurement.date) >= one_year_ago)
        .all()
    )
    prcp_last_12_months_df = pd.DataFrame(prcp_last_12_months).set_index("date")
    prcp_last_12_months_df.fillna(value=0, inplace=True)
    prcp_last_12_months_df = prcp_last_12_months_df.sort_values(
        "date", ascending=True
    ).iloc[0:]
    prcp_last_12_months_df.reset_index(inplace=True)

    return prcp_last_12_months_df.to_dict()
