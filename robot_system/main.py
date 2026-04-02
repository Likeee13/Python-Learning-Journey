from model import BaseAgent, WheeledAgent, QuadrupedAgent
from typing import Optional
from parser import parser_log

if __name__ == "__main__":

    raw_log_stream = [
    "ID:W-01 | TYPE:Wheeled | POS:10.5,20.0 | BATT:85",
    "ID:Q-01 | TYPE:Quadruped | POS:15.2,19.1 | BATT:42 | ERROR:Joint_Overheat",
    "ID:W-02 | TYPE:Wheeled | POS:0,0 | BATT:12 | ERROR:Low_Power",
    "CORRUPTED_DATA_MESSAGE_%%%&&&",
    "ID:Q-02 | TYPE:Quadruped | POS:100.1,200.5 | BATT:98"
    ]

    fleet_registry = {}

    invalid_count = 0
    
    broken_agent_id = []

    for raw_log in raw_log_stream:
        result = parser_log(raw_log)
        if result is None:
            invalid_count += 1
        else:
            id = result["ID"]
            type = result["TYPE"]
            pos = result["POS"]
            batt = result["BATT"]
            error = result.get("ERROR", None)
            if type == "Wheeled":
                fleet_registry[id] = WheeledAgent(id, pos, batt, error)
            elif type == "Quadruped":
                fleet_registry[id] = QuadrupedAgent(id, pos, batt, error)
            else:
                print(f"出现了不合法的机器人类型，请检查")
 
            
    print(f"===== 异构集群初始化完毕 =====")
    print(f"成功解析 {len(fleet_registry)} 条有效日志，拦截 {invalid_count} 条损坏日志")   

    print(f"===== 当前集群状态报告 =====")
    for key, value in fleet_registry.items():
        value.report_status()
        if value.error is not None:
            broken_agent_id.append(key)


    print(f"===== ⚠️ 预警调度系统 =====")
    print(f"以下机器人需要立即回港检修：{broken_agent_id}")          

    print(f"===== 🔋 电量警报系统 =====")
    print(f"以下机器人的电量低于20%：{[agent.id for agent in fleet_registry.values() if agent.electric_charge < 20]}")