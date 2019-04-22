# -*- encoding=utf8 -*-
__author__ = "jayce"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir="/Users/jayce/PerformanceOutput/NetEase/Launch", devices=[
            "ios:///http://127.0.0.1:8100",
    ])
sleep(1.0)
start_app('com.netease.news')
sleep(2.0)
stop_app('com.netease.news')




# script content


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath="/Users/jayce/PerformanceOutput/NetEase/Launch")