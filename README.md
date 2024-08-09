
# Shared Utils

Этот репозиторий содержит общие утилиты и функции, которые могут быть переиспользованы в различных проектах.

## Структура

- **wb/images_retrieval**: Содержит функции, связанные с получением изображений товаров с Wildberries (WB).
  - `wb_get_url_by_sku.py`: Предоставляет функцию для генерации URL изображений товаров по SKU.

## Использование

### Импорт функций

Вы можете импортировать функции из этого репозитория в свои проекты следующим образом:

```python
from wb.images_retrieval.wb_get_url_by_sku import get_url_by_sku

# Пример использования:
sku = 149564395
url = get_url_by_sku(sku)
print(url)
```

### Динамическое получение функции

Также вы можете динамически загружать функцию `get_url_by_sku` с помощью `requests` и использовать кэшированную версию в случае недоступности удаленной функции:

```python
import os
import requests

def load_remote_function(url, local_cache_path="get_url_by_sku_cached.py"):
    try:
        # Попытка загрузки удаленного кода
        response = requests.get(url)
        response.raise_for_status()  # Проверка статуса ответа
        code = response.text
        
        # Сохранение кода локально для кэширования
        with open(local_cache_path, "w") as f:
            f.write(code)
        print("Удаленный код успешно загружен и кэширован.")
        
    except (requests.RequestException, IOError) as e:
        print(f"Ошибка при загрузке удаленного кода: {e}")
        print("Попытка использовать кэшированную версию.")
        
        # Проверка наличия кэшированной версии
        if os.path.exists(local_cache_path):
            with open(local_cache_path, "r") as f:
                code = f.read()
            print("Кэшированная версия успешно загружена.")
        else:
            raise RuntimeError("Не удалось загрузить удаленный код и кэшированная версия отсутствует.")
    
    # Выполнение загруженного кода
    exec(code, globals())

# Пример использования
url = "https://gitlab.mpstats.io/bigdata/shared-utils/-/raw/main/wb/images_retrieval/wb_get_url_by_sku.py?inline=false"
load_remote_function(url)

# Теперь функция доступна
print(get_url_by_sku(149564395))
```

### Описание функций

- **`get_url_by_sku(sku, image_num=1, size='c246x328')`**: 
  - Генерирует URL для изображения товара на Wildberries.
  - **Параметры**:
    - `sku` (int): Номер SKU товара.
    - `image_num` (int): Номер изображения в карточке товара (по умолчанию 1).
    - `size` (str): Размер изображения (по умолчанию `'c246x328'`).
  - **Возвращает**: Строку, содержащую URL изображения товара.
