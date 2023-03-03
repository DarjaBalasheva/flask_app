import hashlib


def check_hashed_message(data):
    data = str(data)
    data = "".join(data.split())

    if len(data) > 0 and len(data) < 64:
        data = hashlib.md5(data.encode()).hexdigest()
        return data
    elif len(data) > 64:
        return "Слишком длинная строка"
    elif len(data) == 0:
        return "Строка не должа быть пустой"
    else:
        return "Что-то сломалось"
