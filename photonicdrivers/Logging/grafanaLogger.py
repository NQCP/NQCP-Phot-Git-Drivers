# Class for logging to Grafana

import requests

# User ID and API Key for Grafana account created with Peter Granum's email
DEFAULT_USER_ID = 1545635
DEFAULT_API_KEY = "glc_eyJvIjoiMTEwODkyOCIsIm4iOiJzdGFjay05MTU0MjEtaW50ZWdyYXRpb24tbnFjcHBob3QiLCJrIjoiaDg5NnJiMTlQZTI2NzhWQmxVZDJ3SXlNIiwibSI6eyJyIjoicHJvZC1ldS1ub3J0aC0wIn19"

class GrafanaLogger:
  def __init__(self, _userID = DEFAULT_USER_ID, _apiKey = DEFAULT_API_KEY):
    # By default, the logger will log to Peter Granum's Grafana account
    self.userID = _userID
    self.apiKey = _apiKey
    print('Initialising Grafana logger')

  def log(self, varNameString, varValueDouble):

    body = varNameString + ',bar_label=abc,source=grafana_cloud_docs metric=' + str(varValueDouble)

    # print(body)
    # print(USER_ID)
    # print(API_KEY)

    response = requests.post('https://influx-prod-39-prod-eu-north-0.grafana.net/api/v1/push/influx/write', 
                              headers = {
                                'Content-Type': 'text/plain',
                              },
                              data = str(body),
                              auth = (self.userID, self.apiKey)
    )

    status_code = response.status_code
    # print(status_code)

    return status_code     
    

# def main():
#     print('hello')
#     logger = logG()
#     print(logger.log('myVar',2.40))

# if __name__ == "__main__":
#   main()