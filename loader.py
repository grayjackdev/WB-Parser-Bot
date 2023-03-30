from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dadata import Dadata
from dotenv import load_dotenv
from os import environ
import logging.config

load_dotenv()

from conf_log import logger_settings

logging.config.dictConfig(logger_settings)
logger = logging.getLogger('my_logger')
DADATA_TOKEN = environ.get('DADATA_TOKEN')
BOT_TOKEN = environ.get('BOT_TOKEN')
ADMINS = environ.get('ADMINS')

dadata = Dadata(DADATA_TOKEN)

bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
