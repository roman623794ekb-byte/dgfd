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
# Настройки для GitHub Actions
# =============================================================================

# Указываем точный путь к sdkmanager в актуальных образах Ubuntu
android.sdkmanager_path = /usr/local/lib/android/sdk/cmdline-tools/latest/bin/sdkmanager

# Позволяем buildozer самому управлять SDK в локальной папке
# android.sdk_path = 

# Стабильные версии API для сборки
android.api = 33
android.minapi = 21
android.ndk_api = 21

# Автоматически принимать лицензии
android.accept_sdk_license = True

# (list) Разрешения
android.permissions = INTERNET

# (string) Ориентация экрана
orientation = portrait

# [отладочные настройки]
log_level = 2
warn_on_root = 1
