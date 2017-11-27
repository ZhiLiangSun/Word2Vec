def openfile(file_path):
    with open(file_path) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like '\n' at the end of each line
    content = [x.strip() for x in content]
    return content
