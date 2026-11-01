[app] 

### (str) Title of your application

title = Pygame NumPy AI App 

### (str) Package name

package.name = pygameaiapp 

### (str) Package domain (needed for android packaging)

package.domain = org.example 

### (str) Source code where the main.py lives

source.dir = . 

### (list) Source files to include (leave empty to include all the files)

source.include_exts = py

### (list) List of directories to include (comma separated)

source.include_dirs = ai 

### (str) Application versioning (method 1)

version = 0.1 

### (list) Application requirements

### comma separated e.g. requirements = sqlite3,kivy

requirements = python3, pygame-ce

### (str) Supported orientations (valid options are: landscape, portrait, all)

orientation = all 

### (bool) Indicate if the application should be fullscreen or not

fullscreen = 1 

### (list) Permissions

### permissions = INTERNET

### (int) Target Android API, should be as high as possible.

android.api = 33 

### (int) Minimum API your APK will support.

android.minapi = 21 

### (str) Android NDK version to use

android.ndk = 25b 

### (bool) Use ccache to speed up compilation

android.ccache = 1 

### (str) Format used to package the app for the source distribution (aab or apk)

android.package_format = apk 

### (list) The Android architectures to build for.

android.archs = arm64-v8a, armeabi-v7a 

### (bool) skip data check

android.skip_data_check = False 

[buildozer] 

### (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))

log_level = 2 

### (int) Display warning if buildozer is run as root (0 = False, 1 = True)

warn_on_root = 1
