#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import os.path
from data_util.yaml_util import read_yaml

def yaml_list_get(execute_path = './settings.yaml'):
  path = read_yaml(execute_path)
  execute_path1 = path['execute_path']
  list1 = []
  for parent,dirnames, filenames in os.walk(execute_path1):
    for filename in filenames:
      if filename.endswith('.yaml'):
        list1.append(filename)
  return list1
