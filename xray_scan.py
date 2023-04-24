import subprocess
import concurrent.futures
from tqdm import tqdm
import time
import os
import argparse

py_path=os.path.dirname(os.path.realpath(__file__))
parser = argparse.ArgumentParser(description="xray多线程扫描")
parser.add_argument('-t','--thread', type=int, default=3, dest='thread_num', help='线程数')

args = parser.parse_args()
thread_num=args.thread_num

def run_scan(target):
    global py_path
    cmd = ["./xray.exe", "webscan", "--browser-crawler", target, "--html-output", "report__datetime__.html"]
    try:
        process = subprocess.Popen(cmd, creationflags=subprocess.CREATE_NEW_CONSOLE)
        while process.poll() is None:
            time.sleep(3)
    except Exception as e:
        print(f"file {e}")

def main():
    targets = []
    file=open("url.txt","r",encoding='utf-8')
    for i in file:
        i=i.strip('\n')
        targets.append(i)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_num) as executor:
        futures = [executor.submit(run_scan, target) for target in targets]
        with tqdm(total=len(futures), ncols=80) as pbar:
            for future in concurrent.futures.as_completed(futures):
                pbar.update(1)

if __name__ == '__main__':
    main()
