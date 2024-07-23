from lark import Lark,exceptions
from evaluator import Evaluator
from grammar import grammar

parser = Lark(grammar, parser='lalr', transformer=Evaluator())

def parse_expression(expression):
    print(f'expression: {expression}')
    try:
        return parser.parse(expression)
    except exceptions.UnexpectedToken as e:
        print(f'''Error UNEXPECTED TOKEN: 
            general: {e}
            token con error: {e.token}
            token esperado: {e.expected}
            token type: {e.token.type}
            token value: {e.token.value}
            token previo: {e.token_history}
        ''')
        if e.expected.pop() == "URL":
            print('Error: URL no válido')
             
    except exceptions.UnexpectedCharacters as e:
        print(f'''Error UNEXPECTED CHARACTERS:
            general: {e}
            char: {e.char}
            args: {e.args}
            allowed: {e.allowed}
            considered rules: {e.considered_rules}
            considered tokens: {e.considered_tokens}
            token previo: {e.token_history} - {e.token_history[0]}
        ''')
        prev_token = e.token_history[0]
        if e.allowed.pop() == 'URL':
            print('Error: URL no válido')
        elif prev_token == "read_pdf":
            print('Error: El archivo no es un PDF')
        else:
            print('Error: El archivo no es un YAML')
    except Exception as e:
        return print(f'Error: {e}')
        
    
