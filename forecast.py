#!/usr/bin/env python

import requests
import datetime
import tweepy


def get_next_weekday(weekday):
    """
    @startdate: given date, in format '2013-05-25'
    @weekday: week day as a integer, between 0 (Monday) to 6 (Sunday)
    """
    d = datetime.date.today()
    t = datetime.timedelta((7 + weekday - d.weekday()) % 7)
    return (d + t)


def get_candidates(config):
    start = get_next_weekday(4)

    forecast = requests.get(
        'http://api.forecast.io/forecast/%s/%s,%s' % (
            config['api']['key'],
            config['latitude'],
            config['longitude']
        ),
        params={'extend': 'hourly', 'units': 'si'}
    ).json()

    start = datetime.time(config['range']['time']['from'])
    end = datetime.time(config['range']['time']['to'])

    startdate = datetime.date.today() + datetime.timedelta(days=config['range']['date']['from'])
    enddate = datetime.date.today() + datetime.timedelta(days=config['range']['date']['to'])

    startspeed = config['range']['speed']['from']
    endspeed = config['range']['speed']['to']

    candidates = []

    for item in forecast['hourly']['data']:
        date = datetime.datetime.fromtimestamp(item['time'])

        if startdate <= date.date() <= enddate:
            if start <= date.time() <= end:
                if startspeed <= item['windSpeed'] <= endspeed:
                    candidates.append((date, item['windSpeed']))

    return candidates
