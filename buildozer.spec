[app]

# (string) Title of your application
title = My Application

# (string) Package name
package.name = myapp

# (string) Package domain (needed for android packaging)
package.domain = org.example

# (string) Source code where the main.py lives
source.dir = .

# (string) Application version
version = 0.1

# (list) Application requirements
requirements = python3==3.11.16, hostpython3==3.11.16, kivy

# (string) Custom NDK version and Python version
p4a.python_version = 3.11

# =============================================================================
# Настройки путей для GitHub Actions (решают ошибку "Aidl not found")
# =============================================================================

# Указываем Buildozer использовать предустановленный в Ubuntu SDK вместо скачивания своего
android.sdk_path = /usr/local/lib/android/sdk

# Рекомендуемые параметры API для стабильной сборки Kivy
android.api = 33
android.minapi = 21
android.ndk_api = 21

# (bool) Использовать ли автоматическое принятие лицензий
android.accept_sdk_license = True

# (list) Разрешения (добавьте нужные, если требуются)
android.permissions = INTERNET

# (string) Ориентация экрана
orientation = portrait

# [отладочные настройки]
log_level = 2
warn_on_root = 1
