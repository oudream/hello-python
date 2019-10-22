#!/usr/bin/env bash

python -m pip install SomePackage==1.0.4    # specific version
python -m pip install "SomePackage>=1.0.4"  # minimum version

pip help install
pip help list

# --no-index - Ignore package index (only looking at --find-links URLs instead).
# -f, --find-links <URL> - If a URL or path to an html file, then parse for links to archives.
# If a local path or file:// URL that's a directory, then look for archives in the directory listing.
pip install -r requirements.txt --no-index --find-links file:///tmp/packages

Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  help                        Show help for commands.
