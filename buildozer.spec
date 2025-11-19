[app]
title = Spy Monitor
package.name = spymonitor
package.domain = org.spy
source.dir = spymonitor
version = 1.0
requirements = python3,kivy==2.1.0,kivymd,plyer,requests
orientation = portrait
android.api = 30
android.minapi = 21
android.ndk = 25b
android.sdk = 30
android.archs = armeabi-v7a
android.release_artifact = apk
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0

[app:android.permissions]
INTERNET = 1
ACCESS_NETWORK_STATE = 1
ACCESS_FINE_LOCATION = 1
READ_EXTERNAL_STORAGE = 1
WRITE_EXTERNAL_STORAGE = 1
CAMERA = 1
