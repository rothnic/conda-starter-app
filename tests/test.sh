#!/bin/bash

echo conda info

py.test /app/tests

pylint example_conda_app --rcfile=/app/.pylintrc \
  --ignore=_version.py
