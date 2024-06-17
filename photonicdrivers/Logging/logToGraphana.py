# logging to graphaha

# API:
# glc_eyJvIjoiMTEwODkyOCIsIm4iOiJzdGFjay05MTU0MjEtaW50ZWdyYXRpb24tbnFjcHBob3QiLCJrIjoiaDg5NnJiMTlQZTI2NzhWQmxVZDJ3SXlNIiwibSI6eyJyIjoicHJvZC1ldS1ub3J0aC0wIn19

import requests
import base64

USER_ID = 1545635
API_KEY = "glc_eyJvIjoiMTEwODkyOCIsIm4iOiJzdGFjay05MTU0MjEtaW50ZWdyYXRpb24tbnFjcHBob3QiLCJrIjoiaDg5NnJiMTlQZTI2NzhWQmxVZDJ3SXlNIiwibSI6eyJyIjoicHJvZC1ldS1ub3J0aC0wIn19"

class logG:
    def __init__(self):
        print('init')

    def log(self, varName, varValue):

        body = varName + ',bar_label=abc,source=grafana_cloud_docs metric=' + str(varValue)

        print(body)
        print(USER_ID)
        print(API_KEY)

        response = requests.post('https://influx-prod-39-prod-eu-north-0.grafana.net/api/v1/push/influx/write', 
                         headers = {
                           'Content-Type': 'text/plain',
                         },
                         data = str(body),
                         auth = (USER_ID, API_KEY)
        )

        status_code = response.status_code
        print(status_code)

        return status_code     
    

def main():
    print('hello')
    logger = logG()
    print(logger.log('myVar',3.2))

if __name__ == "__main__":
  main()