def loader(file):
    def main_l():
        """ Use for load a html template """
        with open(file, 'r') as f:
            content = f.read()
        return content.replace('\n', '')
    return main_l

