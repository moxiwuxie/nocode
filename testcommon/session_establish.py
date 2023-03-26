#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json
import re
from data_util.yaml_util import read_yaml
from testcommon import logings
logg = logings.logger

def session_establish(datas):
  session = requests.session()
  rep_text_list = []
  for filedata in range(len(datas)):
    method = str(datas[filedata]['method'].lower())
    url = datas[filedata]["url"]
    datas[filedata]['headers']['authorization'] = read_yaml('./token.yaml')['authorization']
    headers = datas[filedata]['headers']
    data = datas[filedata]["data"]
    data_regular_expression = datas[filedata]['data_regular_expression']
    status_code_expected_outcome = datas[filedata]['status_code_expected_outcome']
    body_expected_oucome = datas[filedata]['body_expected_oucome']
    is_assert = datas[filedata]['is_assert']

    if method == 'get':
      rep = session.request(method=method, url=url, headers=headers, params=json.dumps(data))
      # logings.logger.info(rep.text)
    elif method == 'post':
      rep = session.request(method=method, url=url, data=json.dumps(data), headers=headers)
      # logings.logger.info(rep.text)
    elif method == 'delete':
      rep = session.request(method=method, url=url)
      # logings.logger.info(rep.text)
    else:
      rep = session.request(method=method, url=url)
      # logings.logger.info(rep.text)
    logg.info('request.url=  ' + str(rep.request.url))
    logg.info('request.headers=  ' + str(rep.request.headers))
    logg.info('request.body=  ' + str(rep.request.body))
    logg.info('rep.status_code=  ' + str(rep.status_code))
    logg.info('rep.text=  ' + rep.text)
    if rep.status_code == status_code_expected_outcome:
      if is_assert:
        actual_result_body = re.findall(data_regular_expression, rep.text)
        if body_expected_oucome == str(actual_result_body):
          logg.info("assert check success !!!")
        else:
          logg.error('assert check failed\n' + 'rep.text' + rep.text)
    else:
      logg.error('rep.status_code' + str(rep.status_code))
    rep_text_list.append(rep.text)
  return rep_text_list


