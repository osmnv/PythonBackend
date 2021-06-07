
import socket
import argparse
import time
from threading import Lock
from concurrent.futures import ThreadPoolExecutor, as_completed


class Client:

    BUFF_SIZE = 4096

    def __init__(self,
                 thread_num,
                 filepath,
                 s_host='localhost',
                 s_port=15000):

            self.s_host = s_host
            self.s_port = s_port
            self.filepath = filepath
            self.thread_num = thread_num
            self.print_lock = Lock()


    def make_request(self, url):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect((self.s_host, self.s_port))
        sock.sendall(url.encode('utf-8'))

        resp = b''
        while True:
            chunk = sock.recv(self.BUFF_SIZE)
            resp += chunk
            if len(chunk) < self.BUFF_SIZE:
                break
        with self.print_lock:
            print(resp.decode('utf-8'))

    def run(self):
        with ThreadPoolExecutor(max_workers=self.thread_num) as thread_pool:
            with open(self.filepath, 'r') as f:
                for url in f:
                    thread_pool.submit(self.make_request, url)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', type=int, default=10)
    parser.add_argument('-f', type=str, default='urls.txt')
    args = parser.parse_args()

    begin_t = time.time()
    client = Client(args.m, args.f)
    client.run()
    end_t = time.time()
    print('Time exceeded: ', end_t - begin_t)