#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging
import pytest
import json
from data_util.yaml_util import read_yaml, write_yaml
from testcommon.session_establish import session_establish
import requests
import time

# logger = logging.Logger
@pytest.fixture(scope='session',autouse=True)
def login():
  a = read_yaml(path='login.yaml')
  session_establish(a)
  # print('test')
  # 需要进行正则匹配
  # if 'token' in rep.text:
  #   token = json.loads(rep.text)['data']['token']
  #   write_yaml(data=dict.fromkeys(['authorization'],token),path='./token.yaml')
  #   print('登陆成功')
  # else:
  #   print('登录失败')
  #   pass
  # yield
  # data = {
  #   "msg_type": "interactive",
  #   "card": {
  #     "config": {
  #       "wide_screen_mode": True,
  #       "enable_forward": True
  #     },
  #     "elements": [{
  #       "tag": "div",
  #       "text": {
  #         "content": "allure报告地址：",
  #         "tag": "lark_md"
  #       }
  #     }, ],
  #     "header": {
  #       "title": {
  #         "content": "自动化测试报告-allure：" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
  #         "tag": "plain_text"
  #       }
  #     }
  #   }
  # }
  # response = requests.post("https://open.feishu.cn/open-apis/bot/v2/hook/9a03d9e4-089e-4dc1-9a1d-7e85fcba7e46",
  #                          data=json.dumps(data))
  # print("\nsession会话结束！")


