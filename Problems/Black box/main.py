# use the function blackbox(lst) that is already defined
list_ = [1, 2, 3]
if id(blackbox(list_)) == id(list_):
    print('modifies')
else:
    print('new')