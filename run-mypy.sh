#!/usr/bin/env bash
set -o errexit
cd "$(dirname "$0")"
pip install --editable . --index-url https://custom-index-url.com/simple --retries 1 --no-input --quiet
mypy --package acme --namespace-packages
