from symbol_table import loop_stack

def initialize_file(filename):
    with open(filename, "w") as file:
        file.write("#include <stdio.h>\n\n")
        file.write("int main() {\n")

def append_to_file(c_line, filename, action):
    if action == "loop_end":
        indent = "    " * len(loop_stack)
    else:
        indent = "    " * (len(loop_stack) + 1)

    with open(filename, "a") as file:
        file.write(f"{indent}{c_line}\n")

def finalize_file(filename):
    with open(filename, "a") as file:
        file.write("    return 0;\n")
        file.write("}\n")