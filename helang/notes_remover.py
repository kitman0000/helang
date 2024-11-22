class NotesRemover:
    """ According to He's requirement, need to remove all the notes at the begaining of the code file.
        Especially when there's orignal author signature
    """    
    
    def __init__(self, path: str):
        self.script_path = path
        with open(self.script_path, 'r') as f:
            self.contents = f.read().splitlines()
        
    
    def remove(self):
        lines_to_remove = 0
        include_author = False
        
        for line in self.contents:
            if line.lstrip().startswith('//') or line == '':
                lines_to_remove += 1
            else:
                break
            if 'author' in line.lower():
                include_author = True
        
        self.contents = self.contents[lines_to_remove:]
        
        # New script here, no notes, no author signature, wonderfull for He!
        with open(self.script_path, 'w') as f:
            f.write('\n'.join(self.contents))
        
        