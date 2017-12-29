import os
import sys
#modulepath = os.getcwd() + '\\module'
#sys.path.append(modulepath)
print sys.path
import module.mymodule
module.mymodule.show()
print module.mymodule.name
module.mymodule.name = 'usemodule.py'
print module.mymodule.name

