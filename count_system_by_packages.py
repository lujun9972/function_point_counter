import package2system

class system_counter():
    '''统计投产系统数量'''
    def __init__(self):
        self._dict={}
        self._translater = package2system.package2system()

    def incf_by_systems(self,*systems):
        for system in systems:
            if system not in self._dict:
                self._dict[system] = 0
            self._dict[system]=+1

    def incf_by_packages(self,*packages):
        systems = [self._translater.get_system(package) for package in packages]
        self.incf_by_systems(*systems)

    def count(self,system):
        return self._dict.get(system,0)

    def get_systems(self):
        return self._dict.keys()
