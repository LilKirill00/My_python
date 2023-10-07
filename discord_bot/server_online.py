from mcstatus import JavaServer


def online_check(check):
    try:
        server = JavaServer.lookup(check)
        status = server.status()
        return status.players.online
    except:
        return -1


def ping_check(check):
    try:
        server = JavaServer.lookup(check)
        status = server.status()
        return round(status.latency, 1)
    except:
        return -1


if __name__ == '__main__':
    ip = "hypixel.net"
    print(online_check(ip))
    print(ping_check(ip))
