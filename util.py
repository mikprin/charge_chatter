#Util funcs
import socket

def debug_msg(msg,lvl):
    print(msg)

def error(msg):
    sys.exit(msg)

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False
