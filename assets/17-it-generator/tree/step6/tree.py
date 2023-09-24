def tree(cls, dis_level, level=0):
    if level <= dis_level:
        yield cls.__name__, level
        for sub_cls in cls.__subclasses__():
            yield from tree(sub_cls, dis_level, level=level+1)


def display(cls, display_level=5):
    for cls_name, level in tree(cls, display_level - 1):
        indent = ' ' * 4 * level
        print(f'{indent}{cls_name}')


if __name__ == '__main__':
    display(BaseException, 2)
