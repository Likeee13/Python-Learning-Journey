def write_log(msg:str, file_path = "dispatch_task.log"):
    print(msg)
    with open(file_path, "a", encoding = "utf-8") as f:
        f.write(msg + "\n")
