from __future__ import absolute_import
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
        'https://api.darksky.net/forecast/%s/%s,%s' % (
            config['api']['key'],
            config['latitude'],
            config['longitude']
        ),
        params={'extend': 'hourly', 'units': 'si'}
    ).json()

    hours = config['date']['hours']
    start = datetime.time(hours['from'])
    end = datetime.time(hours['to'])

    days = config['date']['days']
    startdate = datetime.date.today() + datetime.timedelta(days=days['from'])
    enddate = datetime.date.today() + datetime.timedelta(days=days['to'])

    fields = config['fields']
    candidates = []

    for item in forecast['hourly']['data']:
        date = datetime.datetime.fromtimestamp(item['time'])

        if (
            startdate <= date.date() <= enddate and
            start <= date.time() <= end and
            all(
                value['from'] <= item[key] <= value['to']
                for key, value in fields.iteritems()
            )
         ):
            candidates.append((date, item))

    return candidates
