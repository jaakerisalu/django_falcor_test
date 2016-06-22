#bind = "0.0.0.0:8000"
bind = "unix:/tmp/gunicorn_django_falcor_test.sock"

workers = 2
proc_name = "django_falcor_test"
#loglevel = 'debug'
