__author__ = 'varadag'
__doc__ = '''Build an end point that checks and returns the status of all components that it depends on - Eg: Is MongoDB
            still up etc.. Checking for services and dependency.
          '''

from subprocess import Popen, PIPE
import platform
if platform.system() == "Linux":
    from re import split


class GetProcessList(object):
    """
    Get the list of process active on the system.
    """
    def __init__(self):
        """
        Initialize the processlist array to Null
        """
        self.processlist = []
        self.result = None
        self.process_status = {}

    def listprocess(self):
        """
        Based on platform identify the currently available process in the system
        """
        if platform.system() == "Windows":
            sub_process = Popen(['tasklist'], shell=False, stdout=PIPE)
            sub_process.stdout.readline()
            for process in sub_process.stdout:
                self.processlist.append(" ".join(process.split()[:1]).strip())
            else:
                print "Completed the process fetch from %s"%(platform.system())
            self.result = True
        elif platform.system() in ["Linux", "Darwin"]:
            sub_process = Popen(['ps', 'aux'], shell=False, stdout=PIPE)
            sub_process.stdout.readline()
            for line in sub_process.stdout:
                self.processlist.append(" ".join(split(" *", line)[10:]).strip())
            else:
                print "Completed the process fetch from %s"%(platform.system())
            self.result = True
        else:
            raise Exception("PlatformCouldNotBeDetermined")

    def processlookup(self, *args):
        """
        :param : *args :type : List of process key words to be serached in list of available processed
        """
        self.listprocess()
        assert self.result == True

        self.process_status["Active"] = []
        self.process_status["InActive"] = []

        self.process_status["Active"] = list(set(filter(lambda proc:proc in args, self.processlist)))
        self.process_status["InActive"] = list(set(filter(lambda proc:proc not in self.processlist, args)))

if __name__ == "__main__":
    P = GetProcessList()
    P.processlookup("chrome.exe", "node.exe", "notepad++.exe", "mongo")
    print P.process_status["Active"], P.process_status["InActive"]
