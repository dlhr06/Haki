from lark import Lark
from evaluator import Evaluator

grammar = open('grammar.lark').read()
parser = Lark(grammar, parser='lalr', transformer=Evaluator())

def parse_expression(expression):
    try:
        return parser.parse(expression)
    except Exception as e:
        return f'Error: {e}'
