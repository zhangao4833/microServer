# -*- coding: utf-8 -*-

from unittest import TestCase
import requests


class TestTornadoRequest(TestCase):
    base_url = 'http://10.36.174.18:9000'

    def test_index_request_post(self):
        url = self.base_url + '/'
        resp = requests.delete(url=url, data={
            'name': 'jack',
            'city': '西安'
        })
        print(resp.text)

    def test_index_request_delete(self):
        url = self.base_url + '/'
        resp = requests.delete(url=url, data={
            'name': 'jack',
            'city': '西安'
        })
        print(resp.text)

    def test_index_request_put(self):
        url = self.base_url + '/'
        resp = requests.put(url=url, data={
            'name': 'jack',
            'city': '西安'
        })
        print(resp.text)

    def test_index_request_get(self):
        url = self.base_url + '/'
        resp = requests.get(url=url, params={
            'wd': 'jack',
            'title': ['西安', '上海']
        })

    def test_index_request_get_and_post(self):
        url = self.base_url + '/'
        resp = requests.post(url=url, data={
            'name': 'jack',
            'city': '西安'
        }, params={
            'wd': '西安'
        })


class TestCookie(TestCase):
    url = 'http://10.36.174.18:9000/cookie'

    def test_delete_cookie(self):
        res = requests.delete(self.url, params={'name': 'wd'})
        print(res.text)

    def test_search(self):
        resp = requests.get('http://10.36.174.18:9000/search?wd=python')
        print(resp.text)
        print(resp.cookies)
        for k, cookie in resp.cookies.items():
            print(k, cookie)


class TestOrderRequest(TestCase):
    url = 'http://10.36.174.18:9000/order/2/3/'

    def test_get(self):
        resp = requests.get(self.url)
        print(resp.text)

    def test_post(self):
        resp = requests.post(self.url)
        print(resp.text)


class TestUserRequest(TestCase):
    url = 'http://10.36.174.18:9000/user'

    def test_get(self):
        resp = requests.get(url=self.url, json={
            'name': 'jack',
            'pwd': '123'
        })
        print(resp.json())

    def test_user_register(self):
        resp = requests.post(url=self.url, json={
            'name': 'tom',
            'pwd': '123',
            'phone': '123123123',
            'city': '西安'
        })
        print(resp.json())
    def test_user_update_info(self):
        resp = requests.put(url=self.url, json={
            'user_id':1,
            'phone':'110110110'
        })
        print(resp.json())
    def test_user_update_pwd(self):
        resp = requests.put(url=self.url, json={
            'user_id':1,
            'pwd':'0000000'
        })
        print(resp.json())
    def test_user_delete(self):
        resp = requests.delete(url=self.url, json={
            'user_id':1
        })
        print(resp.json())
