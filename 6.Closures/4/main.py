def new_collection(initial_docs):
    initial_docs_cpy = initial_docs.copy()
    def modify_init_cpy(str_to_app):
        initial_docs_cpy.append(str_to_app)
        return initial_docs_cpy
    return modify_init_cpy