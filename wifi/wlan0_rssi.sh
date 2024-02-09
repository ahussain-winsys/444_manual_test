#!/bin/bash

sudo ip link set wlan0 up
sudo iw wlan0 scan | grep -B 9 "WSGuest" | grep "signal"
sudo ip link set wlan0 down
