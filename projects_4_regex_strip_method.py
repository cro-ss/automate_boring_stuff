#Regex of the strip method
import re
def strip_1(arg):
    words_stripped=[]
    space=re.compile(r'''(\s*)
    ([a-zA-Z0-9]+)
    (\s*)''',re.VERBOSE)
    mo=space.findall(arg)
    for spaces in mo:
        words_stripped.append(spaces[1])
    print(mo)
    print(words_stripped[0])

print(':')
entry=input()
arg_1=input('Enter you argument')
strip_1(entry,arg_1)


def strip_2(arg,1_arg):
    words_stripped=[]
    space=re.compile(r'''(\s*)
    ([a-zA-Z0-9]+)
    (\s*)''',re.VERBOSE)
    mo=space.findall(arg)
    for spaces in mo:
        words_stripped.append(spaces[1])
    print(mo)
    print(words_stripped[0])


