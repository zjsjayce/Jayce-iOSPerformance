#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import collections
import datetime
import os
import shutil

from Utils import logger
from report import combine_single_csv, constants

LOGGING = logger.get_logger(__name__)
def pre_before(case):
    return '<pre id="' + case + '"  style="display:none">'


def pre_after():
    return '</pre>'


def function_before():
    return "<script>" + '\n' + "$(function () {$('#"


def generate_function_case(case):
    function_case = function_before() + 'container' + "_" + case + "').highcharts({title: {text: '" + constants.case_map.get(
        case) + "'},data: {csv: document.getElementById('" + case + "').innerHTML},chart: {type: 'column'},plotOptions: {series: {marker: {enabled: false},dataLabels: {enabled: true,}}},series: []});});</script>"

    return function_case


def convertVersions(all_version):
    app_versions = []
    for version in all_version:
        app_name = constants.app_map.get(version.split("-")[0])
        version = version.split("-")[1]
        app_versions.append(app_name + version)
    return app_versions


def generate_pre_function_section(dataToDeal):
    toInsert_preSection = ''
    toInsert_functionSection = ''
    for case in dataToDeal.keys():
        dataForCase = collections.OrderedDict(dataToDeal[case])
        all_version = []
        for device in dataForCase.keys():
            all_version.extend(dataForCase[device].keys())
        all_version = set(all_version)
        toInsert_preSection_case = pre_before(case) + "版本," + ",".join(convertVersions(all_version)) + '\n'
        toInsert_preSection_case_app = collections.OrderedDict()
        for device in dataForCase.keys():
            for app_version in dataForCase[device].keys():
                if (device not in toInsert_preSection_case_app.keys()):
                    toInsert_preSection_case_app[device] = []
                toInsert_preSection_case_app[device].append(round(dataForCase[device][app_version]))

        for device in dataForCase.keys():
            toInsert_preSection_case += constants.device_map.get(device) + ','
            toInsert_preSection_case += ','.join(str(value) for value in toInsert_preSection_case_app[device])
            toInsert_preSection_case += '\n'

        toInsert_preSection += toInsert_preSection_case
        toInsert_preSection += pre_after()
        toInsert_functionSection_case = generate_function_case(case)
        toInsert_functionSection += toInsert_functionSection_case

    return toInsert_preSection, toInsert_functionSection


def div_before():
    div_before_str = '<div class="parent">'
    return div_before_str


def div_after():
    return '</div>'


def generate_insert_content(dataToDeal):
    toInsert_divSection = generate_div_function_section(dataToDeal)

    toInsert_preSection, toInsert_functionSection = generate_pre_function_section(dataToDeal)

    return toInsert_divSection, toInsert_preSection, toInsert_functionSection


def generate_div_function_section(dataToDeal):
    toInsert_divSection = div_before()
    for case in dataToDeal.keys():
        containerName = 'container' + "_" + case
        toInsert_divSection += '<div class="child" id="' + containerName + '" style="width: 600px; height: 400px; margin-top: 100 auto">' + '</div>'
    toInsert_divSection += div_after()
    return toInsert_divSection

def insert_html(toInsert_divSection, toInsert_preSection, toInsert_functionSection, html_whole_name):
    dst_html_name = os.path.join(constants.HTML_DIR, html_whole_name)
    shutil.copy(os.path.join(constants.HTML_DIR, 'template.html'), dst_html_name)
    with open(html_whole_name, 'r') as f:
        content = f.read()
        position = content.find('<body>')
        if position != -1:
            content = content[:position + len('<body>')] + toInsert_divSection + '\n'+ toInsert_preSection + '\n' + toInsert_functionSection + '\n' + content[position + len('<body>'):]
            with open(dst_html_name, 'w') as f2:
                f2.write(content)

def generate_html(csvPath, htmlPath):
    dataToDeal = combine_single_csv.generateResultToPlot(csvPath)
    toInsert_divSection, toInsert_preSection, toInsert_functionSection = generate_insert_content(dataToDeal)
    html_name = constants.HTML_NAME
    html_whole_name = os.path.join(htmlPath, html_name)
    if os.path.exists(html_whole_name):
        shutil.move(html_whole_name, os.path.join(htmlPath, html_name))
    insert_html(toInsert_divSection, toInsert_preSection, toInsert_functionSection, html_whole_name)
    LOGGING.info("Html generated: " + os.path.join(constants.HTML_DIR, html_whole_name))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--csvDir", help="the path you want to store csv results, optional")
    args = parser.parse_args()
    generate_html(args.csvDir)