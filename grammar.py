from lark import Lark, Transformer, v_args

grammar = '''
start: expression

expression: commands

commands: read_pdf

read_pdf: "read_pdf" filename

filename: NAME "." EXTENSION

NAME: /[a-zA-Z0-9_-]+/
EXTENSION: "pdf" | "txt"

%import common.WS
%ignore WS
'''