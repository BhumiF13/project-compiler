from validator import validate_intent

def generate_c_line(intent):
    if not validate_intent(intent):
        return None

    if intent["action"] == "create":
        return f"int {intent['name']} = {intent['value']};"

    elif intent["action"] == "loop_start":
        return f"for(int {intent['name']} = {intent['start']}; {intent['name']} <= {intent['end']}; {intent['name']}++) {{"

    elif intent["action"] == "loop_end":
        return "}"

    elif intent["action"] == "set":
        return f"{intent['name']} = {intent['value']};"

    elif intent["action"] == "print":
        if intent["type"] == "variable":
            return f'printf("%d\\n", {intent["name"]});'
        elif intent["type"] == "text":
            return f'printf("{intent["value"]}\\n");'