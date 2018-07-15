#coding:utf-8
def get_curdir():
    import os
    return os.getcwd()

#测试代码不能直接写，需要写在如下结构中,name是python内置的1个专有变量
if __name__ == '__main__':
    print(get_curdir())
    
    


