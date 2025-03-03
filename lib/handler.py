import logging

logger = logging.getLogger(__name__)

#create handler...
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')

# Level and format...
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning("This is a Warning")
logger.error("This is an Error")
