def list_files(current_filetree, current_path=""):
    paths = []

    for i in current_filetree.keys():

        if current_filetree[i] == None:
            paths.append(f"{current_path}/{i}")
            continue
        paths = paths + list_files(current_filetree[i], f"{current_path}/{i}")

    return paths