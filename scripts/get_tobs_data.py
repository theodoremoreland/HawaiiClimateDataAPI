# Third party
import pandas as pd
from sqlalchemy import func

# Custom
from . import Measurement, session, one_year_ago


def get_tobs_data():
    tobs_last_12_months = (
        session.query(Measurement.date, Measurement.tobs)
        .order_by(Measurement.date.desc())
        .filter(func.strftime("%Y-%m-%d", Measurement.date) >= one_year_ago)
        .all()
    )
    tobs_df = pd.DataFrame(tobs_last_12_months)
    tobs_df_clean = tobs_df.copy().fillna(value=0)
    tobs_df_sorted = tobs_df_clean.sort_values("date", ascending=True).iloc[0:]

    return tobs_df_sorted.to_dict()
