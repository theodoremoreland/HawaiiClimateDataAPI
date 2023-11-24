# HawaiiClimateDataAPI

For this project, I used Python to perform analysis on a climate database before mapping said database to a custom built REST-API. I used Python and SQLAlchemy to do climate analysis and exploration on a hawaii.sqlite database, all analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib. The REST-API was developed using vanilla Flask.

<img src="presentation/thumbnail.png" width="650">

*This project was for an assignment at Washington University's Data Analytics Boot Camp (2019).*

## Technologies used
- Python
- HTML
- CSS
- Jupyter Notebook
- Matplotlib
- Pandas
- Flask
- Black
- VS Code

## Sections
- [API](#Climate-API)
- [Analysis](#Analysis)

# Climate API

### Home (Desktop)
<img src="presentation/1.PNG" width="900">

### Home #2 (Mouseover - Desktop)

<img src="presentation/2.PNG" width="700">

### Home (Mobile)

<img src="presentation/3.PNG" width="300">

### /api/v2.0/precipitation
Returns precipitation data for the most recent 12 months of dataset.

<img src="presentation/4.PNG" width="700">

### /api/v2.0/stations
Return station data.

<img src="presentation/5.PNG" width="700">

### /api/v2.0/tobs
Returns temperature observation data (tobs) from 12 most recent months of dataset.

<img src="presentation/6.PNG" width="700">

### /api/v2.0/aggregate/start-date/end-date
Returns minimum temperature, average temperature, and the max temperature for a given start or start-end range.

<img src="presentation/7.png" width="700">

- - -

## Analysis
### Precipitation summary statistics (within 12 month range)

<img src="presentation/plot1.png" width="900">

<img src="presentation/stats.PNG" width="200">


### Last 12 months of temperature observation data (tobs)

<img src="presentation/plot2.png" width="900">

<img src="presentation/plot3.png" width="300">
