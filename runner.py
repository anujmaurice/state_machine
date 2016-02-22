import logging

from config.test import RM_PROCESS,HTTPD_PROCESS,POSTFIX_PROCESS,COMMAND_1
from state import ProcessState, Command
from utils import initlogging
from pexec import prunner

initlogging()
logger = logging.getLogger('Maintenance.Automation')
#pro = ProcessState(RM_PROCESS)
#httpd = ProcessState(HTTPD_PROCESS)
#postfix = ProcessState(POSTFIX_PROCESS)
# logger.info("test")
#state = 'start'
#p = prunner(5,
#            [
#                (pro,'changestate',[state]),
#                (httpd,'changestate',[state]),
#                (postfix,'changestate',[state])
#            ]
#            )
#p.join()
#import pdb;pdb.set_trace()
#print "@"*5

#if pro.state == httpd.state == postfix.state =='stop':
#    print "All stopped"


#pro.changestate(state)
#httpd.changestate(state)
#postfix.changestate(state)
#if pro.state == 'start':
#	pro.changestate('stop')

cc = Command(COMMAND_1)
import pdb;pdb.set_trace()
cc.executestate("yeah")
cc.executestate("oh")
