[app]

# (str) Title of your application
title = Monitor

# (str) Package name
package.name = monitor

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.2.1,requests,plyer,android,urllib3,werkzeug,flask,opencv-python,pillow,pyjnius

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT_TO_PY

# (str) OSX App bundles are not a "executable", link a main.pyo instead
#osx.python_path =

# (str) OSX App bundles are not a "executable", link a main.pyo instead
#osx.kivy_main = main.pyo

# (str) OSX App bundles are not a "executable", link a main.pyo instead
#osx.app_main = main.pyo

# (str) Targeted (Minimum) Android API
android.api = 21

# (str) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 9c

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (str) python-for-android fork to use, defaults to upstream (impact=4) (deprecated)
#p4a.fork = kivy

# (str) python-for-android branch to use, defaults to master (impact=4) (deprecated)
#p4a.branch = master

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
#p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#p4a.local_recipes =

# (str) Filename to the hook for p4a
#p4a.hook =

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap collision)
#p4a.port =

# (str) OUYA Console category in which your app will be listed
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must exist.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (list) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7a/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_mips = libs/android-mips/*.so

# (bool) Indicate whether the screen should stay on
#android.wakelock = False

# (list) Android application meta-data to set (key=value format)
#android.meta_data =

# (list) Android library project to add (will be added in the
# project.properties automatically.)
#android.library_references =

# (list) Android shared libraries which will be added to AndroidManifest.xml using <uses-library> tags (NOT ANDROID STUDIO)
#android.uses_library =

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a

# (int) overrides automatic versionCode computation (full = 1, date = 2, buildozer = 3, vercode = 4)
#android.numeric_version = 1

# (bool) will split the apk to create a 2gb asset file when the apk+obb is too big (BUT YOU CANNOT UPDATE YOUR APP ON PLAY STORE IF YOU USE THIS)
#android.split_apk = False

# (str) APK signing alias
#android.alias =

# (str) APK signing key
#android.key =

# (str) APK signing key password
#android.key_pass =

# (str) APK signing store password
#android.store_pass =

# (str) APK signing store file
#android.keystore =

# (str) APK signing algorithm
#android.signingAlgorithm =

# (str) APK signing digest algorithm
#android.signingDigestAlgorithm =

# (str) APK signing key algorithm
#android.signingKeyAlgorithm =

# (str) APK signing key size
#android.signingKeySize =

# (str) APK signing validity
#android.signingValidity =

# (str) APK signing organization
#android.signingOrganization =

# (str) APK signing organizational unit
#android.signingOrganizationalUnit =

# (str) APK signing country
#android.signingCountry =

# (str) APK signing state
#android.signingState =

# (str) APK signing locality
#android.signingLocality =

# (str) APK signing distinguished name
#android.signingDistinguishedName =

# (str) APK signing not before
#android.signingNotBefore =

# (str) APK signing not after
#android.signingNotAfter =

# (str) APK signing serial number
#android.signingSerialNumber =

# (str) APK signing key usage
#android.signingKeyUsage =

# (str) APK signing extended key usage
#android.signingExtendedKeyUsage =

# (str) APK signing subject alternative name
#android.signingSubjectAlternativeName =

# (str) APK signing issuer alternative name
#android.signingIssuerAlternativeName =

# (str) APK signing issuer
#android.signingIssuer =

# (str) APK signing subject
#android.signingSubject =

# (str) APK signing certificate
#android.signingCertificate =

# (str) APK signing certificate chain
#android.signingCertificateChain =

# (str) APK signing private key
#android.signingPrivateKey =

# (str) APK signing public key
#android.signingPublicKey =

# (str) APK signing signature
#android.signingSignature =

# (str) APK signing signature algorithm
#android.signingSignatureAlgorithm =

# (str) APK signing signature digest algorithm
#android.signingSignatureDigestAlgorithm =

# (str) APK signing timestamp
#android.signingTimestamp =

# (str) APK signing timestamp authority
#android.signingTimestampAuthority =

# (str) APK signing timestamp authority certificate
#android.signingTimestampAuthorityCertificate =

# (str) APK signing timestamp authority private key
#android.signingTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority public key
#android.signingTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority signature
#android.signingTimestampAuthoritySignature =

# (str) APK signing timestamp authority signature algorithm
#android.signingTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

# (str) APK signing timestamp authority timestamp authority signature
#android.signingTimestampAuthorityTimestampAuthoritySignature =

# (str) APK signing timestamp authority timestamp authority signature algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureAlgorithm =

# (str) APK signing timestamp authority timestamp authority signature digest algorithm
#android.signingTimestampAuthorityTimestampAuthoritySignatureDigestAlgorithm =

# (str) APK signing timestamp authority timestamp
#android.signingTimestampAuthorityTimestamp =

# (str) APK signing timestamp authority timestamp authority
#android.signingTimestampAuthorityTimestampAuthority =

# (str) APK signing timestamp authority timestamp authority certificate
#android.signingTimestampAuthorityTimestampAuthorityCertificate =

# (str) APK signing timestamp authority timestamp authority private key
#android.signingTimestampAuthorityTimestampAuthorityPrivateKey =

# (str) APK signing timestamp authority timestamp authority public key
#android.signingTimestampAuthorityTimestampAuthorityPublicKey =

