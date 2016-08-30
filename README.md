# 通用可视化接口演示
使用接口：
打开页面一输入下面的链接，将data传入
http://192.168.165.200:82/custom/input/?live=1&chart=bar&key=adsl&data={"10.10.10.121": {"eth0": {"purpose": "网站-运营","down_total": 200,"up_total": 35,"down_used": 100,"up_used": 10}}}


效果：打开页面二
http://192.168.165.200:82/custom/output/?chart=bar&key=adsl&timeout=5


当更改传入data后，页面二的图形会变化(无需手动刷新)（更改后的url如：）
http://192.168.165.200:82/custom/input/?live=1&chart=bar&key=adsl&data={"10.10.10.121": {"eth0": {"purpose": "行政","down_total": 200,"up_total": 35,"down_used": 10,"up_used": 20}}}


## 参数/格式说明：
数据输入链接：　http://ip:port/custom/input/
	参数:
	live 　　是否在当前页面直接显示效果　可选　默认0
	chart : 选用哪种图形显示数据，当live为１时才有效
	key 　　　访问数据的key 必选
	data 　　数据
	
数据输出链接：　http://ip:port/custom/out/
	参数：
	key : 图像化对应key的数据
	chart : 选用哪种图形显示数据，目前是代码为demo,仅有默认的bar
	timeout: 更新数据的频率
# 传入的数据格式data说明
## 必须的参数：
{
    "10.32.64.134": {
        "eth0": {
            "purpose": "用于代码部署", 
            "down_total": 200, 
            "up_total": 35, 
            "down_used": 100, 
            "up_used": 10
        }
    }
}

## 完整版本格式说明
{
    "10.32.64.134": {
        "eth0": {
            "purpose": "用于代码部署", //用途，如：ＱＱ，部门
            "equrrdment": "虚拟机", //设备，如光纤,adsl
            "down_total": 200, //下载总带宽，单位m/s
            "up_total": 35, //上行总带宽,单位m/s
            "down_used": 100, //上行已用,单位m/s
            "up_used": 10, //下行已用，单位m/s
            "zabbix_graph_id": "yzs-1"　//该ｉｐ的网口eth0对应的zabbix_graph_id
        }
    }
}


# 更为完整的demo
http://192.168.165.200:82/custom/input/?live=1&chart=bar&key=adsl&data={ "10.10.10.121": { "eth0": { "purpose": "网站-运营", "equrrdment": "ADSL", "down_total": 200, "up_total": 35, "down_used": 100, "up_used": 10, "zabbix_graph_id": "yzs-1" } }, "10.10.10.2": { "eth1": { "purpose": "电信", "equrrdment": "光纤出口", "down_total": 100, "up_total": 100, "down_used": 100, "up_used": 10, "zabbix_graph_id": "yzs-1" } }, "10.10.10.122.": { "eth0": { "purpose": "QQ", "equrrdment": "ADSL", "down_total": 200, "up_total": 35, "down_used": 100, "up_used": 10, "zabbix_graph_id": "yzs-1" } }, "10.10.10.1": { "eth3": { "purpose": "睿江", "equrrdment": "光纤出口", "down_total": 100, "up_total": 100, "down_used": 100, "up_used": 10, "zabbix_graph_id": "yzs-1" } }, "10.10.10.126": { "eth0": { "purpose": "无线1", "equrrdment": "ADSL", "down_total": 200, "up_total": 35, "down_used": 100, "up_used": 10, "zabbix_graph_id": "yzs-1" } }, "10.10.10.123": { "eth0": { "purpose": "运营-公用机", "equrrdment": "ADSL", "down_total": 200, "up_total": 35, "down_used": 100, "up_used": 10, "zabbix_graph_id": "yzs-1" } }, "10.10.10.125": { "eth0": { "purpose": "无线2", "equrrdment": "ADSL", "down_total": 200, "up_total": 35, "down_used": 100, "up_used": 10, "zabbix_graph_id": "yzs-1" } }, "10.10.10.127": { "eth0": { "purpose": "技术", "equrrdment": "ADSL", "down_total": 200, "up_total": 35, "down_used": 100, "up_used": 10, "zabbix_graph_id": "yzs-1" } }, "10.10.10.120": { "eth0": { "purpose": "运营-行政", "equrrdment": "ADSL", "down_total": 200, "up_total": 35, "down_used": 100, "up_used": 10 } }, "10.28.0.1": { "eth0": { "purpose": "成都电信2", "equrrdment": "光纤出口", "down_total": 20, "up_total": 20, "down_used": 10, "up_used": 10, "zabbix_graph_id": "yzs-1" }, "eth3": { "purpose": "成都AD", "equrrdment": "光纤出口", "down_total": 100, "up_total": 20, "down_used": 100, "up_used": 10, "zabbix_graph_id": "yzs-1" } }, "10.10.10.124": { "eth0": { "purpose": "策划", "equrrdment": "ADSL", "down_total": 200, "up_total": 35, "down_used": 100, "up_used": 10, "zabbix_graph_id": "yzs-1" } } }
