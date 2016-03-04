#! python
# -*- coding: utf-8 -*-

import ConfigParser
import re

class package2system:
    """根据包前缀查询对应的系统名称"""
    def __init__(self):
        self._dict = {}
        config = ConfigParser.ConfigParser()
        config.read("package2system.cfg")
        for option in config.options("package2system"):
            self._dict[option] = config.get("package2system",option)

    def get_system(self,package):
        for package_prefix,system in self._dict.items():
            if package.upper().encode("utf-8").startswith(package_prefix.upper()):
                return system
        return None

