from grafanaLogger import GrafanaLogger

import random
import time

# User ID and API Key for Grafana account created with Peter Granum's email
# The logging class is set up to log to this account by default, so the arguments are only added here for demonstration
USER_ID = 1545635
API_KEY = "glc_eyJvIjoiMTEwODkyOCIsIm4iOiJzdGFjay05MTU0MjEtaW50ZWdyYXRpb24tbnFjcHBob3QiLCJrIjoiaDg5NnJiMTlQZTI2NzhWQmxVZDJ3SXlNIiwibSI6eyJyIjoicHJvZC1ldS1ub3J0aC0wIn19"

LOGGING_INTERVAL = 5 # in seconds

logger = GrafanaLogger(USER_ID,API_KEY)

while True:
    # Generate a random number to simulate data acquisition
    random_number = random.randint(0, 100)
    print(random_number)

    # Log the data to Grafana
    logger.log('myVarRand2',random_number)
    
    # Wait
    time.sleep(LOGGING_INTERVAL)