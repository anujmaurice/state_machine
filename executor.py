import subprocess
import sys
import logging

class executeCommand():
	def __init__(self,cmdlist=[]):
		self.rcode = 2 # defaults to error
		self.logger = logging.getLogger('Maintenance.Automation')
		if not cmdlist:
			raise Exception
		else:
			self.cmdlist = cmdlist
	def execute(self):
		if type([]) == type(self.cmdlist):
			COMMAND = " ".join(self.cmdlist)
		else:
			COMMAND = self.cmdlist
		#COMMAND = "exit 2"
		self.logger.info("Executing .. {0}".format(COMMAND))
		#import pdb;pdb.set_trace()
		ssh = subprocess.Popen(["ssh", "-t","desktop", COMMAND],
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
