#!/usr/bin/env python



import time, os, sys


class Tail(object):
    def __init__(self, tailed_file, group):
        
        ''' Initiate a Tail instance.
            Check for file validity, assigns callback function to standard out.
        '''

        self.check_file_validity(tailed_file)
        self.tailed_file = tailed_file
        self.group = group
        self.callback = sys.stdout.write
    
    
    def check_file_validity(self, file_):
        ''' Check whether the a given file exists, readable and is a file '''
        if not os.access(file_, os.F_OK):
            raise TailError("File '%s' does not exist" % (file_))
        if not os.access(file_, os.R_OK):
            raise TailError("File '%s' not readable" % (file_))
        if os.path.isdir(file_):
            raise TailError("File '%s' is a directory" % (file_))

    def follow(self, s):
        #Set the filename and open the file
        self.file = open(self.tailed_file,'r')
        
        #Find the size of the file and move to the end
        st_results = os.stat(self.tailed_file)
        st_size = st_results[6]
        self.file.seek(st_size)
        
        while 1:
            where = self.file.tell()
            line = self.file.readline()
            if not line:
                time.sleep(s)
                self.file.seek(where)
            else:
                #print line, # already has newline
                self.callback(line, self.group)


    def register_callback(self, func):
        ''' Overrides default callback function to provided function. '''
        self.callback = func

 
        
        
class TailError(Exception):
    def __init__(self, msg):
        self.message = msg
    def __str__(self):
        return self.messagev
