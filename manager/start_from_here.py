from core.config import ApiConfig
from core.talker import Talker

if __name__ == '__main__':
    conf = ApiConfig('your client_id', 'your client_secret')
    tk = Talker(conf)
    re = tk.talk('你口你口妮')
    re.to_file()
