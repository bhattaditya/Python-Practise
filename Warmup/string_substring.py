"""
adding substring at every iteration.

0 
0-1
0-1-2
"""

def string_splosion(str):
    s = ''
    for i in range(len(str)):
        s += str[:i+1]
    return s

if __name__ == "__main__":
    print(string_splosion('code'))