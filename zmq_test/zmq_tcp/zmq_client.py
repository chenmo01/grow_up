# encoding:utf-8
import zmq
import time
import sys

def run(req):
    zmq_sock = zmq.Context()
    zmq_sock = zmq_sock.socket(zmq.REQ)
    zmq_sock.connect("tcp://127.0.0.1:5000")
    zmq_sock.send_string(req)
    print("发送: ", req)
    # time.sleep(10),  zmq服务器发送之后就会执行下一跳，无论客户段是否接收
    recv = zmq_sock.recv_string()
    print("接收：　", recv)


if __name__ == "__main__":
    pre = ""
    if len(sys.argv) > 1:
        pre = sys.argv[1]
    reqs = ["Are you ok?", u"Sleep?", u"Play game?", "上班吗"]
    for req in reqs:
        run(pre+req)