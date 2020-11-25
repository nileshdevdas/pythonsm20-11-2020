import helpers

# module import
# import utils

# using a spefific function import
# from utils import check_if_empty

# using a specific function import with alias
# from utils import check_if_empty as cfi


# import all function of the module using a *
from utils import *

print(check_if_empty())

helpers.write_log()


# 1. of the fundamental thing we have in python 
# Flexibility is import even a single function with or without a alias 
# Felxibility is to import a complete module 
# Flexibility is to also import only all functions 
# a. import <moduleName>
# where modulename is nothhing but .py file 
# b. when we want to import only functions specific ones
#   from <module> import <function>  as <alias>
# c . when i want to import all the functions 
#    from module  import * 




