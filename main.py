from normalizer import normalize
from intent_extractor import extract_intent
from code_generator import generate_c_line
from file_handler import *
from symbol_table import loop_stack, symbol_table_stack
from input_voice import get_voice_input

def main():
    filename = "output.c"
    initialize_file(filename)

    while True:
        user_input = get_voice_input()

        if user_input is None:
            print("❌ Invalid command")
            continue

        # ✅ FIX: exact match instead of "in"
        if user_input.strip() == "stop":
            print("stopping...")
            break

        try:
            normalized = normalize(user_input)
            print("Normalized:", normalized)

            intent = extract_intent(normalized)
            print("Intent:", intent)

            if intent["action"] is None:
                print("❌ Invalid command")
                continue

            c_line = generate_c_line(intent)

            if c_line:
                append_to_file(c_line, filename, intent["action"])

                if intent["action"] == "loop_end":
                    if loop_stack:
                        loop_stack.pop()
                    if symbol_table_stack:
                        symbol_table_stack.pop()

        except Exception:
            print("❌ Invalid command")
            continue

    finalize_file(filename)
    print("C code successfully written to output.c")

if __name__ == "__main__":
    main()