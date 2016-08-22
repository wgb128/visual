#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-8-22 下午3:42
# @Author  : youzeshun
# 参考资料  :
# 说明     :
import yaml


# 交换机ip和端口的映射 ， 该参数不允许类修改，只允许访问
def get_switch_map():
    object_file = file('static/idc/cache/ip_to_interface.yaml')
    dict_switch_map = yaml.load(object_file)
    return dict_switch_map.copy()


def get_interface(switch_ip, line):
    '''
    :param switch_ip: 交换机ip
    :param line: 需要查询的交换机接口对应的线路
    :return: 交换机接口的名称
    '''
    object_file = file('static/idc/cache/ip_to_interface.yaml')
    dict_switch_map = yaml.load(object_file)
    if not switch_ip in dict_switch_map:
        return ''
    if not line in dict_switch_map[switch_ip]:
        return ''
    return dict_switch_map[switch_ip][line]


DICT_SWITCH_MAP = get_switch_map()

if __name__ == '__main__':
    pass