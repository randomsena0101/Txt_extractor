#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6991599062:AAFwn6ubznUzL51Wi5jH0EaODVyck3w4atQ")
    API_ID = int(os.environ.get("API_ID", "27862677"))
    API_HASH = os.environ.get("API_HASH", "e343ce2c81b2b6c2c0d6bee58284e3bd")
    AUTH_USERS = os.environ.get("AUTH_USERS", "5925499677")
