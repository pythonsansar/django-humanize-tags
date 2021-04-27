from django.shortcuts import render
import datetime


def homepage(request):
    current_time = datetime.datetime.now()
    context = {
        # apnumber
        'ap_first': 1,
        'ap_second': 7,
        # intcomma
        'comma_first': 1234,
        'comma_second': 123456.7,
        # intword
        'word_first': 10000000,
        'word_second': 1500000000,
        # naturalday
        'current_time': current_time,
        'day_first': current_time,
        'day_second': current_time - datetime.timedelta(days=1),
        'day_third': current_time + datetime.timedelta(days=1),
        # naturaltime
        'time_first': current_time - datetime.timedelta(days=7),
        'time_second': current_time + datetime.timedelta(days=600),
        # ordinal
        'ord_first': 7,
        'ord_second': 41,
    }
    return render(request, 'test.html', context)
