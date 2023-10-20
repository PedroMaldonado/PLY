import ply.lex as lex

#List of token names. This is always required
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Regular expression rules for simple tokens.
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# A regular expression rule with some action code.
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers.
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs).
t_ignore = '\t' # "'\t'' '"


# Error handling rule.
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer.
lexer = lex.lex()

# Test it out
data = '''
3 + 4 * 10
  + -20 *2
'''

# Give the lexer some input.
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break # No more input
    #print(tok)
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
    # The tok.type and tok.value attributes contain the type and value of the token itself. 
    # tok.line and tok.lexpos contain information about the location of the token. 
    # tok.lexpos is the index of the token relative to the start of the input text.

# Iteration protocol - Alternative
# for tok in lexer:
    # print(tok)

