"""
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). 
So "xxyz" counts but "x.xyz" does not.
"""

def xyz_there(str):
  if len(str)>=3:
    if str[:3] == 'xyz':
        return True
    for i in range(len(str)-3):
      if str[i] !='.' and str[i+1:i+4] == 'xyz':
        return True
  return False

if __name__ == "__main__":
    print(xyz_there('abc.xyzxyz'))
    print(xyz_there('1.xyz.xyz2.xyz'))