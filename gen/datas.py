# -*- coding: utf-8 -*-
import json

"""
DATA TYPE: 
    0 - menu list
    1 - play list
    2 - menu item
    3 - self
"""

def gen_default_config():
    ret = {}

    #ret["home"] = gen_home()
    # 相关列表
    #ret["list"] = gen_list()


    ret["lists"] = read__list("tab")
    ret["banners"] = read__list("banner")

    return ret

def read__list(file_name):
    home_content = []

    other = read__otherlist("other")

    file = "./data/" + file_name
    content = open(file)

    for line in content:
        data = line.replace("\n", "").split(",")
        object = {}
        object["tab_name"] = data[0]
        object["tab_type"] = data[1]
        object["tab_pattern"] = data[2]
        object["tab_row"] = data[3]
        object["content_num"] = data[4]
        object["tab_order"] = data[5]
        object["song_limit"] = data[6]
        object["channel_id"] = data[7]
        object["channel_otherlist"] = other
        object["banner_cover"] = "http://pic7.nipic.com/20100518/3409334_031036048098_2.jpg"
        home_content.append(object)

    return home_content


def read__otherlist(file_name):
    home_content = []

    file = "./data/" + file_name
    content = open(file)

    for line in content:
        data = line.replace("\n", "").split(",")
        object = {}
        object["list_name"] = data[0]
        object["list_order"] = data[1]
        object["list_id"] = data[2]
        object["list_cover"] = data[3]
        home_content.append(object)

    return home_content

"""
Home
"""

def gen_home():
    home = {}
    home["content"] = read_home_detail("home_content")

    return home


"""
Play List
"""

PLAY_LIST = "PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI"

def gen_list():
    all_list = {}

    list = PLAY_LIST.split(",")
    # dataType 0
    all_list["menuList"] = gen_menu_list("menu_list")
    # dataType 1
    all_list["playList"] = gen_play_list(list)
    # dataType 2
    all_list["menuItem"] = gen_menu_item()

    return all_list

def gen_play_list(LIST_ID):
    play_list = []

    for id in LIST_ID:
        object = {}
        object["id"] = id
        object["list"] = read_file(id)
        play_list.append(object)

    return play_list


"""
Menu List
"""

def gen_menu_list(file_name):
    menu_list = []

    file = "./data/" + file_name
    content = open(file)

    for line in content:
        data = line.replace("\n", "").split(",")
        ID = read_file_to_list(data[0] + "_id")
        NAME = read_file_to_list(data[0] + "_name")

        object = {}
        object["id"] = data[0]
        object["list"] = gen_content_detail(ID, NAME, data[1])
        menu_list.append(object)

    return menu_list

def gen_content_detail(ID, NAME, dataType):
    detail = []

    for index, id in enumerate(ID):
        object = {}
        object["id"] = ID[index]
        object["name"] = NAME[index]
        object["dataType"] = dataType
        detail.append(object)

    return detail


"""
Menu Item
"""

def gen_menu_item():
    MENU_ITEM_LIST = "banner_item"
    LIST = MENU_ITEM_LIST.split(",")
    menu_item_list = []

    for list_file in LIST:
        object = {}
        object["id"] = list_file.replace("_item", "")
        object["items"] = read_menu_item(list_file)
        menu_item_list.append(object)

    return menu_item_list

"""
Read File
"""

def read_file(file_name):
    file = "./data/" + file_name

    with open(file, 'rb') as data:
        return json.load(data)

def read_file_to_list(file_name):
    list = []
    file = "./data/" + file_name
    content = open(file)

    for line in content:
        list.append(line.replace("\n", ""))

    return list

def read_menu_item(file_name):
    list = []
    file = "./data/" + file_name
    content = open(file)

    for line in content:
        data = line.replace("\n", "").split(",")
        object = {}
        object["id"] = data[0]
        object["name"] = data[1]
        object["image"] = data[2]
        object["dataType"] = data[3]
        list.append(object)

    return list

def read_home_detail(file_name):
    home_content = []

    file = "./data/" + file_name
    content = open(file)

    for line in content:
        data = line.replace("\n", "").split(",")
        object = {}
        object["id"] = data[0]
        object["name"] = data[1]
        object["dataType"] = data[2]
        object["maxNum"] = data[3]
        object["itemNum"] = data[4]
        object["image"] = data[5]
        object["viewType"] = data[6]
        object["actionType"] = data[7]
        home_content.append(object)

    return home_content
