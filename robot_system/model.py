from typing import Optional

class BaseAgent:
    def __init__(self, id, pos_info: tuple, electric_charge: int, error: Optional[list]):
        self.id = id
        self.pos_info = pos_info
        self.electric_charge = electric_charge
        self.error = error if error is not None else None

class WheeledAgent(BaseAgent):
    def report_status(self):
        if self.error is None:
            status = "状态正常"
        else:
            status = f"历史异常:{self.error}"
        print(f"[轮式搬运车] {self.id}: 当前坐标 {self.pos_info},电量 {self.electric_charge}%, {status}")

class QuadrupedAgent(BaseAgent):
    def report_status(self):
        if self.error is None:
            status = "状态正常"
        else:
            status = f"历史异常:{self.error}"
        print(f"[四足机器狗] {self.id}: 当前坐标 {self.pos_info},电量 {self.electric_charge}%, {status}")