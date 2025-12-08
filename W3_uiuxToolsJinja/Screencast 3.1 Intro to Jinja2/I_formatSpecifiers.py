
#**********************************************
#! Format Specifiers I
#**********************************************
#**********************************************

'''

TEMPLATE = """
Hello {name}    
"""
# We can even send empty {} or location like this {0}


def main():
    print(TEMPLATE.format(name="Rahul"))

if __name__ == "__main__":     # execute only if run as a script, wont work if we import it
    
    # When Python runs a file, it sets a special variable:
        # __name__ = "__main__" if the file is being run directly
        # __name__ = "filename" if the file is being imported
    

    main()

'''


#**********************************************
#! Format Specifiers II
#**********************************************
#**********************************************

'''


# TEMPLATE = """This is {p} and this is {n}"""
TEMPLATE = """This is {p:+} and this is {n:+}"""   # means "print the sign of the number too"

def main():
    print(TEMPLATE.format(p=5, n=-7))

if __name__ == "__main__":    
    main()


'''

#**********************************************
#! Format Specifiers III
#**********************************************
#**********************************************


TEMPLATE = """This is in decimal={value:d} and this is in hex={value:x}"""   

def main():
    print(TEMPLATE.format(value=10))

if __name__ == "__main__":    
    main()
