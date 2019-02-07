import py_compile
py_compile.compile("hello.py")

'''
$ python
>>> import py_compile
>>> py_compile.compile('server.py')
>>> ^D
$ python ./server.pyc
'''