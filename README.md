## Climate Analysis and Exploration

To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Use the provided starter notebook and hawaii.sqlite files to complete your climate analysis and data exploration.

* Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.

* Use SQLAlchemy `create_engine` to connect to your sqlite database.

* Use SQLAlchemy `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.

### Precipitation Analysis

* Design a query to retrieve the last 12 months of precipitation data.

* Select only the `date` and `prcp` values.

* Load the query results into a Pandas DataFrame and set the index to the date column.

* Sort the DataFrame values by `date`.

* Plot the results using the DataFrame `plot` method.


* Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Design a query to calculate the total number of stations.

* Design a query to find the most active stations.

  * List the stations and observation counts in descending order.

  * Which station has the highest number of observations?

  * Hint: You may need to use functions such as `func.min`, `func.max`, `func.avg`, and `func.count` in your queries.

* Design a query to retrieve the last 12 months of temperature observation data (tobs).

  * Filter by the station with the highest number of observations.

  * Plot the results as a histogram with `bins=12`.

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
