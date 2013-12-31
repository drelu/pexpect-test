import urlparse
import pdb
import glob
import errno
import sys
import os
import stat
import logging
import traceback
import pexpect
from pexpect import TIMEOUT



child = pexpect.spawn(os.path.join(os.getcwd(),"test.sh"), 
                      timeout=None)
child.timeout=10
try:
    child.expect("password:",timeout=10, searchwindowsize=5024)
    password_error=True
except Exception as ex:
    print("No password prompt error found" + str(ex))

output = child.readlines()
print("Run %s Output: %s"%(command, str(output)))