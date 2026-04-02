from models import Scheduler


if __name__ == "__main__":
    engine = Scheduler()
    engine.load_nodes("nodes.json")
    engine.load_tasks("tasks.txt")
    
    print(f"成功加载了 {len(engine.nodes)} 个节点！")
    print(f"成功加载了 {len(engine.tasks)} 个任务！")
    
    engine.sort_tasks()
    print("\n--- 🚥 调度队列已按优先级排序 ---")
    for t in engine.tasks:
        print(t)

    
    print("\n--- 现在开始按照优先级为任务分配计算节点 --- ")
    engine.dispatch_tasks()
