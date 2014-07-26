#!/usr/bin/env python

import yaml
import twitter
import forecast


def main():
    with open("config.yaml", 'r') as f:
        config = yaml.load(f)

    candidates = forecast.get_candidates(config['forecastio'])

    if len(candidates) >= config['trigger']['hours']:
        print "%d hours of wind, posting to twitter" % len(candidates)
        twitter.post(config['twitter'], config['message'] % len(candidates))
    else:
        print "Not enough wind. %d hours" % len(candidates)

if __name__ == '__main__':
    main()
