#!/usr/bin/env python

from __future__ import absolute_import
import os
import yaml
import argparse
from . import twitter
from . import forecast
from . import telegram
from . import units


targets = {
    'twitter': twitter,
    'telegram': telegram,
}


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'config',
        help='Config filename',
        default='config.yaml',
        nargs='?',
    )
    args = parser.parse_args(args)

    with open(os.path.join(args.config), 'r') as f:
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
