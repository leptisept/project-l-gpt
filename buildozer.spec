[app]
# Название приложения, как оно будет отображаться на устройстве.
title = Life Game

# Имя пакета (только строчные латинские буквы без пробелов).
package.name = lifegame

# Домен пакета. Можно указать свой домен или использовать org.example.
package.domain = org.example

# Каталог, где лежат исходники (точка означает текущую папку).
source.dir = .

# Основной файл приложения.
source.main = main.py

# Расширения файлов, включаемые в пакет.
source.include_exts = py,png,jpg,kv,atlas

# Версия приложения.
version = 1.0.0

# Ориентация экрана (portrait, landscape или all).
orientation = portrait

# Разрешения Android (при необходимости добавьте нужные разрешения).
android.permissions = INTERNET

# Список зависимостей. Здесь указаны Python 3 и Kivy.
requirements = python3,kivy

# (Опционально) Файл иконки приложения. Укажите путь к своей иконке, если есть.
# icon.filename = %(source.dir)s/icon.png

[buildozer]
# Уровень логирования (рекомендуется 2).
log_level = 2

# Не запускать сборку от имени root.
warn_on_root = 1

[android]
# Использовать для хранения данных приложения приватное хранилище.
android.private_storage = True

# Android API, используемый для сборки.
android.api = 33

# Минимальная поддерживаемая версия API.
android.minapi = 21

# Версия Android SDK, которая будет использоваться.
android.sdk = 33

# Версия Android NDK (обычно 19b для совместимости).
android.ndk = 19b

# Минимальный NDK API.
android.ndk_api = 21

# Точка входа в приложение (обычно не меняется).
android.entrypoint = org.kivy.android.PythonActivity

# Поддерживаемые архитектуры. Можно указывать несколько вариантов через запятую.
android.arch = ar
meabi-v7a, arm64-v8a

requirements = python3,kivy,numpy
