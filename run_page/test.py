import os
def test():
    sum = 1 + os.environ["number"]
    print(sum)
    
if __name__ == '__main__':
    test()