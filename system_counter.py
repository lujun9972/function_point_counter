import package2system

class system_counter():
    '''统计投产系统数量'''
    def __init__(self):
        self._dict={}
        self._translater = package2system.package2system()

    def incf_by_system(self,system,incf=1):
        if system not in self._dict:
            self._dict[system] = 0
        self._dict[system]=+incf

    def incf_by_package(self,packages,incf=1):
        system = self._translater.get_system(package)
        self.incf_by_system(systems,incf)

    def count(self,system):
        return self._dict.get(system,0)

    def get_systems(self):
        return self._dict.keys()
