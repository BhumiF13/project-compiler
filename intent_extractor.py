import re

def extract_intent(command):
    
    intent = {
        "action": None,
        "type": None,
        "name": None,
        "value": None
    }

    if "loop from" in command or "create loop" in command:
        intent["action"] = "loop_start"

        match = re.search(r"from\s+(\d+)\s+to\s+(\d+).*variable\s+(\w+)", command)
        if match:
            intent["start"] = match.group(1)
            intent["end"] = match.group(2)
            intent["name"] = match.group(3)

    elif "end loop" in command:
        intent["action"] = "loop_end"

    elif "create" in command and "variable" in command:
        intent["action"] = "create"
        intent["type"] = "variable"

        match = re.search(r"variable\s+(\w+)\s+(.+)", command)
        if match:
            intent["name"] = match.group(1)
            intent["value"] = match.group(2)

    elif "set" in command:
        intent["action"] = "set"
        intent["type"] = "variable"

        match = re.search(r"set\s+(\w+)\s+to\s+(.+)", command)
        if match:
            intent["name"] = match.group(1)
            intent["value"] = match.group(2)

    if "print text" in command:
        intent["action"] = "print"
        intent["type"] = "text"

        match = re.search(r"print text (.+)", command)
        if match:
            intent["value"] = match.group(1)

    elif "print" in command:
        intent["action"] = "print"

        match = re.search(r"variable\s+(\w+)", command)
        if match:
            intent["type"] = "variable"
            intent["name"] = match.group(1)
        else:
            match = re.search(r"print\s+(\w+)", command)
            if match:
                intent["type"] = "variable"
                intent["name"] = match.group(1)

    return intent