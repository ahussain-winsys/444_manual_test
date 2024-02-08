#!/bin/bash

sudo iw wlan0 scan | grep -B 9 "WSGuest" | grep "signal"