# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implement pre-processing
"""

from nikl.option import setting_parse
from nikl.loader.load_file import read_text_file
from nikl.target.infos import get_info

if __name__ == '__main__':
    """ Setting parameters input & description """
    filenames, info, content, newline = setting_parse()

    for _ in filenames:
        print(_)
        raw_text = read_text_file(_)
        #print(len(raw_text))
        get_info(_, raw_text, info)
        #print(raw_text)
