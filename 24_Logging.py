#  Logging in Python is a way to track events that happen while a program runs. It helps developers debug, monitor, and record the behavior of applications. 

# DEBUG: This is a debug message
# INFO: This is an info message
# WARNING: This is a warning message
# ERROR: This is an error message
# CRITICAL: This is a critical message


import logging

# Configure logging...
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
# By default it doesn't print msgs above warning, that's why we did that basic configuration...

# Log messages :

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message\n")

from lib import helper
print("\n")
from lib import handler





# Advanced Logging :---

# For more complex applications, you can use loggers, handlers, and formatters to manage logs more efficiently.

# Loggers – Generate log messages.
# Handlers – Determine where logs should go (console, file, etc.).
# Formatters – Define the format of log messages.

