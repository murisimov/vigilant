from os.path import getsize

headquarters = {
    'url': '',
    'channel': '',
    'bot_name': '',
    'bot_icon': '',
}

settings = {
    'trailers': {
        'log': {
            'path': '/home/trailers/trailers.log',
            'position': getsize('/home/trailers/trailers.log')
        },
        'patterns': [
            'hey'
        ],
        'remote': {
            'url': '',
            'channel': '',
            'bot_name': '',
            'bot_icon': '',
        }
    },

}
