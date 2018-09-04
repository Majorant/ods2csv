"""
find and change contract names

"""
import re


def contract_rename(inp: str):
    """change leteers to latin and lowercase chars"""
    try:

    if 'а' in inp.lower():
        return inp.lower().replace('а', 'a')
    elif 'к' in inp.lower():
        return inp.lower().replace('к', 'k')
    else:
        return inp.lower()


def search(st: str):
    """return contract num"""
    # pattern of contract
    pattern = r'\d+[aAkKаАкК]\d+'
    tmp = []
    for line in st.split('\r\n'):
        if re.search(pattern, str(line)) is not None:
            tmp.append(contract_rename(re.search(pattern, str(line)).group()))
    return tmp
