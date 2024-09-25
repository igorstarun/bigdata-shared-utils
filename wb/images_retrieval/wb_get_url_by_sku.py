
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


def get_url_by_sku(sku, image_num=1, size='c246x328'):
    """
    Функция возвращает ссылку на картинку товара с WB.

    :param sku: номер SKU
    :param image_num: порядковый номер фотографии в карточке
    :param size: размер картинки (big или c246x328)
    :return: ссылка на товар
    """

    def _get_basket(sku):
        sku_floor = custom_floor(sku / 100000)
        if sku_floor <= 143:
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
        return '18'

    vol = custom_floor(sku / 100000)
    part = custom_floor(sku / 1000)

    return f"https://basket-{_get_basket(sku)}.wbbasket.ru/vol{vol}/part{part}/{sku}/images/{size}/{image_num}.webp"
