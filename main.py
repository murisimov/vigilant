from sys import exit
from time import sleep

from config import headquarters, settings
from helpers import log_reader, form_body, send


def main():
    run = True
    print "Starting"
    try:
        # TODO: Implement headquarters report
        while run:
            for name, observable in settings.items():
                result = log_reader(observable['log'], observable['patterns'])
                if result:
                    body = form_body(observable['remote'], result)
                    response = send(observable['remote']['url'], body)
                    print response
            else:
                sleep(10)
    except (SystemExit, KeyboardInterrupt):
        print "Shutting down"
        run = False
        exit(0)
    except Exception as e:
        print e


if __name__ == "__main__":
    main()
