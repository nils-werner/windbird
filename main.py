#!/usr/bin/env python

import os
import yaml
import twitter
import forecast


def main():
    root = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(root, "config.yaml"), 'r') as f:
        config = yaml.load(f)

    candidates = forecast.get_candidates(config['forecastio'])

    if len(candidates) >= config['trigger']['hours']:
        print "%d hours of wind, posting to twitter" % len(candidates)

        try:
            twitter.post(config['twitter'], config['message'] % len(candidates))
        except KeyError:
            pass

        try:
            pushbullet.post(
                config['pushbullet'], config['message'] % len(candidates)
            )
        except KeyError:
            pass

    else:
        print "Not enough wind. %d hours" % len(candidates)

if __name__ == '__main__':
    main()
