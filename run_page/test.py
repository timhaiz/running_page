import os
def test():
    sum = 1 + os.getenv('number')
    print(sum)