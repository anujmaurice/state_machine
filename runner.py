import logging

from config.test import RM_PROCESS
from state import ProcessState
from utils import initlogging

initlogging()
logger = logging.getLogger('Maintenance.Automation')
pro = ProcessState(RM_PROCESS)
#logger.info("test")
pro.changestate('start')
if pro.state == 'start':
	pro.changestate('stop')
