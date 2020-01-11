import sys
import logging

LOG = logging.getLogger(__name__)

def get_fname(stack_frame):
    fname = sys._getframe(stack_frame).f_code.co_name
    return fname

def log_message(msg):
    LOG.info('%s(): %s', get_fname(2), msg)

def log_entry():

    # We are logging the function which called this function and its caller
    fname = get_fname(1)
    caller = get_fname(2)

    # Log name of executing function and name of caller
    LOG.info(fname +"(): caller: " +caller)

def log_entry_msg(msg):

    # We are logging the function which called this function and its caller
    fname = get_fname(1)
    caller = get_fname(2)

    # Log name of executing function and name of caller
    LOG.info(fname +"(): caller: " +caller +" [" +msg +"]")

def log_qos_msg(msg):

    # We are logging the function which called this function and its caller
    fname = get_fname(1)
    caller = get_fname(2)

    # Log name of executing function and name of caller
    LOG.info(fname +"(): rolaya:qos: caller: " +caller +" [" +msg +"]")    

    