#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import yaml

#yaml读取
def read_yaml(path):
    with open(path,mode='r',encoding='utf-8') as f:
      return yaml.load(stream=f,Loader=yaml.FullLoader)
#写入
def write_yaml(data,path):
    with open(path,mode='w',encoding='utf-8') as f:
        yaml.dump(data,stream=f,allow_unicode=True)
#清空
def clear_yaml(path):
    with open(os.getcwd()+path,mode='w',encoding='utf-8') as f:
        f.truncate()
