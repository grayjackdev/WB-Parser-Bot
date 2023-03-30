from .number import IsNumber
from loader import dp

if __name__ == 'filters':
    dp.filters_factory.bind(IsNumber)
