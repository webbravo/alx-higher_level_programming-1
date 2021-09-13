#!/usr/bin/env python3

def no_c(my_string):
    copy_string = [x for x in my_string if x != 'c' and x != 'C']
    return("".join(copy_string))