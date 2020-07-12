# HawaiiClimateDataAPI

For this project, I used Python to perform analysis on a climate database before mapping said database to custom built REST-API. I used Python and SQLAlchemy to do climate analysis and exploration on a hawaii.sqlite database, all analysis completed using SQLAlchemy ORM queries, Pandas, and Matplotlib. The REST-API was developed using vanilla Flask.

*This project was for an assignment at Washington University's Data Analytics Boot Camp (2019).*

### Precipitation Analysis

* Design a query to retrieve the last 12 months of precipitation data and plots the results.

### Station Analysis

* Retrieves the last 12 months of temperature observation data (tobs) and plots the results as a histogram with `bins=12`.

- - -

## Climate API

A Flask API based on the queries that you have just developed.

## Home 
<img src="presentation/1.PNG" width="900">

## /api/v1.0/precipitation

<img src="presentation/2.PNG" width="700">


## /api/v1.0/stations
Returns a JSON list of stations from the dataset.

<img src="presentation/3.PNG" width="700">

## /api/v1.0/tobs
Returns a JSON list of Temperature Observations (tobs) for the previous year.

<img src="presentation/4.PNG" width="700">


## /api/v1.0/start-date
Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

<img src="presentation/5.PNG" width="700">


## /api/v1.0/start-date/end-date

<img src="presentation/6.PNG" width="700">
