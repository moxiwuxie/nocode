#!/usr/bin/python
# -*- coding: UTF-8 -*-
from data_util.yaml_list_get import yaml_list_get
from data_util.yaml_util import read_yaml
from testcommon.session_establish import session_establish
import pytest


# @pytest.mark.smoke
def test_yaml_list_post():
  path = read_yaml(path='./settings.yaml')
  execute_path1 = path['execute_path']
  yaml_list = yaml_list_get()
  for i in yaml_list:
    session_establish(read_yaml(execute_path1 + i))
@pytest.mark.smoke
def test_01():
  pass


