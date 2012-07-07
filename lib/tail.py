#!/usr/bin/env python



import time, os, sys
import logging

class Tail(object):
    def __init__(self, tailed_file, group, delay_time):
        
        ''' Initiate a Tail instance.
            Check for file validity, assigns callback function to standard out.
        '''

        #self.check_file_validity(tailed_file)
        self.delay_time=delay_time
        self.tailed_file = tailed_file
        self.group = group
        self.callback = sys.stdout.write
    
    
    def check_file_validity(self):
        ''' Check whether the a given file exists, readable and is a file '''
        if not os.access(self.tailed_file, os.F_OK):
            logging.error("Log '%s' does not exist" % (self.tailed_file))
            return False
            
        if not os.access(self.tailed_file, os.R_OK):
            logging.error("Log '%s' not readable" % (self.tailed_file))
            return False
        
        if os.path.isdir(self.tailed_file):
            logging.error("Log '%s' is a directory" % (self.tailed_file))
            return False
        
        return True
            

    def follow(self):
        #Set the filename and open the file
        self.file = open(self.tailed_file,'r')
        
        #Find the size of the file and move to the end
        st_results = os.stat(self.tailed_file)
        st_size = st_results[6]
        self.file.seek(st_size)
        inode=self.getInode()
        
        while 1:
            new_inode=self.getInode()
            if inode != new_inode:
                logging.info("Log inode have change for " + self.tailed_file + " Reloading the File")
                self.file.close()
                self.file = open(self.tailed_file,'r')
                inode=new_inode
                
            where = self.file.tell()
            line = self.file.readline()
            if not line:
                time.sleep(self.delay_time)
                self.file.seek(where)
            else:
                #print line, # already has newline
                self.callback(line, self.group)


    def register_callback(self, func):
        ''' Overrides default callback function to provided function. '''
        self.callback = func

        
    def getInode(self):
        '''get inode for file'''
        if not os.path.exists(self.tailed_file):
            return None
        else:
            return os.stat(self.tailed_file)[1]
    
 
        
'''        
class TailError(Exception):
    def __init__(self, msg):
        self.message = msg
    def __str__(self):
        return self.messagev
'''