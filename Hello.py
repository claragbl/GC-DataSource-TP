from flask import Flask, request, render_template, jsonify
import logging
import os
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    MetricType,
    RunReportRequest,
)
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('agg')
from pytrends.request import TrendReq
import base64
from io import BytesIO
import time
from collections import Counter
import numpy as np

KEY_FILE_LOCATION = 'datasourceproject-1df797562433.json'

app = Flask(__name__)

# ----------------------------------------------------------------------------------
# Decorator to measure the execution time of a function
def timing_decorator(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"{func.__name__} took {execution_time:.2f} seconds to execute.")
    #result_str = f"{func.__name__} took {execution_time:.2f} seconds to execute."
    return result
  return wrapper

@timing_decorator
def get_active_users(property_id="YOUR-GA4-PROPERTY-ID"):
    
  os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = KEY_FILE_LOCATION
    
  """Runs a simple report on a Google Analytics 4 property."""
  # Replace with your Google Analytics 4 property ID before running.
  property_id = "407503460"

  # Using a default constructor instructs the client to use the credentials
  # specified in GOOGLE_APPLICATION_CREDENTIALS environment variable.
  client = BetaAnalyticsDataClient()

  request = RunReportRequest(
    property=f"properties/{property_id}",
    metrics=[Metric(name="activeUsers")],
    date_ranges=[DateRange(start_date="2020-03-31", end_date="today")],
  )
  response = client.run_report(request)

  return response.rows[0].metric_values[0].value


# Function using a dictionary to count words
@timing_decorator
def word_count_dict(text):
  word_count = {}
  words = text.split()
  for word in words:
    word = word.lower() # Lowercase for case-insensitive word counting
    word_count[word] = word_count.get(word, 0) + 1
  return word_count

# Function using Counter to count words
@timing_decorator
def word_count_counter(text):
  words = text.split()
  words = [word.lower() for word in words]  
  return Counter(words)


# -------------------------------------------
# MAIN PAGE (TP1 - TP2): 
# -> GOOGLE BUTTON
# -> GOOGLE ANALYTIC BUTTON
# -> COOKIES
# -> ACTIVE USERS
# -------------------------------------------
@app.route("/")
def hello_world():

  cookies = request.cookies
  active_users = get_active_users()

  return render_template('helloTemplate.html', cookies=cookies, active_users=active_users)

# -------------------------------------------
# LOGGER PAGE (TP1):
# -> TEXT BOX
# -------------------------------------------
@app.route("/logger", methods=['GET', 'POST'])
def logger():
#     # display a log on the server side
#     #app.logger.info("Hi ! I am a log on the server side")
#     print('coucou')

#     # display a log on the browser side 
#     js_code = """
#     <script>
#         console.log("Hi ! I am a log on the browser side");
#     </script>
#     """

  if request.method == 'POST':
    # Retrieve the text from the textarea
    text = request.form.get('textarea')
  
    # Print the text in terminal for verification
    print(text)
  
  return render_template('index.html')

# -------------------------------------------
# GOOGLE TREND PAGE (TP3):
# -> GOOGLE TREND GRAPH OF WAR & COVID
# -------------------------------------------
@app.route('/google-trends', methods=['GET'])
def get_google_trends():

  pytrends = TrendReq(hl='en-US', tz=360) 
  pytrends.build_payload(kw_list=['war', 'covid'], timeframe='2019-03-01 2020-10-31')
  data = pytrends.interest_over_time()
    
  # Generate a line plot to see the trends
  plt.figure(figsize=(10, 4))
  plt.plot(data.index, data['war'], label='War')
  plt.plot(data.index, data['covid'], label='Covid')
  plt.xlabel('Date')
  plt.ylabel('Search Interest')
  plt.title('Google Trends Data')
  plt.legend()

  # Convert the plot to a bytes object and then to base64 for embedding in a web page
  buffer = BytesIO()
  plt.savefig(buffer, format='png')
  plt.close()
  buffer.seek(0)
  plot_data = base64.b64encode(buffer.read()).decode()
    
  return render_template('google_trend.html', plot_data=plot_data)

# -------------------------------------------
# SHAKESPEARE COUNT WORD(TP3):
# -------------------------------------------
@app.route('/count-words', methods=['GET'])
def count_words():
  with open('shakespeare.txt', 'r') as file:
    text = file.read()

  word_count_dict_result = word_count_dict(text)
  word_count_counter_result = word_count_counter(text)

  return render_template('word_count.html',
                           word_count_dict=word_count_dict_result,
                           word_count_counter=word_count_counter_result)


