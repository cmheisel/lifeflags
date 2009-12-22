pip -q install pywatch
pywatch "django-admin.py test --settings=lifeflags.conf.test.settings" lifeflags/flags/*.py
