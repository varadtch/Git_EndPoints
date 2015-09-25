__author__ = 'varadag'
__doc__ = 'Build an end point when called returns list of files in a directory'

import os
import sys
import traceback

class ListDirectories(object):
    """
    List the Files in a Directories
    Recusive and Non-Recursive
    """
    def __init__(self, directory, recursive=True):
        """
        Define the constructor and define the input parameters
        :param directory :type :str
        :param recursive :type :str
        """
        self.dir = directory
        self.recursive = recursive
        self.countOfFiles = 0
        self.Files = []
        self.FileCount = 0
        self.DirList = []
        self.DirCount = 0

    def listfiles(self):
        """
        Check the existance of the Directory. If the Directory Exists list the files in the directory.
        :return:
        """
        try:
            if os.path.isdir(self.dir):
                if self.recursive:
                    for root, dirs, files in os.walk(self.dir, topdown=False):
                        for file_name in files:
                            self.Files.append(os.path.join(root, file_name))

                        for dir_name in dirs:
                            self.DirList.append(os.path.join(root, dir_name))
                else:
                    for file_name in os.listdir(self.dir):
                        if os.path.isfile(os.path.join(self.dir, file_name)):
                            self.Files.append(os.path.join(self.dir, file_name))
                        else:
                            self.DirList.append(os.path.join(self.dir, file_name))
            else:
                raise Exception("DirNotFound")
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)

if __name__ == "__main__":
    L = ListDirectories("E:\Tutorials", False)
    L.listfiles()
    print L.Files
    print L.DirList

    M = ListDirectories("E:\Tutorials", True)
    M.listfiles()
    print M.Files
    print M.DirList
