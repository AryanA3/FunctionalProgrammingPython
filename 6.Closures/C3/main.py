def css_styles(initial_styles):
    styles_cpy = initial_styles.copy()

    def add_style(selector, property, value):
        nonlocal styles_cpy
        if styles_cpy.get(selector, -1) == -1:
            styles_cpy[selector] = {property : value}
        else:
            styles_cpy[selector][property] = value
        return styles_cpy
    return add_style