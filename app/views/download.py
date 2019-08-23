# -*- coding: utf-8 -*-
import os

from tornado.web import RequestHandler, asynchronous
from tornado.gen import coroutine
from tornado.httpclient import HTTPClient, AsyncHTTPClient, HTTPResponse, HTTPRequest


class DownloadHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # 获取查询参数中的url（下载资源的网址）
        url = self.get_query_argument('url')
        filename = self.get_query_argument('filename', default='index.html')
        # 发起同步请求
        client = HTTPClient()
        # validate_cert 是否验证SSL证书安全连接
        response: HTTPResponse = client.fetch(url, validate_cert=False)
        print(response.body)
        # 保存到static/downloads
        from app import BASE_DIR
        dir = os.path.join(BASE_DIR, 'static\downloads')
        with open(os.path.join(dir, filename), 'wb') as f:
            f.write(response.body)
        self.write('下载成功')


class AsyncDownloadHandler(RequestHandler):
    def save(self, response: HTTPResponse):
        filename = self.get_query_argument('filename', default='index.html')
        # 在回调函数中获取请求的查询参数
        print('%s -下载成功' % response.effective_url)
        # 保存到static/downloads
        print(response.body)
        from app import BASE_DIR
        dir = os.path.join(BASE_DIR, 'static\downloads')
        with open(os.path.join(dir, filename), 'wb') as f:
            f.write(response.body)
        self.write('<br>下载完成,并保存成功！')
        self.finish()

    @asynchronous
    def get(self, *args, **kwargs):
        # 获取查询参数中的url（下载资源的网址）
        url = self.get_query_argument('url')
        # 发起异步请求
        client = AsyncHTTPClient()
        # validate_cert 是否验证SSL证书安全连接
        client.fetch(url, self.save, validate_cert=False)

        self.write('下载中...')


class Async2DownloadHandler(RequestHandler):
    def save(self, response: HTTPResponse):
        filename = self.get_query_argument('filename', default='index.html')
        # 在回调函数中获取请求的查询参数
        print('%s -下载成功' % response.effective_url)
        # 保存到static/downloads
        print(response.body)
        from app import BASE_DIR
        dir = os.path.join(BASE_DIR, 'static\downloads')
        with open(os.path.join(dir, filename), 'wb') as f:
            f.write(response.body)
        self.write('<br>下载完成,并保存成功！')
        self.finish()

    @asynchronous
    @coroutine
    def get(self, *args, **kwargs):
        # 获取查询参数中的url（下载资源的网址）
        url = self.get_query_argument('url')
        # 发起异步请求, 如果使用协程，等于是同步了
        client = AsyncHTTPClient()
        # validate_cert 是否验证SSL证书安全连接
        response = yield client.fetch(url, validate_cert=False)
        print(response.code)
        self.write('下载中...')
        self.save(response)
