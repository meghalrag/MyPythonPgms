class check(Exception):
    pass
b=input("b:")
try:
    # assert b>=18,'exception throws'
    # print 'go ahead'

    if b<18:
        raise check('exception throws')
    else:
        print 'go ahead'
except check,arg:
    print"?????,",arg
