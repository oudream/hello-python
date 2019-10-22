#!/usr/bin/env bash

# --no-index - Ignore package index (only looking at --find-links URLs instead).
# -f, --find-links <URL> - If a URL or path to an html file, then parse for links to archives.
# If a local path or file:// URL that's a directory, then look for archives in the directory listing.
pip install -r requirements.txt --no-index --find-links file:///tmp/packages
