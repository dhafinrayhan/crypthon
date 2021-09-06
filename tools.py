def str_to_ascii_list(s: str) -> list:
    return [ord(i) for i in s]


def ascii_list_to_str(l: list) -> str:
    return ''.join([chr(i) for i in l])


def filter_alpha(s: str) -> str:
    return ''.join([i for i in s if i.isalpha()])


