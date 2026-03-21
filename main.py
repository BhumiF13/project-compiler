from normalizer import normalize
from intent_extractor import extract_intent
from code_generator import generate_c_line
from file_handler import *
from symbol_table import loop_stack, symbol_table_stack

def main():
    filename = "output.c"
    initialize_file(filename)

    print("Enter commands (type 'done' to finish):")

    while True:
        user_input = input(">> ")

        if user_input.lower() == "done":
            break

        normalized = normalize(user_input)
        print("Normalized:", normalized)

        intent = extract_intent(normalized)
        print("Intent:", intent)

        if intent["action"] is None:
            print("Invalid command")
            continue

        c_line = generate_c_line(intent)

        if c_line:
            append_to_file(c_line, filename, intent["action"])

            if intent["action"] == "loop_end":
                loop_stack.pop()
                symbol_table_stack.pop()

    finalize_file(filename)
    print("C code successfully written to output.c")

if __name__ == "__main__":
    main()
