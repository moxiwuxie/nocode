#!/usr/bin/python
# -*- coding: UTF-8 -*-
import yaml
with open('../casedata/login1.yaml') as f:
  a = yaml.load(stream=f, Loader=yaml.FullLoader)
  b = a[1]
  print(a)
  print(b)
  print(len(b))
  # print(a['1'])
