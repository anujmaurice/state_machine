from executor import executeCommand
import logging


class ProcessState():
    # Class for process states

    def __init__(self, process_defn,force_yes=False):
        self.state = self.getstate(process_defn)
        self.logger = logging.getLogger('Maintenance.Automation')
        self.logger.info("Assigning state as {0}".format(self.state))
        self.defn = process_defn
        self.force_yes = force_yes

    def getstate(self, pdefn):
        # iterates through each defined state
        # in the process definition and trying
        # to check at what state the object is in
        logger = logging.getLogger('Maintenance.Automation')
        statelist = []
        for k in pdefn.keys():
            state, cmd = k, pdefn.get(k).get('verify')
            logger.info("Verifying state '{0}' using command '{1}'".format(
                state, cmd))
            e = executeCommand(cmd, self.force_yes)
            rcode = e.execute()
            if rcode == 0:
                statelist.append(k)
        if len(statelist) > 1:
            raise Exception
        elif len(statelist) == 1:
            return statelist[0]
        else:
            raise Exception

    def changestate(self, nstate):
        # to change the state of the object to another state.
        # state is transistioned only after the verification returns
        # a success.
        if self.state == nstate:
            self.logger.info("State is already {0}".format(nstate))
            return True
        nextstate = self.defn.get(nstate)
        command = nextstate.get('command')
        rcode = self.execute(command)
        if rcode == 0:
            if self.verifystate(nextstate):
                self.logger.info("switching state from {0} to {1}".format(
                    self.state, nstate
                    )
                )
                self.state = nstate
                self.logger.info("switched to {0}".format(self.state))
                return True
        else:
            return False

    def verifystate(self, nextstate):
        e = executeCommand(nextstate.get("verify"),self.force_yes)
        rcode = e.execute()
        if rcode == 0:
            return True
        else:
            return False

    def execute(self, command):
        e = executeCommand(command,self.force_yes)
        rcode = e.execute()
        return rcode


class Command():

    def __init__(self, process_defn, force_yes=False):
            states = ["Started", "Stopped", "Error"]
            self.state = None
            self.logger = logging.getLogger('Maintenance.Automation')
            self.logger.info("Assigning state as {0}".format(self.state))
            self.defn = process_defn
            self.force_yes = force_yes

    def executestate(self, nstate):
        nextstate = self.defn.get(nstate)
        command = nextstate.get("command")
        rcode = self.execute(command)
        if rcode == 0:
            self.state = nstate
            self.logger.info("switched to {0}".format(self.state))
            return True

    def execute(self, command):
        e = executeCommand(command,self.force_yes)
        rcode = e.execute()
        return rcode
