# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implement pre-processing
"""

from nikl.option import setting_parse
from nikl.loader.load_file import read_text_file
from nikl.target.infos import get_info
from nikl.target.contents import get_content


def chk_newline(filename, content, newline):
    """ Check newline value
        본문 내용을 저장할 시
        각 문단별 끝에 개행문자가 들어가는지에 대한 여부 확인
    """
    if newline is True:
        get_content(filename, content, True)
    else:
        get_content(filename, content, False)


if __name__ == '__main__':
    """ Setting parameters input & description """
    filenames, info, content, newline = setting_parse()

    for filename in filenames:
        print("=======================================\n"
              "    *   Target Data: ", filename, "\n"\
              "=======================================\n"\
              "         - info: ", info, "\n"\
              "         - content: ", content, "\n"\
              "         - newline: ", newline, "\n"\
              "=======================================")

        filename = filename.replace(".txt", "")
        raw_text = read_text_file(filename)
        if info is True:
            print("[Start] Pre-process: info data...")
            get_info(filename, raw_text)
            print("[Save] info data. Check data/%s_info.txt\n" % filename)
        if content is True:
            print("[Start] Pre-process: content data...")
            chk_newline(filename, raw_text, newline)
            print("[Save] content data. Check data/%s_content.txt\n\n" % filename)
