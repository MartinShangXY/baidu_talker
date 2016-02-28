from core.config import Config
from core.talker import Talker

if __name__ == '__main__':
    conf = Config('your client_id', 'your client_secret')
    tk = Talker(conf)
    tk.talk('aa')
