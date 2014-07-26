WindBird
========

A small Python application that posts to Twitter if the wind conditions at a certain location
are good for sailing or surfing.

Installation
------------

 1. Create developer account on <https://developer.forecast.io/>
 2. Register application API key and Access Token on <https://apps.twitter.com/>
 3. Create virtualenv
 4. Install dependencies

        pip install -r requirements.txt

 5. Copy `config_example.yaml` to `config.yaml` and adjust its values
 6. Create crontab entry to run `main.py` once a day

        SHELL=/bin/bash
        0 12 * * * source /path-to-env/bin/activate && /path-to-env/windbird/main.py > /path-to-env/windbird/main.log
