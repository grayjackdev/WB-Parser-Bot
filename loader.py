from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from os import environ
import logging.config

load_dotenv()

for i in logging.Logger.manager.loggerDict:
    logging.getLogger(i).setLevel(logging.CRITICAL)

from conf_log import logger_settings

logging.config.dictConfig(logger_settings)
logger = logging.getLogger('my_logger')

DADATA_TOKEN = environ.get('DADATA_TOKEN')
BOT_TOKEN = environ.get('BOT_TOKEN')
ADMINS = environ.get('ADMINS')

bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())



