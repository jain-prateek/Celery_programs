from celery import Celery
import sys
import json
from entry_point import config
app = Celery('periodic', broker="pyamqp://guest@localhost//")
@app.task
def see_you(test):
    print("See you in ten seconds!...."+ test)
    return "hello"
# app.conf.beat_schedule = {
#     "see-you-in-ten-seconds-task": {
#         "task": "periodic.see_you",
#         "schedule": 10.0
#     }
# }
#OR
# Schedule tasks.
#app_celery.conf.beat_schedule = {
#    'load_ticket_data-every-day': {
#        'task': 'tasks.load_ticket_data',
#        # 'schedule': crontab(minute=3, hour=18), # run every day on 6 AM.
#        # 'schedule': crontab(minute=1),
#        'schedule': 50.0,
#        'args': [".", "fuzzy_test.xlsx", "EDLT", "fuzzy_test.xlsx", "true"]
#    }
#}

print("****", config)
app.conf.beat_schedule = config


# if __name__ == "__main__":
#     json_in = json.loads(sys.argv[1])
#     print(json_in)
#
#     app.conf.beat_schedule = json_in

# celery -A periodic beat --loglevel=info

# run the celery worker
#celery -A periodic worker --loglevel=info

#pip install eventlet
#celery -A periodic worker --loglevel=info -l info -P eventlet

# class Test():
#     def __init__(self, input_json):
#         self.input_json = input_json
#
#     def define(self):
#         app.conf.beat_schedule = self.input_json

