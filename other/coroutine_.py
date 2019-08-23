# -*- coding: utf-8 -*-
import asyncio
import requests



async def download(url):
    await asyncio.sleep(1)
    resp = requests.get(url)
    return resp.content, resp.status_code


@asyncio.coroutine
def save(url, filename):
    print('%s -正在下载中' % url)
    content, code = yield from download(url)
    print(url, code)
    yield from write_file(filename, content)
    print('%s -保存成功' % url)


@asyncio.coroutine
def write_file(filename, content):
    with open(filename, 'wb') as f:
        f.write(content)
    print('%s write OK!' % filename)


if __name__ == '__main__':
    # 获取事件循环器对象
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([
        save('https://www.baidu.com', 'baidu.txt'),
        save('https://www.imzhangao.com', 'imzhangao.txt'),
        save('https://jd.com', 'jd.txt'),
        save('https://mail.qq.com', 'mail.txt')
    ]))
