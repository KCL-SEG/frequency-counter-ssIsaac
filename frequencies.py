"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        if isinstance(item, str):    
            if item in frequencies:
                frequencies[item] +=1
            else:
                frequencies[item] = 1
        elif (isinstance(item, int)):
            x = str(item)
            if x in frequencies:
                frequencies[x] +=1
            else:
                frequencies[x] = 1
    return frequencies
