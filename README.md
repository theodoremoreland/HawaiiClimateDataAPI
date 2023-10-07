# HawaiiClimateDataAPI

For this project, I used Python to perform analysis on a climate database before mapping said database to a custom built REST-API. I used Python and SQLAlchemy to do climate analysis and exploration on a hawaii.sqlite database, all analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib. The REST-API was developed using vanilla Flask.

*This project was for an assignment at Washington University's Data Analytics Boot Camp (2019).*

## Technologies used
- Python
- HTML
- CSS
- Jupyter Notebook
- Pandas
- Flask
- Black
- VS Code

## Sections
- [Analysis](#Analysis)
- [API](#Climate-API)

## Analysis
### Precipitation summary statistics (within 12 month range)

<img src="presentation/plot1.png" width="900">

<img src="presentation/stats.PNG" width="200">


### Last 12 months of temperature observation data (tobs)

<img src="presentation/plot2.png" width="900">

<img src="presentation/plot3.png" width="300">

- - -

# Climate API

### Home 
<img src="presentation/1.PNG" width="900">

### /api/v2.0/precipitation

<img src="presentation/2.PNG" width="700">

### /api/v2.0/stations
Returns a JSON list of stations from the dataset.

<img src="presentation/3.PNG" width="700">

### /api/v2.0/tobs
Returns a JSON list of Temperature Observations (tobs) for the most recent 12 months of dataset.

<img src="presentation/4.PNG" width="700">

### /api/v2.0/start-date
Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

<img src="presentation/5.PNG" width="700">

### /api/v2.0/start-date/end-date

<img src="presentation/6.PNG" width="700">
