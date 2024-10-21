def args_logger(*args, **kwargs):
    for i in range(len(args)):
        print(f'{i+1}. {args[i]}')

    for k in sorted(kwargs.keys()):
        print(f'* {k}: {kwargs[k]}')