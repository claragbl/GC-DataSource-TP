from flask import Flask, request, render_template
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

KEY_FILE_LOCATION = 'datasourceproject-1df797562433.json'

app = Flask(__name__)

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


@app.route("/")
def hello_world():

  cookies = request.cookies
  #status_code = request.status_code

  print(cookies)
  active_users = get_active_users()
  #print(status_code)

  return render_template('helloTemplate.html', cookies=cookies, active_users=active_users)

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
