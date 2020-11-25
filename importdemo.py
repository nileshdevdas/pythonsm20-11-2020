


def calculate_tax():
    from utils import check_if_empty as ck
    print("calling ck...........")
    ck()
    print(locals())

print(globals())
calculate_tax()
# i do have the activity mapped to the  import inside a function 
# can i import at file level *Yes it will become globals 
# can i import at function level *Yes it will become locals
# can i import all at a one time  using * yes may cause ambigous imports 
# can i import only  the module  Yes  but invocation module.function 
# can i import with aliase and single function Yes this is the best practice 
# does import a module and import a package is differnet to end user no for python yes 




