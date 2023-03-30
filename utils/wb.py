import httpx
from httpx import HTTPError, HTTPStatusError
from fake_useragent import UserAgent
from loader import logger


class Wildberries:
    def __init__(self, latitude, longitude, addr, product, max_items):
        useragent = UserAgent().chrome
        self.headers = {
            'User-Agent': useragent,
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br'
        }
        self.latitude = latitude
        self.longitude = longitude
        self.addr = addr
        self.product = product
        self.max_items = max_items

    async def get_geo_info(self):
        url = f'https://user-geo-data.wildberries.ru/get-geo-info?currency=RUB&latitude={self.latitude}&longitude={self.longitude}&locale=ru&address={self.addr}'
        try:
            async with httpx.AsyncClient() as client:
                r = await client.get(url, headers=self.headers)
        except (HTTPError, HTTPStatusError):
            logger.exception(f'Произошла ошибка при получении геоданных с wb. Коорд: {self.latitude} {self.longitude} ; {self.addr}')
            return False

        xinfo = r.json().get('xinfo')

        if xinfo:
            self.xinfo = xinfo
            return True
        return False


