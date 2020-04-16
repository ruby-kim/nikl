"""
Implement pre-processing and save files: <teiHeader></teiHeader> part
"""
from bs4 import BeautifulSoup

from nikl.preprocessor import *

# def save_info(name, infos):
#     """ Save .text info"""
#     file = open("../data/info/" + name + "_info.txt", 'a', encoding="utf-8")
#     #for info in range(len(infos)):
#
#     #file.write(line) for line in range(len(text))


def make_fileDesc(text):
    """ ============================
        Parsing fileDesc information
        ============================
        Args:
            :param: text(str): raw_file
    """
    soup = BeautifulSoup(text, "html.parser")
    element = {
        "titleStmt": ["title",
                      "author",
                      "sponsor",
                      "respStmt"],
        "extent": None,
        "publicationStmt": ["distributor",
                            "idno",
                            "availability"],
        "sourceDesc": None
    }

    # setting list options: element's values
    result = list()
    for key, value in element.items():
        if value is not None:
            for tag in value:
                result.append(tag)
        else:
            result.append(key)

    # find result's values
    idx = 0
    for _ in result:
        if _ is not "respStmt":
            tag = soup.select(_)[0].text
            _ += ": " + tag
        else:
            resp = soup.select("resp")[0].text
            tname = soup.select("tname")[0].text
            _ = "    " + _ + "\n\tresp: " + resp + "\n\ttname: " + tname
        result[idx] = _
        idx += 1

    # insert section: [fileDesc]
    result.insert(0, "[fileDesc]")
    return result


def make_encodingDesc(text):
    """ ================================
        Parsing encodingDesc information
        ================================
        Args:
            :param: text(str): raw_file
    """
    soup = BeautifulSoup(text, "html.parser")
    result = [
        "projectDesc",
        "samplingDecl",
        "editorialDecl"
    ]

    # find result's values
    idx = 0
    for _ in result:
        tag = soup.select(_)[0].text
        _ += ": " + tag
        result[idx] = _
        idx += 1

    # insert section: [encodingDesc]
    result.insert(0, "\n[encodingDesc]")

    return result


def make_profileDesc(text):
    """ ============================
        Parsing profileDesc information
        ============================
        Args:
            :param: text(str): raw_file
    """
    soup = BeautifulSoup(text, "html.parser")
    element = {
        "creation": ["date"],
        "langUsage": ["language"],
        "particDesc": ["person"],
        "settingDesc": None,
        "textClass": ["catRef"]
    }

    # setting list options: element's values
    result = list()
    for key, value in element.items():
        if value is not None:
            for tag in value:
                result.append(tag)
        else:
            result.append(key)
    print(result)
    # find result's values
    idx = 0
    for _ in result:
        tag = soup.select(_)[0].text
        if _ is "date":
            _ = "creation:\n    " + _
        elif _ is "language":
            _ = "language:\n    " + _
        elif _ is "person":

        elif _ is "settingDesc":
            _ += ": " + tag
        elif _ is "catRef":
            _ += ": "
    #     if _ is not "respStmt":
    #         tag = soup.select(_)[0].text
    #         _ += ": " + tag
    #     else:
    #         resp = soup.select("resp")[0].text
    #         tname = soup.select("tname")[0].text
    #         _ = "    " + _ + "\n\tresp: " + resp + "\n\ttname: " + tname
    #     result[idx] = _
    #     idx += 1

    # insert section: [profileDesc]
    result.insert(0, "\n[profileDesc]")
    #return result
#
#
# def make_revisionDesc(key, value):


def get_info(text, infos):
    """ =======================
        Parsing the information
        =======================
        Args:
            :param: text(str): raw_file
            :param: info(boolean, default: false)
    """
    if not infos:
        return

    # get specific values & write
    fileDesc = make_fileDesc(text)
    encodingDesc = make_encodingDesc(text)
    #profileDesc = make_profileDesc(text)
    make_profileDesc(text)
    #revisionDesc = make_revisionDesc(text)
    #print(fileDesc)
    #print(encodingDesc)
    #print(profileDesc)
    #print(revisionDesc)
