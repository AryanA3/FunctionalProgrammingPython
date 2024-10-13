def toggle_case(line:str):
    if line.istitle():
        return f"{line.upper()}!!!"
    if line.isupper():
        return f"{line.capitalize().replace('!', '')}"
    if len(line) > 0 and line[1:].islower():
        return line.title()

    return line
