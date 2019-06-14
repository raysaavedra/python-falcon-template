#!/bin/bash

gunicorn -b 0.0.0.0:8001 --reload src.app