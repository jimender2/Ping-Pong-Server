import socket


def Main():
    HOST = "0.0.0.0"
    PORT = 8888

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    c, addr = s.accept()
    msg = "hello"
    msg = msg.encode("utf-8")
    s.sendall(msg)
