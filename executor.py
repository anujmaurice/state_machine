import subprocess
import sys
import logging


def user_confirmation(f):

    def f_wrapper(self):
        print "-"*10
        print self.cmdlist
        print "-"*10
        u_input = raw_input("Press Y to proceed: ")
        if "Y" == u_input.upper().strip():
            self.logger.info("User input .. {0}".format(u_input))
            self.logger.info("Executing .. {0}".format(self.cmdlist))
            return f(self)
        else:
            self.logger.info("User input .. {0}".format(u_input))
            self.logger.info("Skipping Execution")
    return f_wrapper


class executeCommand():

    def __init__(self, cmdlist=[]):
        self.rcode = 2  # defaults to error
        self.logger = logging.getLogger('Maintenance.Automation')
        if not cmdlist:
            raise Exception
        else:
            self.cmdlist = cmdlist

    @user_confirmation
    def execute(self):
        if isinstance(self.cmdlist, type([])):
            COMMAND = " ".join(self.cmdlist)
        else:
            COMMAND = self.cmdlist
        ssh = subprocess.Popen(
                        ["ssh", "-t", "desktop", COMMAND],
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                        )
        ssh.wait()
        self.rcode = ssh.returncode
        result = ssh.stdout.readlines()
        if result:
            self.logger.info(result)
        return self.rcode
