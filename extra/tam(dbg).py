import subprocess
from tabulate import tabulate
import sys, os
import time
from threading import Thread
import fcntl
import numpy as np
import subprocess as sp, copy, threading as thr
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from colorama import Back
from termios import tcflush, TCIOFLUSH
# Terminals
def help():
    print("np - next page pp - previous page 0p - 1st page lp - last page go2 <number of page>", end='')
class childs2run:
    running: list = []
    viewer: list = []
    prnt: str = ""
class page_struct:
    num_page: int = 0
    num_cols: int = 3
    num_rows: int = 11
    num_spaces: int = 4
    c2r: childs2run
def log(msg, num_line: int, funcName: str):
    f = open("./it.log", mode="w")
    print(f"{funcName} said cmd = {msg} at line: {str(num_line)}", file=f)
def clear_screen():
    os.system('clear')
def init_view():
    c2r = childs2run()
    for v in range(1, len(sys.argv)):
        if sys.argv[v] == "-view_w":
            c2r.viewer.append(str(sys.argv[v + 1]))
            c2r.prnt.join(f"\n{c2r.viewer[-1]}")
    return c2r
def run_viewers(c2r: childs2run, fileListMain: list, cmd: str):
    viewer_indx, file_indx = cmd.split()
    viewer_indx = int(viewer_indx)
    file_indx = int(file_indx)
    file2run: str = fileListMain[file_indx]
    file2run = file2run[0:len(file2run) - 1]
    cmd = f'{c2r.viewer[viewer_indx]}' + ' ' + f'"{file2run}"'
    cmd = [cmd,]
    log(cmd, 46, "run_viewers")
    os.system(f"wall {cmd}")
    t = sp.Popen(cmd, shell=True)
    c2r.running.append(t)

def cmd_page(cmd: str, ps: page_struct, fileListMain: list):
    if cmd == "np":
        ps.num_page += 1
        return
    if cmd == "pp":
        ps.num_page -= 1
        return
    if cmd == "0p":
        ps.num_page = 0
        return
    if cmd == "lp":
        ps.num_page = len(fileListMain) // (ps.num_cols * ps.num_rows)
        return
    if cmd[0:3] == "go2":
        _, ps.num_page = cmd.split()
        ps.num_page = int(ps.num_page)
        return
    run_viewers(ps.c2r, fileListMain, cmd)
def manage_pages(fileListMain: list, ps: page_struct):
    cmd = ""
    c2r = ps.c2r
    while True:
        clear_screen()
        print(f"Viewers:{c2r.prnt}")
        print(tabulate(make_page_of_files(fileListMain, ps), tablefmt="fancy_grid"))
        print(cmd)
        cmd = input("Please enter Your command: ")
        if cmd == "help" or cmd == "" or cmd == "?":
            clear_screen()
            help()
            cmd = input("Please enter Your command: ")
        else:
            cmd_page(cmd, ps, fileListMain)
    return
def nop():
    return
def make_page_of_files(fileListMain: list, ps: page_struct):
    row: list =[]
    item = ""
    table: list = []
    stop = False
    num_page = ps.num_page * ps.num_cols * ps.num_rows
    for i in range(0, ps.num_rows):
        try:
            for j in range(0, ps.num_cols):
                indx = j + ps.num_cols * i + num_page
                try:
                    _, item = os.path.split(fileListMain[indx])
                except IndexError:
                    by0 = 1 / 0
                row.append(str(indx) + ":" + item + " " * ps.num_spaces)
        except ZeroDivisionError:
            break
        table.append(row)
        row = []
    return table


# Threads
stopCode = "∇\n"
class PIPES:
    def __init__(self, outNorm, outErr):
        self.outNorm_r = open(outNorm.name, mode="r", encoding="utf8")
        self.outErr_r = open(outErr.name, encoding="utf8", mode="r")
        self.outNorm_w = open(outNorm.name, encoding="utf8", mode="w+")
        self.outErr_w = open(outErr.name,  encoding="utf8", mode="w+")
        self.outNorm_name = outNorm.name
        self.outErr_name = outErr.name
        self.stdout = open(sys.stdin.name, mode="w+", encoding="utf8")
        self.stop = globals()['stopCode']
class lapse:
    find_files_start = 0
    find_files_stop = 0
    read_midway_data_from_pipes_start = 0
    read_midway_data_from_pipes_stop = 0
#manage files
def get_fd(fileName: str = ""):
    funcName = "get_fd"
    if fileName == "":
        fileName = "/tmp/tam.out"
    path, name = os.path.split(fileName)
    norm_out = open(f"{path}/norm_{name}", mode="a")
    err_out = open(f"{path}/err_{name}", mode="a")
    try:
        assert (norm_out > 0)
        assert (err_out > 0)
    except AssertionError:
        errMsg(f"can't open files {fileName}", funcName)
    finally:
        return norm_out, err_out
def errMsg(msg: str, funcName: str):
    print(f"{Fore.RED}{funcName} said: {msg}{Style.RESET_ALL}")
def read_midway_data_from_pipes(pipes: PIPES, fileListMain: list) -> None:
    funcName="read_midway_data_from_pipes"
    try:
        type(pipes.outNorm_r)
    except AttributeError:
        errMsg(funcName=funcName, msg=f"proc has wrong type {type(pipes)} id: {id(pipes)}")
    if pipes.outErr_r != "":
        errMsg(f"{pipes.outErr_r}", funcName)
    lapse.read_midway_data_from_pipes_start = time.time_ns()
    path0 = ""
    pipes.outNorm_r.flush()
    pipes.outNorm_r.seek(0)
    print(f"\nprobe write for _r {pipes.outNorm_r.read()} pipes.outNorm_r.fileno ={pipes.outNorm_r.fileno()} ")
    print(f"tst: {pipes.outNorm_r.read()}")
    prev_pos = 0
    cur_pos = 1
    for path in iter(pipes.outNorm_r.readline, b''):
        if path == pipes.stop:
            break
        if path !="":
          fileListMain.append(path)
          print(f"{path}", end='', file=sys.stdout)
        prev_pos = cur_pos
        cur_pos = pipes.outNorm_r.tell()
    lapse.read_midway_data_from_pipes_stop = time.time_ns()
    print(f"prev_pos = {prev_pos}, {cur_pos}")
    fileListMain = set(fileListMain)
    print(f"{funcName} exited")
def find_files(path: str, pipes: PIPES, in_name: str, tmp_file: str = None):
    funcName = "find_files"
    cmd = [f"find '{path}' -type f{in_name} > {pipes.outNorm_w.name};echo '\n{pipes.stop}'"]
    if tmp_file is None:
        cmd = [f"find '{path}' -type f{in_name};echo '\n{pipes.stop}'"]

    print(f"{cmd}")
    lapse.find_files_start = time.time_ns()
    proc = sp.Popen(
        cmd,
        stdout=pipes.outNorm_w,
        stderr=pipes.outErr_w,
        shell=True
        )
    lapse.find_files_stop = time.time_ns()
    print(f"{funcName} exited")
    return proc
# End threads
#measure performance
class perf0:
    def __init__(self, vec):
        self.vec = np.array(vec, dtype="int64")
        self.norm_vec = [s[0:3] for s in self.vec]

    def __str__(self):
        return str(self.norm_vec)

    def show_vec(self):
        return str(self.vec)


## normalize mask
def norm_msk(vecs: perf0, overlap_problem: int = 0):
    strip_msk = vecs.norm_vec[-1][1] ^ vecs.norm_vec[-2][1]
    msk_tail = 0
    while strip_msk > 0:
        msk_tail = msk_tail + 1
        strip_msk = strip_msk >> 1
    msk_tail = msk_tail + overlap_problem
    msk = vecs.norm_vec[-1][1] >> msk_tail
    msk = msk << msk_tail
    norm = [(s[0] ^ msk, s[1] ^ msk, s[2]) for s in vecs.norm_vec]
    norm_set = [s[2] for s in norm]
    norm_set = set(norm_set)
    print(f"norm = {norm}\nnorm_set = {norm_set}")
    return np.array(norm)


## mean value for perf0.norm_vec
def mean0(vecs: perf0, lenA: int):
    mean_vec0 = np.array((0, 0, 0), dtype="int64")
    norm_vec = norm_msk(vecs, 3)
    mean_vec0 = sum(mean_veci for mean_veci in norm_vec)
    mean_vec0 = mean_vec0 // lenA
    return mean_vec0


# measure the smallest time delta by spinning until the time changes
def measure_w_time():
    t0 = time.time_ns()
    t1 = time.time_ns()
    no_while = True
    while t1 == t0:
        t1 = time.time_ns()
        no_while = False
    return (t0, t1, t1 - t0, no_while)


def measure_w_perfCounter():
    t0 = time.perf_counter_ns()
    t1 = time.perf_counter_ns()
    no_while = True
    while t1 == t0:
        t1 = time.perf_counter_ns()
        no_while = False
    return (t0, t1, t1 - t0, no_while)


def time_samples(type0="time", num_of_samples=10):
    if type0 == "time":
        measure = measure_w_time
    else:
        measure = measure_w_perfCounter
    print(f"{type(measure)}")
    samples = perf0([measure() for i in range(num_of_samples)])
    print(f"mean val = {mean0(samples, num_of_samples)}")


# search params in cmd line
def get_arg_in_cmd(key: str, argv):
    cmd_len = len(argv)
    key0 = ''
    for i in range(1, cmd_len):
        key0 = argv[i]
        if key0 == key:
            return argv[i + 1]
    return None
def put_in_name() -> str:
    cmd_len = len(sys.argv)
    grep0 = ""
    for i in range(1, cmd_len):
        if sys.argv[i] == "-in_name":
            grep0 +=f"|grep -i '{str(sys.argv[i + 1])}'"
    return grep0
def cmd():
    cmd_len = len(sys.argv)
    cmd_key = ''
    cmd_val = ''
    num_of_samples = 1
    argv = copy.copy(sys.argv)
    for i in range(1, cmd_len):
        cmd_key = sys.argv[i]
        if cmd_key == "-ver":
            print("Version: 1, Revision: 1")
        if cmd_key == "-time_prec":
            i = i + 1
            cmd_val = sys.argv[i]
            num_of_samples = get_arg_in_cmd("-num_of_samples", argv)
            if num_of_samples is None:
                num_of_samples = 10
            if cmd_val == "time":
                time_samples("time", int(num_of_samples))
            else:
                time_samples(cmd_val, int(num_of_samples))
        if cmd_key == "-find_files":
            base_path = get_arg_in_cmd("-path0", argv)
            filter_name = put_in_name()
            if filter_name is None:
                filter_name = "*"
            if base_path is None:
                base_path = "./"
            fileListMain = []
            tmp_file = get_arg_in_cmd("-tmp_file", argv)
            outNorm, outErr = get_fd(tmp_file)
            tmp_file = None
            print(f"IDs: norm = {outNorm}, err = {outErr}")
            pipes = PIPES(outNorm, outErr)
            thr_find_files: Thread = thr.Thread(target=find_files, args=(base_path, pipes, filter_name, tmp_file))
            thr_find_files.start()
            thr_read_midway_data_from_pipes: Thread = thr.Thread(target=read_midway_data_from_pipes, args=(pipes, fileListMain))
            thr_read_midway_data_from_pipes.start()
            thr_find_files.join()
            thr_read_midway_data_from_pipes.join()
            delta_4_entries = f"Δt for entry points of find_files() & read_midway_data_from_pipes(): {lapse.find_files_start - lapse.read_midway_data_from_pipes_start} ns"
            вар = 5
            print(delta_4_entries)
            print(f"len of list = {len(fileListMain)}")
            ps = page_struct()
            ps.c2r = init_view()
            table = make_page_of_files(fileListMain, ps)
            print(tabulate(table, tablefmt="fancy_grid"))
            manage_pages(fileListMain, ps)
cmd()