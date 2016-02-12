# place for all the utils

from executor import executeCommand
import logging

def initlogging():
    logger = logging.getLogger('Maintenance.Automation')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

def verifystate(nextstate):
    e  = executeCommand(nextstate.get("verify"))
    rcode = e.execute()
    if rcode == 0:
        return True
    else:
        return False


def getstate(pdefn):
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
