import ipaddress
import socket


def target_is_up(target_ip: ipaddress.IPv4Address, target_port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((str(target_ip), target_port))
    if result == 0:
        sock.close()
        return True
    else:
        sock.close()
        return False
