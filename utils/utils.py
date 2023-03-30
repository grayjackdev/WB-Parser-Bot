from loader import dadata, logger
from httpx import HTTPStatusError, HTTPError


def get_addr(latitude, longitude):
    try:
        result = dadata.geolocate(name="address", lat=latitude, lon=longitude)
    except (HTTPError, HTTPStatusError) as error:
        logger.exception(f'Ошибка при получении адреса по координатам: {latitude} {longitude}')
        return False

    return result
