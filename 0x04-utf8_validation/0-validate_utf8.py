#!/usr/bin/python3
""" UTF-8 validation """



def validUTF8(data):
    """ 
    method that determines if a given data set represents a valid utf-8 
    """

    mbytes = 0
    
    k1 = 1 << 7
    k2 = 1 << 6
    for j in data:
        k = 1 << 7
        if mbytes == 0:
            while k and j:
                mbytes += 1
                k = k >> 1
              if mbytes == 0:
                  continue
              if mbytes == 1 or mbytes > 4:
                  return False
              else:
                  if not (j & k1 and not (j & k2)):
                      return False
                mbytes -= 1
            return mbytes == 0
