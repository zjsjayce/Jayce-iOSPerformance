#!/usr/bin/env python
# -*- coding: utf-8 -*-

case_map = {
    'hotstart-white': '热启动白屏',
    'hotstart-total': '热启动完整',
    'list-refresh': '头条列表刷新',
    'tuji': '图集详情页加载',
    'shipin-luodi': '视频详情页加载',
    'shipin-shouzhen': '视频起播',
    'tuwen': '图文详情页加载',
    'coldstart-white': '冷启动白屏',
    'coldstart-total': '冷启动完整',
    'coldstart-newuser-white': '新用户白屏',
    'coldstart-newuser-total': '新用户完整',
}

device_map = {
    'XPU4C17112010268': '华为nova',
    '573a521e': '小米6'
}

# 需要和jenkins job name相同
# HTML_DIR = r'E:\jenkinsWorkspace\workspace\Android performance mock test'
HTML_DIR = r'D:\Users\zhaoyuting\auto\report\html'
HTML_NAME = "performance_test_results.html"
CSV_DIR = r'D:\Users\zhaoyuting\auto\report\csv'


app_map = {
    'netease': '网易新闻',
    'toutiao': '今日头条',
    'tencent': '腾讯新闻'
}