#!/usr/bin/python
# coding= utf-8
"""
腾讯新闻视频起播时间
"""
import os
import sys
import time

import casePackage.utils.constants as constants
import Utils.exception as exception

from casePackage.abstract_case import biz_case as biz_case
import casePackage.utils.apptool as apptool

app = apptool.TENCENT
scene = 'shipin_shouzhen'

class Case(biz_case.Case):

    def __init__(self, app, scene, buildId, branch, app_version, batch_num, device, ran, suite):
        biz_case.Case.__init__(self, app, scene, buildId, branch, app_version, batch_num, device, ran, suite)

    def enter_shipin(self):
        count = 0
        while True:
            element = self.m.tencent_find_shipin_tab()
            if element:
                element.click()
                return True
            self.apptools.swipe(0.8, 0.12, 0.2, 0.12)
            count += 1
            if count > 20:
                return False

    def case(self):
        # self.apptools.pmClearApp()
        self.apptools.forceStopApp()
        self.apptools.start()
        time.sleep(15)
        isEnter = self.enter_shipin()
        if not isEnter:
            raise exception.CaseExecutingException(self.log_tag + "Didn't find 视频 tab in toutiao_shipin_shouzhen",
                                                   RuntimeError(constants.FIND_FAIL_EXCE_MSG))
        time.sleep(1)
        self.apptools.swipe(0.5, 0.25, 0.5, 0.85)
        time.sleep(3)

        for i in range(0, 10):
            video_item = self.m.tencent_find_video_start()
            if video_item:
                break
        if not video_item:
            raise exception.CaseExecutingException(self.log_tag + "Didn't find video_start in toutiao_shipin_luodi",
                                                   RuntimeError(constants.FIND_FAIL_EXCE_MSG))
        # record duration must less than total sleep duration
        self.startRecord(6)
        time.sleep(1)
        self.apptools.click_at(video_item.x, video_item.y)
        time.sleep(6)
        tmp_save = self.saveRecord()
        time.sleep(0.5)
        # self.gt.image_path = tmp_save
        # self.gt.start()
        # self.gt.join()
        # self.after_case_exec()


if __name__ == "__main__":
    case = Case(app, scene)
    case.case()