"""
    进程间通讯
"""
# encoding:utf-8
import zmq


def run():
    zmq_sock = zmq.Context()
    zmq_sock = zmq_sock.socket(zmq.REP)
    zmq_sock.bind("ipc:///opt/work/zmq_test/zmq_ipc/sock.sock")
    while True:
        recv = zmq_sock.recv_string()
        print("接收：　", recv)
        zmq_sock.send_string(str(recv)[:-1])
        print("发送: ", str(recv)[:-1])
        print()


if __name__ == "__main__":
    run()
