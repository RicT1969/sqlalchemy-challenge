# sqlalchemy-challenge
<h1><b>sqlalchemy - analysis of climate data and creation of climate app<b></h1>
<p><h2><b>Challenge for Data Analytics course:<b></h2></p> 
  <p><b>Part 1: to do a climate analysis and data exploration of a climate database for Hawaii.</b></p><ol>
  <li>Challenge requires the use of SQLAlchemy ORM queries</li>
  <li>Connect to an SQlite database and use SQLAlchemy to reflect the tables into classes named station and measurement</li>
  <li>Link Python to the database by ceating an SQLAlchemy session</li>
  <li>Using the most recent date, the previous 12 months of precipitation data are reteived by querying the previous 12 months of data</li>
  <li>The query results are loaded into a Pandas DataFrame and the results are plotted using MatPlotLib</li>
  <li>The number of weather stations are queried and listed with observation counts</li>
  <li>The station with the greatest number of observations is identified and its lowest highest and average temperatures recorded</li>
  <li>A dataframe is queried and filtered by the station with the greatest number of observations. A histogram demonstrates the range and frequencies of temperatures recoded.</li></ol></p>
  <p><b>Part 2: Design a climate app.</b></p><ol>
  <li>Design a Flask API based on the above queries</li>
  <li> Convert the results of the climate queries into a dictionary and return a JSON representation of the dictionary</li>
  <li>Return a JSON list of stations from the dataset</li>
  <li>Calculate the minimum, average and maximum temperatures for all dates greater or equal to the start date</li>
  <li>Return a JSON list of the minimum, average and maximum temperatures for a specified start or start-end range</li>
  
  
    
