import requests
class Request:
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                      'Chrome/88.0.4324.190 Safari/537.36',
        'accept': '*/*'}
    def __init__(self, URL):
        self.URL = URL

    def get_html(self, params=None):
        r = requests.get(self.URL, headers=self.HEADERS, params=params)
        return r.text