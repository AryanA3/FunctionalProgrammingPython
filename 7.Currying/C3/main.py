def new_resizer(max_width, max_height):
    def new_resizer_min(min_width = 0, min_height = 0):
        nonlocal max_width, max_height
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")

        def resizer(width, height):
            nonlocal min_height, min_width
            if width > max_width:
                width = max_width
            if height > max_height:
                height = max_height

            if width < min_width:
                width = min_width
            if height < min_height:
                height = min_height

            return width,height
        return resizer
    return new_resizer_min




def new_resizer_given_solution(max_width, max_height):
    def set_min_size(min_width=0, min_height=0):
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")

        def resize_image(width, height):
            new_width = max(min_width, min(width, max_width))
            new_height = max(min_height, min(height, max_height))
            return new_width, new_height

        return resize_image

    return set_min_size