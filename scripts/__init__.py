# Python SQL toolkit and Object Relational Mapper
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

# sqlite path is relative to app.py caller.
engine = create_engine(
    "sqlite:///resources/hawaii.sqlite", connect_args={"check_same_thread": False}
)
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

# References to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
one_year_ago = (
    str(int(last_date[0:4]) - 1) + last_date[4:8] + str(int(last_date[8:10]) + 1)
)
