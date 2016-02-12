# shutdown of a cluster
# starting of a cluster
from executor import executeCommand
from utils import verifystate,getstate
import logging


class ProcessState():
	def __init__(self,process_defn):
		states = ["Started","Stopped","Error"]
		self.state = getstate(process_defn)
		self.logger = logging.getLogger('Maintenance.Automation')
		self.logger.info("Assigning state as {0}".format(self.state))
		self.defn = process_defn
	def changestate(self,nstate):
		if self.state == nstate:
			self.logger.info("State is already {0}".format(nstate))
			return
		nextstate = self.defn.get(nstate)
		command = nextstate.get('command')
		rcode = self.execute(command)
		if rcode == 0:
			if verifystate(nextstate):
				self.logger.info("switching state from {0} to {1}".format(
					self.state,nstate
					)
				)
				self.state = nstate ##
				self.logger.info("switched to {0}".format(self.state))
				return True
		else:
			return False
	def execute(self,command):
		e = executeCommand(command)
		rcode = e.execute()
		return rcode
