#!/usr/bin/env python

# Super Simple Static Site Generator in Python v1.1.1 - https://github.com/peterkaminski/supersimple
# This is free and unencumbered software released into the public domain.

import argparse
import os
import traceback

import datetime
from pathlib import Path

import jinja2

# set up argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Assemble static website.')
    parser.add_argument('--site', '-s', default="site", metavar="SITE_DIR", help='directory for website output')
    parser.add_argument('--templates', '-t', default="templates", metavar="TEMPLATES_DIR", help='directory for HTML templates to process')
    parser.add_argument('--quiet', '-q', action='store_true', help="don't print progress messages")
    return parser

# set up a Jinja2 environment
def jinja2_environment(path_to_templates):
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path_to_templates)
    )

def main():
    argparser = init_argparse();
    args = argparser.parse_args();

    # remember paths
    dir_site = os.path.abspath(args.site)
    dir_templates = os.path.abspath(args.templates)
    if not args.quiet:
        print(f"Directory for HTML templates to process: '{dir_templates}'")
        print(f"Directory for website output: '{dir_site}'")
        print()

    # get a Jinja2 environment
    j = jinja2_environment(dir_templates)

    # remember build time
    build_time = datetime.datetime.now(datetime.timezone.utc)
    build_time_iso = build_time.isoformat()
    build_time_human = build_time.strftime("%A, %d %B %Y, at %H:%M UTC")
    build_time_us = build_time.strftime("%A, %B %d, %Y at %H:%M UTC")

    # render the site
    try:
        for root, dirs, files in os.walk(dir_templates):
            files = [f for f in files if not f.startswith(('.', '_'))]
            path = root[len(dir_templates)+1:]
            if not os.path.exists(Path(dir_site) / path):
                os.mkdir(Path(dir_site) / path)
            for file in files:
                if file.lower().endswith('.html'):
                    if not args.quiet:
                        print(f"Reading '{Path(root) / file}'")

                    html = j.get_template(str(Path(path) / file)).render(
                        output_filename=file,
                        build_time_iso = build_time_iso,
                        build_time_human = build_time_human,
                        build_time_us = build_time_us,
                    )
                    (Path(dir_site) / path / file).write_text(html)

                    if not args.quiet:
                        print(f"Wrote '{Path(dir_site) / path / file}'")
                        print()

    except Exception as e:
        traceback.print_exc(e)

    if not args.quiet:
        print("Done.")

if __name__ == "__main__":
    exit(main())
