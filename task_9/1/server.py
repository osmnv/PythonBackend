
import socket
import time
import argparse
import requests
import json
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from collections import Counter


def parse(url, raw_html, top=10):
    wordlist = BeautifulSoup(raw_html, "lxml").text.split()
    cleaned_wordlist = [word for word in wordlist if word[0].isalpha()]
    counter = Counter(cleaned_wordlist)
    data = {
        word: count for word, count in counter.most_common(min(top, len(cleaned_wordlist)))
    }
    return json.dumps({url.strip(): data}, indent=4)


class TCPServer:

    BUFF_SIZE = 4096

    def __init__(self,
                 thread_num,
                 top,
                 host='localhost',
                 port=15000):

        self.host = host
        self.port = port
        self.thread_num = thread_num
        self.top = top
        self.init_socket()
        self.log(f'init at {self.host}:{self.port}, threads = {self.thread_num}')

    def init_socket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    @staticmethod
    def log(txt):
        print(f"{time.ctime()}: {txt}")

    def handle_conn(self, client, address):
            data = b''
            while True:
                chunk = client.recv(self.BUFF_SIZE)
                data += chunk
                if len(chunk) < self.BUFF_SIZE:
                    break
            if data:
                url = data.decode('utf-8')
                raw_html = requests.get(url).text
                response = (parse(url, raw_html, self.top) + '\n').encode('utf-8')
                client.send(response)
                with self.counter_lock:
                    self.url_counter += 1
                    self.log(f'{self.url_counter} urls processed in total')

    def run(self):
        self.url_counter = 0
        self.counter_lock = Lock()

        self.sock.listen()
        self.log(f'listening at {self.host}:{self.port}')

        with ThreadPoolExecutor(max_workers=self.thread_num) as thread_pool:
            while True:
                client, address = self.sock.accept()
                thread_pool.submit(self.handle_conn, client, address)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', type=int, default=10)
    parser.add_argument('-k', type=int, default=5)
    args = parser.parse_args()

    server = TCPServer(thread_num=args.w, top=args.k)
    server.run()
    