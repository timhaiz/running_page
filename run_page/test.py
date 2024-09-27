import os
def test():
    sum = 1 + int(os.getenv('number'))
    print(sum)
    
if __name__ == '__main__':
    test()