def tree(cls):
    yield cls.__name__, 0
    for sub_cls in cls.__subclasses__():
        yield sub_cls.__name__, 1
        for sub_sub_cls in sub_cls.__subclasses__():
            yield sub_sub_cls.__name__, 2


if __name__ == '__main__':
    for cls_name, level in tree(BaseException):
        indent = ' ' * 4 * level
        print(f'{indent}{cls_name}')
