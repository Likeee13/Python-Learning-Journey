from typing import Optional

def parser_log(log: str) -> Optional[dict]:
    """
    This is a function to parser a piece of log.
    It extracts id, type, pos, batt, and logs (if has) from a piece of log and returns as a dict.

    Example_1:
    Input: "ID:Q-01 | TYPE:Quadruped | POS:15.2,19.1 | BATT:42 | ERROR:Joint_Overheat"
    Output: {
            "ID": "Q-01",
            "TYPE": "Quadruped",
            "POS": (15.2, 19.1),
            "BATT: 42,
            "ERROR": ["Joint_Overheat"]
            }

    Example_2:
    Input: "ID:W-01 | TYPE:Wheeled | POS:10.5,20.0 | BATT:85"
    Output: {
            "ID": "W-01",
            "TYPE": "Wheeled",
            "POS": (10.5, 20.0),
            "BATT: 85
            }

    Example_3:
    Input: "CORRUPTED_DATA_MESSAGE_%%%&&&"
    Output: None

    """
    parsed_data = {}

    parts = log.split("|")
    for part in parts:
        item = part.split(":", 1)
        if len(item) != 2:
            continue

        key = item[0].strip()
        value = item[1].strip()

        if key in ["ID", "TYPE"]:
            parsed_data[key] = value
        elif key == "POS":
            nums = value.split(",")
            parsed_data["POS"] = tuple([float(num.strip()) for num in nums])
        elif key == "BATT":
            if value.isdigit():
                parsed_data["BATT"] = int(value)
            else:
                print(f"电量数值出现异常 [{value}]")
        elif key == "ERROR":
            parsed_data["ERROR"] = [value]
        else:
            print(f"log中出现了未定义的字段，请检查")

    if len(parsed_data) == 0:
        return None
    else:
        return parsed_data

    