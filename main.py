#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pytest
import os


if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./temp -o ./report --clean')#固定报告
