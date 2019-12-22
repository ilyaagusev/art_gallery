<h1> Обработчик изображений </h1>

Данная программа написана в учебных целях в рамках курса dvmn.org "Знакомство с Python"
Программа разделяет тестовое изображение по цветовым каналам, а после собирает со смещением для получения эффекта "Энди Уорхолла"

<h2> Запуск скрипта </h2>

Убедитесь, что директория в которую вы распковали архив, имеет доступ к интернет и содержит следующие файлы:

Название файла          | Содержание файла
------------------------|-----------------------------------
blend_image.py          | Функция объединяющая 2 изображения со смещением 
crop_image.py           | Функция обрезающая изображение по указанному числу пикселей
image_info.py           | Функция возвращающая информацию по изображению
main.py                 | Основной файл обрабатывающий картинку по условиям указанным в задании
merge_image_by_color.py | Функция объединяющая изображения в красном, зеленом и синем канале в RGB изображение
README.md               | Данный файл
requirements.txt        | Файл с зафисимостями
split_image_by_color.py | Функция разделяющая RGB изображение на 3 цветовых канала  



<h2> Требования </h2>

Запуск данного скрипта требует установки Python 3.7.4
и установленной библиотеки Pillow 6.2.1

<h2>Запуск</h2>

Запуск осуществляется через консоль командой: 

    pip install -r reaurements.txt
    python main.py

