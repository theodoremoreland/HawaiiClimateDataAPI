# Third party
import pandas as pd
from sqlalchemy import func
from pprint import pprint

# Custom
from . import Measurement, session, one_year_ago


def get_tobs_data():
    result = {}
    tobs_last_12_months = (
        session.query(Measurement.date, Measurement.tobs)
        .order_by(Measurement.date.desc())
        .filter(func.strftime("%Y-%m-%d", Measurement.date) >= one_year_ago)
        .all()
    )
    tobs_df = pd.DataFrame(tobs_last_12_months)
    tobs_df_clean = tobs_df.copy().fillna(value=0)
    tobs_df_sorted = tobs_df_clean.sort_values("date", ascending=True).iloc[0:]

    for _, row in tobs_df_sorted.iterrows():
        date = row["date"]

        if date not in result:
            result[date] = []

        result[date].append(row["tobs"])

    return result
