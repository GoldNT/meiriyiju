import requests


def meiriyiju():
    #优化版本
    url = "http://open.iciba.com/dsapi/"
    try:
        r = requests.get(url, timeout=5)  # 设置超时时间以防止无限等待
        r.raise_for_status()  # 检查请求是否成功
        try:
            data = r.json()
            content = data.get('content')  # 使用 get 方法可以避免 KeyError 并提供默认值\
            note = data.get('note')
            if content is None:
                print("Warning: 'content' key not found in the response.")
            if note is None:
                print("Warning: 'note' key not found in the response.")
            return note,content
        except ValueError:
            print("Error: Unable to parse JSON from the response.")
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")

    #原本
    # url = "http://open.iciba.com/dsapi/"
    # r = requests.get(url)
    # content = r.json()['content']
    # note = r.json()['note']
    return note,content

note,content = meiriyiju()

def mydata():
    mydata = {
        'text': content,
        'desp': '每日一句' + '<br>'   # 通知的描述，包含公告内容
                '原文:' + content + '<br>'  # 公告的链接
                '翻译：' + note  # 公
    }
    requests.post('你的token.send', data=mydata)
    print(content,note)
    print("发送成功")

meiriyiju()
mydata()