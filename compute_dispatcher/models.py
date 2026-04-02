import json
from exceptions import ResourceExhaustedError
from utils import write_log

class Scheduler:
    def __init__(self):
        self.nodes = []
        self.tasks = []
        self.waiting_tasks = []

    def load_nodes(self, file_path: str):
        with open(file_path, 'r', encoding='utf-8') as f:
            data_list = json.load(f)

        for data in data_list:
            node_id = data.get("node_id")
            cpu_cores = data.get("cpu_cores")
            gpu_vram = data.get("gpu_vram")
            ram = data.get("ram")
            self.nodes.append(ComputeNode(node_id, cpu_cores, gpu_vram, ram))


    def load_tasks(self, file_path: str):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        lines = lines[1:]
        for line in lines:
            line = line.strip()
            parts = line.split(",")
            task_id = parts[0]
            task_type = parts[1]
            req_cpu = int(parts[2])
            req_gpu = int(parts[3])
            req_ram = int(parts[4])
            priority = int(parts[5])
            self.tasks.append(AITask(task_id, task_type, req_cpu, req_gpu, req_ram, priority))

    def sort_tasks(self):
        self.tasks.sort()

    def dispatch_tasks(self):
        count = 0
        for task in self.tasks:
            try:
                count += 1
                flag = False
                write_log(f"\n--- 现在为第{count}个任务分配计算单元 ---")
                write_log(f"{task.task_id} 需求 -> CPU:{task.req_cpu} 核 | GPU:{task.req_gpu} GB | 内存：{task.req_ram} GB")
                for node in self.nodes:
                    if task.req_cpu <= node.cpu_cores and task.req_gpu <= node.gpu_vram and task.req_ram <= node.ram:
                        flag = True
                        write_log(f"成功为该任务分配计算单元{node.node_id}")
                        write_log(f"下面是该计算单元的可用资源量")
                        write_log(f"{node.node_id} 可用资源 -> CPU:{node.cpu_cores} 核 | GPU:{node.gpu_vram} GB | 内存：{node.ram} GB")
                        node.cpu_cores -= task.req_cpu
                        node.gpu_vram -= task.req_gpu
                        node.ram -= task.req_ram
                        break
                if flag == False:
                    write_log(f"暂未为{task.task_id}任务找到合适的计算单元,先将该任务加载到等待队列中")
                    self.waiting_tasks.append(task)
                    raise ResourceExhaustedError(task.task_id)
            except ResourceExhaustedError as e:
                write_log(f"发生异常:{e}")




class ComputeNode:
    def __init__(self, node_id: str, cpu_cores: int, gpu_vram: int, ram: int):
        self.node_id = node_id
        self.cpu_cores = cpu_cores
        self.gpu_vram = gpu_vram
        self.ram = ram

    def __str__(self):
        return f"[节点 {self.node_id}] 剩余资源 -> CPU:{self.cpu_cores} 核 | GPU:{self.gpu_vram} GB | 内存：{self.ram} GB"
    
    def __add__(self, other):
        new_name = f"{self.node_id}_{other.node_id}_Cluster"
        new_cpu_cores = self.cpu_cores + other.cpu_cores
        new_gpu_vram = self.gpu_vram + other.gpu_vram
        new_ram = self.ram + other.ram

        new_node = ComputeNode(new_name, new_cpu_cores, new_gpu_vram, new_ram)

        return new_node
    


class AITask:
    def __init__(self, task_id: str, task_type: str, req_cpu: int, req_gpu: int, req_ram: int, priority: int):
        self.task_id = task_id
        self.task_type = task_type
        self.req_cpu = req_cpu
        self.req_gpu = req_gpu
        self.req_ram = req_ram
        self.priority = priority

    def __str__(self):
        if self.priority == 1:
            tag = "紧急任务"
        elif self.priority == 2 or self.priority == 3:
            tag = "重要任务"
        else:
            tag = "一般任务"
        return f"[{tag} {self.task_id}] 类型：{self.task_type} | 优先级:{self.priority} | 需求：{self.req_cpu}C/{self.req_gpu}G/{self.req_ram}G"
    
    # 此方法用于比较任务的优先级
    def __lt__(self, other):
        if self.priority != other.priority:
            return self.priority < other.priority
        else:
            return self.req_ram < other.req_ram



