class ResourceExhaustedError(Exception):
    def __init__(self, task_id, reasoning = "资源算力不够"):
        error_msg = f"任务{task_id}分配计算节点失败，{reasoning}"
        super().__init__(error_msg)