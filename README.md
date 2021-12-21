# Super Simple Static Site Generator in Python

## Overview

Super Simple helps create static websites.  It reads HTML files in a `templates` directory and combines them using Jinja2, and writes the output files to a `site` directory.

The process is a little inverted from a standard static site generator.  There is no content management or list of content files; Super Simple just reads any HTML files in the `templates` directory (as long as they don't start with `.` or `_`), and sends them through Jinja2.  The resulting output files are written to the `site` directory.

The HTML files can `include` partials (which are HTML files that start with the underscore character,  `_`) using the syntax:

```
{% include '_filenameOfPartial.html' %}
```

Super Simple also sets a few variables:

- `output_filename` - the name of the current output file, useful for setting the active page in navigation or the like
- `build_time_iso` - the time the site was built, in ISO 8601 format
- `build_time_human` - the time the site was built, in a general human readable format
- `build_time_us` - the time the site was built, in a United States-oriented human readable format

## Installation

Clone the repo.

Install Python requirements:

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Replacing the demo files

There are files for a simple website included in this repository, in the `templates` and `site` directories. You can remove them and replace them with your own.

Pro tip: add the filenames of the HTML files in your `templates` directory to the `.gitignore` file in `site`. That will help keep you from getting confused about which HTML files to edit.

## Running Locally

Change to this directory, the one containing the `supersimple.py` script.

Set the environment (only need to do once per terminal session):

```shell
source venv/bin/activate
```

Run the script:

```shell
./supersimple.py
```

To see what flags you can use with Super Simple, use `--help`:

```shell
./supersimple.py --help
```

The files in the templates directory will be read and processed, and written to the site directory.  You can open the HTML files in the site directory with your web browser to see how they look.

## Deploying to Netlify

You can point Netlify to a Git repo containing the Super Simple files and the `templates` and `site` directories.

The included `netlify.toml` file will set up everything necessary for Netlify to run Super Simple and deploy the site.  Be sure to change the "publish" directive if you use an output directory other than `site`.

## License and Acknowledements

Super Simple is free and unencumbered software released into the public domain. See the UNLICENSE file for details.

Central repository: <https://github.com/peterkaminski/supersimple>

The sample site included with Super Simple includes the "Me" website from <https://html5rocket.github.io/> and a favicon set that uses graphics from Twitter Twemoji.  See the "administration/me" and "administration/favicon" directories for more information.
