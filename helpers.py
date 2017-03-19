import json
import re
import urllib2

from os.path import getsize


def log_reader(log, patterns):
    if getsize(log['path']) != log['position']:
        if getsize(log['path']) < log['position']:
            log['position'] = 0

        with open(log['path']) as f:
            f.seek(log['position'])
            result = f.read()
            log['position'] = f.tell()

        # TODO: Implement pattern search here

        return result


def form_body(remote, message):
    body = {
        "unfurl_links": True,
        "channel": remote['channel']
        "username": remote['bot_name'],
        "icon_url": remote['bot_icon'],
        "text": message
    }
    return json.dumps(body)


def send(url, body):

    request = urllib2.Request(
        url, body, {'Content-Type': 'application/json'}
    )
    response = urllib2.urlopen(request)
    result = response.read()
    response.close()
    return result

