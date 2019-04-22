#!/usr/bin/python
# coding= utf-8
"""
视频起播时间
"""
import os
import sys
import time

import casePackage.utils.constants as constants
import Utils.exception as exception

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from casePackage.abstract_case import biz_case as biz_case
import casePackage.utils.apptool as apptool

app = apptool.NETEASE
scene = 'shipin_shouzhen'

class Case(biz_case.Case):

    def __init__(self, app, scene, buildId, branch, app_version, batch_num, device, ran, suite):
        biz_case.Case.__init__(self, app, scene, buildId, branch, app_version, batch_num, device, ran, suite)

    def enter_shipin(self):
        count = 0
        while True:
            element = self.m.netease_find_shipin_tab()
            if element:
                element.click()
                return True
            self.apptools.swipe(0.8, 0.12, 0.2, 0.12)
            count += 1
            if count > 20:
                return False

    def case(self):
        # self.apptools.pmClearApp()
        self.before_case_exec()
        self.apptools.forceStopApp()
        self.apptools.start()
        time.sleep(7)
        isEnter = self.enter_shipin()
        if not isEnter:
            raise exception.CaseExecutingException(self.log_tag + "Didn't find 视频 tab in netease_shipin_shouzhen",
                                                   RuntimeError(constants.FIND_FAIL_EXCE_MSG))
        self.apptools.swipe(0.5, 0.3, 0.5, 0.6)
        time.sleep(3)

        for i in range(0, 10):
            video_item = self.m.netease_find_video_start()
            if video_item:
                break
        if not video_item:
            raise exception.CaseExecutingException(self.log_tag + "Didn't find video_start in netease_shipin_shouzhen",
                                                   RuntimeError(constants.FIND_FAIL_EXCE_MSG))
        self.startRecord(7)
        time.sleep(1)
        self.apptools.click_at(video_item.x, video_item.y)
        time.sleep(7)
        self.listener.stop()
        tmp_save = self.saveRecord()
        # self.gt.image_path = tmp_save
        # self.gt.start()
        # self.gt.join()
        # self.after_case_exec()


if __name__ == "__main__":
    case = Case(app, scene)
    case.case()