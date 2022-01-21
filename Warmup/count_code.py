"""
Return count of 'code' in string. Except 'd' in 'code' there can be any letter.
"""

import re

def count_code(str):
    count = re.findall('co.e', str)
    return len(count)

if __name__ == "__main__":
    print(count_code('cozexxcope'))