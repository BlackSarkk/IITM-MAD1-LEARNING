
#*****************************************
#! Extracting codes from another file
#*****************************************
#*****************************************
 
#* Method 1:
'''
import file2
'''

#* Method 2:
'''
exec(open("file2.py").read())
'''

#* Method 3:
# Via cli, do - python3 file2.py





#*****************************************
#! Extracting Args from cli
#*****************************************
#*****************************************

# do - python3 file1.py 123 abs

import sys
print(sys.argv[0])       # first arg is always filename: file1.py
print(type(sys.argv[1])) # type is alwsy string
print(len(sys.argv))     # length is including file1.py : 3






