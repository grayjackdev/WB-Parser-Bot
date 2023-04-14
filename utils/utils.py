from loader import dadata, logger
from httpx import HTTPStatusError, HTTPError
from openpyxl import Workbook
from openpyxl.styles import Font
from io import BytesIO


def get_addr(latitude, longitude):
    try:
        result = dadata.geolocate(name="address", lat=latitude, lon=longitude)
    except (HTTPError, HTTPStatusError):
        logger.exception(f'Ошибка при получении адреса по координатам: {latitude} {longitude}')
        return False

    return result


def form_excel(items):
    buffer = BytesIO()
    wb = Workbook()
    worklist = wb.active

    column_dimensions = {"A": 20, "B": 20, "C": 60, "G": 15}

    for key, value in column_dimensions.items():
        worklist.column_dimensions[key].width = value

    worklist.append(['Артикул', 'Бренд', 'Наименование', 'Стоимость', 'Рейтинг', 'Отзывы', 'Ссылка'])
    index = 0
    for row in worklist.iter_rows(min_row=2, max_row=len(items), max_col=7):
        item = items[index]
        id, brand, title, price = item.get('id'), item.get('brand'), item.get('name'), item.get('salePriceU')
        rating, feedbacks = item.get('rating'), item.get('feedbacks')
        price = str(int(price) / 100) + " ₽"
        link = f'https://www.wildberries.ru/catalog/{id}/detail.aspx'

        row_value = [id, brand, title, price, rating, feedbacks, link]

        for i in range(6):
            row[i].value = row_value[i]

        row[6].hyperlink = link
        row[6].value = 'Ссылка'
        row[6].font = Font(color="0000FF", bold=True)
        index += 1

    wb.save(buffer)
    wb.close()
    buffer.seek(0)

    return buffer
