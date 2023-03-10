# Тестовое задание на позицию Python Developer
# Белькевич Александр Геннадьевич

# Задания
## Часть 1
```text
Дан массив связей пользователей. Вам необходимо реализовать функцию,
которая принимает на вход три аргумента: информация о связях, как кортеж (tuple)
кортежей, первое имя (str), второе имя (str). Функция должна возвращать True, если
связь между любыми двумя заданными пользователями существует, например, если у
двух пользователей есть общие друзья или у их друзей есть общие друзья и т.д., иначе
False
```

## Часть №2
```text
1. Изначально необходимо отследить трафик с <secret site> и найти HTTP
запрос, который в JSON формате присылает данные о бренде и название
артикула. 
2. Далее необходимо реализовать API принимающее файл формата xlsx с
артикулами (артикулы должны вводиться построчно в первой колонке) или
один артикул (не в файле, а исключительно одно значение). В API должно быть
два инпута: файл или одно значение, передаваться должно что-то одно.
3. API должно асинхронно взаимодействовать с найденным HTTP запросом в
первом пункте и получать данные о карточке товара. Из полученных данных
необходимо сделать PyDantic объект.
4. Успешным результатом работы API является возврат данных о бренде и
названии артикула в JSON формате. Пример: информация об одном артикуле -
{"article": 123, "brand": "brand", "title": "Title"}; артикулы из файла - [{"article": 1,
"brand": "Brand1", "title": "Title1"}, {"article": 2, "brand": "Brand2", "title": "Title2"}]

```

## Копируем и настраиваем переменную окружения
```bash
cp .env.example .env
```
## Создание переменной окружения и установка зависимостей
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Удаление БД, запуск миграций
```bash
rm db.sqlite3
python3 manage.py makemigrations                 
python3 manage.py migrate
```

## Запуск сервера (флаг --reload, если потребуется вносить изменения в файлы)
```bash
uvicorn api_sync_wildberries.asgi:application
```

## Работа с проектом
```bash
open http://127.0.0.1:8000
```
