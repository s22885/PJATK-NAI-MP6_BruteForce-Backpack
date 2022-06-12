import os


def get_data(data: str, separator: str = ","):
    if not data[0]:
        return None
    lines = data[1].splitlines(keepends=False)
    res = []
    if len(lines) != 3:
        return None
    fstline = lines[0].split(sep=" ")
    if len(fstline) != 2:
        return None
    for i in fstline:
        try:
            tmp = int(i)
            res.append(tmp)
        except ValueError:
            return None
    for i in lines[1:]:
        tmp = i.split(sep=separator)
        if len(tmp) != res[1]:
            return None
        res.append([int(v) for v in tmp])
    return res


def data_load(path: str):
    if os.path.isfile(path):
        return [True, open(path, encoding="utf-8").read()]
    return [False]
