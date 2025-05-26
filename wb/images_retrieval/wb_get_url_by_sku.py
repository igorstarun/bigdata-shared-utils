
def custom_floor(value):
    """
    Возвращает наибольшее целое число, которое не превышает данное значение.

    :param value: Число, для которого нужно найти целую часть.
    :return: Целое число, не превышающее value.
    """
    int_value = int(value)
    if value < 0 and value != int_value:
        return int_value - 1
    return int_value


def get_url_by_sku(sku: int, image_num: int = 1, size: str = 'c246x328') -> str:
    """
    Формирует ссылку на картинку товара Wildberries.

    :param sku:   SKU товара
    :param image_num: номер картинки в карточке (начинается с 1)
    :param size:  размер изображения, например 'big' или 'c246x328'
    :return:      URL изображения
    """

    def _get_basket(sku: int) -> str:
        """
        Определяет номер корзины («basket-XX») по SKU.

        :param sku: SKU товара
        :return:    строка с номером корзины, всегда две цифры
        """
        sku_floor = custom_floor(sku / 100_000)

        if 0 <= sku_floor <= 143:
            return '01'
        elif sku_floor <= 287:
            return '02'
        elif sku_floor <= 431:
            return '03'
        elif sku_floor <= 719:
            return '04'
        elif sku_floor <= 1007:
            return '05'
        elif sku_floor <= 1061:
            return '06'
        elif sku_floor <= 1115:
            return '07'
        elif sku_floor <= 1169:
            return '08'
        elif sku_floor <= 1313:
            return '09'
        elif sku_floor <= 1601:
            return '10'
        elif sku_floor <= 1655:
            return '11'
        elif sku_floor <= 1919:
            return '12'
        elif sku_floor <= 2045:
            return '13'
        elif sku_floor <= 2189:
            return '14'
        elif sku_floor <= 2405:
            return '15'
        elif sku_floor <= 2621:
            return '16'
        elif sku_floor <= 2837:
            return '17'
        elif sku_floor <= 3053:
            return '18'
        elif sku_floor <= 3269:
            return '19'
        elif sku_floor <= 3485:
            return '20'
        elif sku_floor <= 3701:
            return '21'
        elif sku_floor <= 3917:
            return '22'
        elif sku_floor <= 4133:
            return '23'
        elif sku_floor <= 4349:
            return '24'
        elif sku_floor <= 4565:
            return '25'
        elif sku_floor <= 4877:
            return '26'
        elif sku_floor <= 5189:
            return '27'
        elif sku_floor <= 5501:
            return '28'
        # Если когда-то появятся новые бакеты — по умолчанию оставляем последний
        return '28'

    vol  = custom_floor(sku / 100_000)
    part = custom_floor(sku /   1_000)

    basket = _get_basket(sku)
    return f"https://basket-{basket}.wbbasket.ru/vol{vol}/part{part}/{sku}/images/{size}/{image_num}.webp"
