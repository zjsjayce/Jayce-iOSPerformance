# -*- encoding=utf8 -*-
__author__ = "jayce"

from airtest.core.api import *

sleep(4.0)
stop_app('com.tencent.info')
sleep(1.0)
auto_setup(__file__)
