from helang.lexer import Lexer
from helang.parser import Parser
from helang.notes_remover import NotesRemover


if __name__ == '__main__':
    script_path = '../great_with_copyrights.he'
    
    notesRemover = NotesRemover(script_path)
    notesRemover.remove()
    
    with open('../great_with_copyrights.he', 'r') as f:
        content = f.read()
    lexer = Lexer(content)
    parser = Parser(lexer.lex())
    env = dict()
    parser.parse().evaluate(env)
