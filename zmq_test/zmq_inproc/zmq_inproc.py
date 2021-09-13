# encoding:utf-8
"""
    需要使用同一个上下文字 zmq.Context()
"""

import zmq
import threading


def server(zmq_sock):
    print("*********server")
    zmq_socket = zmq_sock.socket(zmq.REP)
    zmq_socket.bind("inproc://server")
    while True:
        recv = zmq_socket.recv_string()
        print("接收：　", recv)
        zmq_socket.send_string(str(recv)[:-1])
        print("发送: ", str(recv)[:-1])
        print()


def client(zmq_sock):
    print("*********client")
    zmq_sock = zmq_sock.socket(zmq.REQ)
    zmq_sock.connect("inproc://server")
    reqs = ["Are you ok?", u"Sleep?", u"Play game?", "上班吗"]
    for req in reqs:
        zmq_sock.send_string(req)
        print("发送: ", req)
        # time.sleep(10),  zmq服务器发送之后就会执行下一跳，无论客户段是否接收
        recv = zmq_sock.recv_string()
        print("接收：　", recv)


if __name__ == "__main__":
    zmq_sock = zmq.Context()
    s1 = threading.Thread(target=server, args=(zmq_sock,))
    s1.start()

    s2 = threading.Thread(target=client, args=(zmq_sock,))
    s2.start()