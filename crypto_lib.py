import random

def Crypto_Encode(text):
    enc = str.maketrans(
                "#$%^&=~`<>!\"\'№;:?/*-+.,\\|[]{}()!@ ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя",
                "/*-+.,\\|[]{}()!@#$%^&=~`<>!\"\'№;:?_NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm5678901234РСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПрстуфхцчшщъыьэюяабвгдеёжзийклмноп"
            )

    res = ""

    for let in text:
        res += chr(random.randint(33, 126)) + str.translate(let, enc) + "—"

    print('Process: Шифрование\nResult: {res}'.format(res=res))
    return res


def Crypto_Decode(text):
    text = text.split("—")

    dec = str.maketrans(
                "/*-+.,\\|[]{}()!@#$%^&=~`<>!\"\'№;:?_NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm5678901234РСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПрстуфхцчшщъыьэюяабвгдеёжзийклмноп",
                "#$%^&=~`<>!\"\'№;:?/*-+.,\\|[]{}()!@ ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
            )

    res = ""

    for let in text:
        if (let == ""):
            pass
        res += str.translate(let[1:2], dec)

    print('Process: Расшифрование\nResult: {res}'.format(res=res))
    return res
