grammar = '''
start: expression

expression: commands

commands: read_pdf
        | get_professional_summary
        | get_motivation_letter
        | apply_for_job

read_pdf: "read_pdf" filename_pdf

get_professional_summary: "get_professional_summary" filename_yaml

get_motivation_letter: "get_motivation_letter" filename_yaml

apply_for_job: "apply_for_job" filename_yaml filename_pdf route credentials

filename_pdf: NAME_PDF
filename_yaml: NAME_YAML
credentials: NAME_YAML
route: URL

NAME_PDF: /[\w-]+\.pdf/
NAME_YAML: /[\w-]+\.(yaml|yml)/
URL: /(https:\/\/|http:\/\/)?([\w-]{3,}\.)?\w{3,}\.\w{2,}([\w\/:\.%&\?=-]+)?/

%import common.WS
%ignore WS
'''