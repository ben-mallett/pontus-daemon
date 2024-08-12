# Pontus Daemon

Uploads sensor data and exposes a streaming server. Intended to interface with `pontus`

## Getting Set Up

- Whitelist IP of device in GCP
- Install the `balena` CLI
- Create a device (and fleet if needed) in balena
- Flash device with balena image
- Run `balena deploy`

## Required Hardware Setup

This code has been tested and runs on a Raspberry Pi with a PiCam connected to the default video input. 
