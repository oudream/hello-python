bogon:singleton1 oudream$ p3 ./main.py
['/ddd/cpy/cpy/cpy/hello/pattern/singleton1', '/ddd/cpy/cpy', '/ddd/cpy/cpy/cpy/hello/pattern/singleton1', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']
i am main...:  __main__
locals():
__name__ __main__
__doc__ None
__package__ None
__loader__ <_frozen_importlib_external.SourceFileLoader object at 0x1038577b8>
__spec__ None
__annotations__ {}
__builtins__ <module 'builtins' (built-in)>
__file__ ./main.py
__cached__ None
sys <module 'sys' (built-in)>



bogon:pattern oudream$ p3 -m singleton1.main
['', '/ddd/cpy/cpy', '/ddd/cpy/cpy/cpy/hello/pattern', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']
i am main...:  __main__
locals():
__name__ __main__
__doc__ None
__package__ singleton1
__loader__ <_frozen_importlib_external.SourceFileLoader object at 0x103e5e630>
__spec__ ModuleSpec(name='singleton1.main', loader=<_frozen_importlib_external.SourceFileLoader object at 0x103e5e630>, origin='/ddd/cpy/cpy/cpy/hello/pattern/singleton1/main.py')
__annotations__ {}
__builtins__ <module 'builtins' (built-in)>
__file__ /ddd/cpy/cpy/cpy/hello/pattern/singleton1/main.py
__cached__ /ddd/cpy/cpy/cpy/hello/pattern/singleton1/__pycache__/main.cpython-36.pyc
sys <module 'sys' (built-in)>