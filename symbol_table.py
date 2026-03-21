# Scope-based symbol table
symbol_table_stack = [{}]
loop_stack = []

def is_declared(var):
    for scope in reversed(symbol_table_stack):
        if var in scope:
            return True
    return False

def declare_variable(var):
    symbol_table_stack[-1][var] = True

def exists_in_current_scope(var):
    return var in symbol_table_stack[-1]