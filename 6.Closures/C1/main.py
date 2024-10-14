def new_clipboard(initial_clipboard):
    clipboard_cpy = initial_clipboard.copy()

    def copy_to_clipboard(key, value):
        clipboard_cpy[key] = value

    def paste_from_clipboard(key):
        return clipboard_cpy.get(key, "")

    return copy_to_clipboard, paste_from_clipboard