#! python
# -*- coding: utf-8 -*-

def init_package_system_dict():
    """初始化包前缀与系统名对应关系的字典"""
    package_system_dict = {}
    package_system_dict["GJS"] = "贵金属"
    package_system_dict["cardATMC"] = "自助终端"
    package_system_dict["gbatch"] = "智能社区"
    package_system_dict["card_POSPconsole"] = "智能社区"
    package_system_dict["cardFKJ"] = "发卡机"
    package_system_dict["cardVTM"] = "智能银行"
    package_system_dict["suncard"] = "贷记卡系统"
    package_system_dict["cardMGR"] = "贷记卡管理系统"
    package_system_dict["windows"] = "短信银行"
    package_system_dict["WYZS"] = "网银助手"
    package_system_dict["SmartESB"] = "ESB"
    package_system_dict["DRCB_PB"] = "柜面系统"
    package_system_dict["GMXT"] = "柜面系统"
    package_system_dict["CardICP"] = "IC卡核心"
    package_system_dict["CardICBP"] = "IC卡批处理"
    package_system_dict["ICDP"] = "IC卡数据准备系统"
    package_system_dict["AMC"] = "IC卡金融管理平台"
    package_system_dict["tsp"] = "IC卡受理方"
    package_system_dict["cardfrs"] = "卡前置"
    package_system_dict["AS400"] = "综合业务系统"
    return package_system_dict

class package2system:
    """根据包前缀查询对应的系统名称"""
    def __init__(self):
        self._dict = init_package_system_dict()

    def get_system(self,package):
        for package_prefix,system in self._dict.items():
            if package.startswith(package_prefix):
                return system
        return None

