from core.config import SoftConfig


class Sentence:
    text = None
    response = None

    def __init__(self, text, response):
        self.response = response
        self.text = text

    def to_file(self):
        ctype = self.response.headers['Content-type'].lower().split('/')
        fname = SoftConfig.mp3_dict + self.text + '.' + ctype[1]
        fp = open(fname, 'wb')
        if ('audio' == ctype[0]):
            fp.write(self.response.content)
            fp.close()
            return open(fname, 'rb')
        else:
            err = 'No audio file, this Content-type: ' + ctype[0] + '/' + ctype[1]
            fp.close()
            raise TypeError(err)
