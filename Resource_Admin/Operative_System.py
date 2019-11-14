from Resource_Admin.CU_distributed import CU_distributed
from Resource_Admin.RAM_distributed import RAM_distributed


class Operative_System:
    def __init__(self,RAM,CU):
        self.RAM= RAM
        self.CU=CU
        self.RAM_distributed = RAM_distributed()
        self.CU_distributed=CU_distributed()


