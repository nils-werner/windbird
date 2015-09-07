#!/usr/bin/env python

import os
import yaml
import twitter
import forecast
import pushbullet


def wind_bft(val):
    thresholds = (
        0.3, 1.5, 3.4, 5.4, 7.9, 10.7, 13.8, 17.1, 20.7, 24.4, 28.4, 32.6
    )

    for bft, ms in enumerate(thresholds):
        if val < ms:
            return bft

    return len(thresholds)


def wind_kts(val):
    return val * 3.6 / 1.852


def main():
    root = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(root, "config.yaml"), 'r') as f:
        config = yaml.load(f)

    candidates = forecast.get_candidates(config['forecastio'])
    minspeed = wind_kts(min(candidates, key=lambda x: x[1])[1])

    print "%d hours, max %d kts" % (len(candidates), minspeed)

    if len(candidates) >= config['trigger']['hours']:
        print "Above threshold. Posting."
        print config['message'] % (len(candidates), minspeed)

        try:
            twitter.post(
                config['twitter'],
                config['message'] % (len(candidates), minspeed)
            )
        except KeyError:
            print "Skipping Twitter"

        try:
            pushbullet.post(
                config['pushbullet'],
                config['message'] % (len(candidates), minspeed)
            )
        except KeyError:
            print "Skipping Pushbullet"

    else:
        print "Below threshold. Skipping."

if __name__ == '__main__':
    main()
