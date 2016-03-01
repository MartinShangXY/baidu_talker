from core.config import ApiConfig
from core.talker import Talker

if __name__ == '__main__':
    # 初始化配置
    conf = ApiConfig('your client_id', 'your client_secret')
    # 实例化一个讲述人
    tk = Talker(conf)
    # 获取讲话结果
    re = tk.talk('你口你口妮')
    # 保存音频文件
    re.to_file()
