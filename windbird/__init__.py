#!/usr/bin/env python

from __future__ import absolute_import
import os
import yaml
from . import twitter
from . import forecast
from . import pushbullet
from . import units


targets = {
    'twitter': twitter,
    'pushbullet': pushbullet,
}


def main():
    with open(os.path.join("config.yaml"), 'r') as f:
        config = yaml.load(f)

    candidates = forecast.get_candidates(config['forecastio'])

    print "%d hours" % len(candidates)

    if len(candidates) >= config['trigger']['hours']:
        minspeed = units.wind_kts(
            min(
                candidates,
                key=lambda x: x[1]['windSpeed']
            )[1]['windSpeed']
        )

        print "Above threshold. Posting."
        print config['message'] % (len(candidates), minspeed)

        for key, module in targets.iteritems():
            try:
                config[key]
            except KeyError:
                print "Config missing, skipping %s" % key
                continue

            try:
                module.post(
                    config[key],
                    config['message'] % (len(candidates), minspeed)
                )
            except:
                print "Error during %s" % key

    else:
        print "Below threshold. Skipping."

if __name__ == '__main__':
    main()
