# shutdown of a cluster
# starting of a cluster
from executor import executeCommand
#from utils import verifystate,getstate
import logging


class ProcessState():
	def __init__(self,process_defn):
		states = ["Started","Stopped","Error"]
		self.state = self.getstate(process_defn)
		self.logger = logging.getLogger('Maintenance.Automation')
		self.logger.info("Assigning state as {0}".format(self.state))
		self.defn = process_defn

	def getstate(self, pdefn):
		logger = logging.getLogger('Maintenance.Automation')
		statelist = []
		for k in pdefn.keys():
			state,cmd = k, pdefn.get(k).get('verify')
			logger.info("Verifying state '{0}' using command '{1}'".format(state,cmd))
			e = executeCommand(cmd)
			rcode = e.execute()
			if rcode == 0:
				statelist.append(k)
		if len(statelist)>1:
			raise Exception
		elif len(statelist) == 1:
			return statelist[0]
		else:
			raise Exception

	def changestate(self,nstate):
		if self.state == nstate:
			self.logger.info("State is already {0}".format(nstate))
			return True
		nextstate = self.defn.get(nstate)
		command = nextstate.get('command')
		rcode = self.execute(command)
		if rcode == 0:
			if self.verifystate(nextstate):
				self.logger.info("switching state from {0} to {1}".format(
					self.state,nstate
					)
				)
				self.state = nstate ##
				self.logger.info("switched to {0}".format(self.state))
				return True
		else:
			return False

	def verifystate(self,nextstate):
		e  = executeCommand(nextstate.get("verify"))
		rcode = e.execute()
		if rcode == 0:
			return True
		else:
			return False

	def execute(self,command):
		e = executeCommand(command)
		rcode = e.execute()
		return rcode


class Command():

	def __init__(self,process_defn):
			states = ["Started","Stopped","Error"]
			self.state = None
			self.logger = logging.getLogger('Maintenance.Automation')
			self.logger.info("Assigning state as {0}".format(self.state))
			self.defn = process_defn

	def executestate(self,nstate):
		nextstate = self.defn.get(nstate)
		command = nextstate.get(command)
		rcode = self.execute(command)
		if rcode == 0:
			self.state = nstate
			self.logger.info("switched to {0}".format(self.state))
			return True

	def execute(self,execute):
		e = executeCommand(command)
		rcode = e.execute()
		return rcode
