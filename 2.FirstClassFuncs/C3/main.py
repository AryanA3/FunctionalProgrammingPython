def restore_documents(originals, backups):
    return set(
        filter(
            lambda doc: not doc.isdigit(),
            map(lambda doc: doc.upper(), originals + backups),
        )
    )