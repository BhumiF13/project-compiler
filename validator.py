import re
from symbol_table import *

def is_valid_expression(expr):
    return re.fullmatch(r"[\w\s+\-*/%]+", expr) is not None

def check_variables_in_expression(expr):
    tokens = re.findall(r"[a-zA-Z_]\w*", expr)

    for token in tokens:
        if not token.isdigit():
            if not is_declared(token):
                print(f" Error: Variable '{token}' not declared")
                return False
    return True

def validate_intent(intent):

    if intent["action"] == "create":
        if exists_in_current_scope(intent["name"]):
            print(f"Error: Variable '{intent['name']}' already declared")
            return False

        if not is_valid_expression(intent["value"]):
            print(" Invalid expression")
            return False

        if not check_variables_in_expression(intent["value"]):
            return False

        declare_variable(intent["name"])
        return True

    elif intent["action"] == "loop_start":
        if exists_in_current_scope(intent["name"]):
            print(f" Error: Variable '{intent['name']}' already declared")
            return False

        symbol_table_stack.append({})
        declare_variable(intent["name"])
        loop_stack.append(intent["name"])
        return True

    elif intent["action"] == "loop_end":
        if not loop_stack:
            print(" Error: No loop to end")
            return False
        return True

    elif intent["action"] == "set":
        if not is_declared(intent["name"]):
            print(f" Error: Variable '{intent['name']}' not declared")
            return False

        if not is_valid_expression(intent["value"]):
            print(" Invalid expression")
            return False

        if not check_variables_in_expression(intent["value"]):
            return False

        return True

    elif intent["action"] == "print":
        if intent["type"] == "variable":
            if not is_declared(intent["name"]):
                print(f" Error: Variable '{intent['name']}' not declared")
                return False
            return True

        elif intent["type"] == "text":
            return intent["value"] is not None

    return False