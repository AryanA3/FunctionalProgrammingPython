def create_markdown_image(alt_text):
    text = f'![{alt_text}]'
    def create_markdown_url(url):
        nonlocal text
        url = url.replace('(', '%28')
        url = url.replace(')', '%29')
        url = f'({url})'
        text += url

        def create_markdown_title(title = ""):
            nonlocal text
            space = ''
            if title != "":
                title = f'"{title}"'
                space = ' '
            return text.replace(')' , '') + space + title + ')'
        return create_markdown_title
    return create_markdown_url