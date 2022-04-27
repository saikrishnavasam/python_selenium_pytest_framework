import logging
import os

from config import constants

DOWNLOADS_DIR = constants.Files.DOWNLOADS_FOLDER
abs_path = os.path.abspath('.')
downloads_path = os.path.join(abs_path, DOWNLOADS_DIR)


def get_downloads_folder():
    return downloads_path


def create_downloads_folder():
    if not os.path.exists(downloads_path):
        try:
            logging.info('Creating downloads folder')
            os.mkdir(downloads_path)
        except Exception:
            pass
    else:
        logging.info('Downloads folder already exists')


def get_recently_downloaded_filename():
    logging.info(os.listdir(downloads_path))
    filename = max([f for f in os.listdir(downloads_path)], key=downloads_path.getmtime)
    logging.info(filename)
    return filename
