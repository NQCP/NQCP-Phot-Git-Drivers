from iSMA_MAC36 import iSMA_MAC36
from logToGraphana import logG

import random
import time
import threading
import tkinter as tk


def main():
    logger = logG()

    while True:
        # Generate a random number
        random_num = random.randint(0, 100)
        print("Random number:", random_num)

        logger.log('test',random_num)

        # Wait for the specified interval [s]
        time.sleep(1)

if __name__ == "__main__":
    main()