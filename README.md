# sqlalchemy-challenge
<h1><b>sqlalchemy - analysis of climate data and creation of climate app<b></h1>
  
<p><h2><b>Challenge for Data Analytics course:<b></h2></p> 
  
  <p><b>Part 1: to do a climate analysis and data exploration of a climate database for Hawaii.</b></p><ol>
  
  <li>Challenge requires the use of SQLAlchemy ORM queries</li>
  <li>CThe data is contained in a SQlite database so SQLAlchemy to reflect the tables into two classes: station and measurement</li>
  <li>a SQLAlchemy session is created to explore and analyse the climate data</li>
  <li>Using the most recent date, the previous 12 months of precipitation data are reteived by querying the previous 12 months of data</li>
  <li>The query results are loaded into a Pandas DataFrame and the results are plotted using MatPlotLib</li>
  <li>A query is written to find the number of weather stations with a count of their respective observations</li>
  <li>Having identified the station with the greatest number of observations its lowest, highest and average temperature records are calculated</li>
  <li>This station and its observations are stored in a dataframe and a histogram plots the range and frequencies of temperatures recoded.</li></ol></p>
  
  <p><b>Part 2: Design a climate app.</b></p><ol>
  
  <li>A Flask API is created based on the above queries</li>
  <li> The climate query results are converted into dictionaries and the url endpoints return JSON representations of the observations</li><ul>
    <li>a list of weather stations</li>
    <li> a list of daily rainfall totlas fromt he most active weather station</li>
    <li>The minimum, average and maximum temperatures recorded by the most active station for all dates greater or equal to a user defined start date</li>
    <li>The minimum, average and maximum temperatures recorded by the most active station for all dates user defined range</li></ul></ol>
  
  <h3>Sources</h3><ul>
  <li>StackOverflow (https://stackoverflow.com/questions/61912210/python-flask-returning-values-that-has-the-same-variable)</li>
  <li>https://stackoverflow.com/questions/64861342/return-value-from-inside-flask-function</li>
  <li> https://stackoverflow.com/questions/13279399/how-to-obtain-values-of-request-variables-using-python-and-flask</li>
  <li>Basic html commands: https://www.apu.ac.jp/~gunarto/html.html</li>
  <li>Assistance from ASKBCS Learning re issues around</li><ul>
  <li>url page not displaying for a query</li>
  <li>a coding issue giving incorrect results on the precipitation plot.</li></ul>
  <li>Use of class materials</>
   
  
  
  
    
