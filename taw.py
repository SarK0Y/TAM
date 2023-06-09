import gc
import subprocess
from tabulate import tabulate
import sys, os, signal
import time
from threading import Thread
import numpy as np
import subprocess as sp, copy, threading as thr
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import ctypes, msvcrt
from colorama import Back
# import pywin32
import win32file
import win32con
import win32security
import win32api
import pywintypes
import codecs
import win32console


class keys:
    dirty_mode = False

    def __init__(x):
        dirty_mode = x

    def setDirty():
        dirty_mode = True


# Win32/64
def makeSharedFile(fileName: str):
    secur_att = win32security.SECURITY_ATTRIBUTES()
    secur_att.Initialize()
    # fileName = codecs.decode(f"b'{fileName}'", encoding=GetWindowsCodePage())
    print(f"file = {fileName}")
    hfile = win32file.CreateFileW(fileName, \
                                  win32con.GENERIC_READ | win32con.GENERIC_WRITE, \
                                  win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE, \
                                  secur_att, \
                                  win32con.OPEN_ALWAYS, \
                                  win32con.FILE_ATTRIBUTE_NORMAL, 0)
    return hfile


# End W32/64
# Terminals
def signal_manager(sig, frame):
    print(f"sig = {sig}")


# signal.signal(signal.SIGINT, signal_manager)
def SYS():
    no_SYS = os.path.exists("/tmp/no_SYS")
    no_SYS1 = get_arg_in_cmd("-SYS", sys.argv)
    if no_SYS == True or no_SYS1 == "1":
        os.system("rm -f /tmp/no_SYS")
        sys.exit(0)
    print("\r\nSee You Soon\nBye.. bye, my Dear User 🙂")
    sys.exit(0)


def SetAlias(name: str, val: str) -> None:
    cmd = f"powershell.exe Set-Alias -Name '{name}' -Value '{val}'"
    sp.Popen(cmd, shell=True)


def SetDefaultKonsoleTitle():
    out = get_arg_in_cmd("-path0", sys.argv)
    try:
        out += f" {put_in_name()}"
        out = out.replace("'", "")
        print(f"konsole title = {out}")
    except TypeError:
        out = "cmd is empty"
    win32console.SetConsoleTitle(f"{out}")
    # sp.Popen("powershell.exe", f"$host.ui.RawUI.WindowTitle = 'tst'", shell=True)


def self_recursion():
    no_SYS = os.path.exists("/tmp/no_SYS")
    no_SYS1 = get_arg_in_cmd("-SYS", sys.argv)
    if no_SYS == True or no_SYS1 == "1":
        os.system("rm -f /tmp/no_SYS")
        sys.exit(0)
    else:
        os.system("touch -f /tmp/no_SYS")
    cmd_line = ""
    for i in range(1, len(sys.argv)):
        cmd_line += f" {sys.argv[i]}"
    cmd_line += f";{sys.executable} {sys.argv[0]} -SYS 1"
    cmd = f"{sys.executable} {sys.argv[0]} {cmd_line}"
    os.system(cmd)
    os.system("rm -f /tmp/no_SYS")


def banner0(delay: int):
    colsize = os.popen("powershell $host.UI.RawUI.MaxWindowSize.Width", 'r').read().split()[0]
    while True:
        typeIt = "(c) SarK0Y 2023".center(int(colsize), "8")
        print(f"\r{typeIt}", flush=True, end='')
        time.sleep(delay)
        typeIt = "(c) Knyazhev Evgeney 2023".center(int(colsize), "|")
        print(f"\r{typeIt}", flush=True, end='')
        time.sleep(delay)
        typeIt = "(c) Knyazhev Evgeney 2023".center(int(colsize), "/")
        print(f"\r{typeIt}", flush=True, end='')
        time.sleep(delay)
        typeIt = "(c) Knyazhev Evgeney 2023".center(int(colsize), "-")
        print(f"\r{typeIt}", flush=True, end='')
        time.sleep(delay)
        typeIt = "(c) Knyazhev Evgeney 2023".center(int(colsize), "+")
        print(f"\r{typeIt}", flush=True, end='')
        time.sleep(delay)
        typeIt = "(c) Knyazhev Evgeney 2023".center(int(colsize), "=")
        typeIt = "(c) SarK0Y 2023".center(int(colsize), "oo")
        print(f"\r{typeIt}", flush=True, end='')
        time.sleep(delay)


def info():
    clear_screen()
    colsize = os.popen("powershell $host.UI.RawUI.MaxWindowSize.Width", 'r').read().split()[0]
    print(" Project: Tiny Automation Manager. ".center(int(colsize), "*"))
    print(" WWW: https://alg0z.blogspot.com ".center(int(colsize), "*"))
    print(" E-MAIL: sark0y@protonmail.com ".center(int(colsize), "*"))
    print(" Supported platforms: TAM for Linux; TAW stands for TAM Windows Version ".center(int(colsize), "+"))
    print(" Version: 1. ".center(int(colsize), "*"))
    print(" Revision: 1. ".center(int(colsize), "*"))
    print(f"\nlicense/Agreement:".title())
    print(
        "Personal usage will cost You $0.00, but don't be shy to donate me.. or You could support me any other way You want - just call/mail me to discuss possible variants for mutual gains. ?")
    print("Commercial use takes $0.77 per month from You.. or just Your Soul 😇😜")
    print("my the Best Wishes to You 🙃")
    print(" Donations: https://boosty.to/alg0z/donate ".center(int(colsize), "~"))
    print("\n")
    try:
        banner0(.3)
    except KeyboardInterrupt:
        SYS()
    except Exception:
        SYS()


def help():
    print("np - next page pp - previous page 0p - 1st page lp - last page go2 <number of page>", end='')


class childs2run:
    running: list = []
    viewer: list = []
    prnt: str = ""
    full_path = ""


class page_struct:
    num_page: int = 0
    num_cols: int = 3
    col_width = 70
    num_rows: int = 11
    num_spaces: int = 4
    c2r: childs2run


def achtung(msg):
    os.system(f"wall '{msg}'")


def log(msg, num_line: int, funcName: str):
    f = open("./it.log", mode="w")
    print(f"{funcName} said cmd = {msg} at line: {str(num_line)}", file=f)


def clear_screen():
    dirtyFlag = keys()
    if dirtyFlag.dirty_mode == True:
        return
    print(f"keys.dirty = {dirtyFlag.dirty_mode}")
    os.system('cls')


def init_view(c2r: childs2run):
    i = 0
    for v in range(1, len(sys.argv)):
        if sys.argv[v] == "-view_w":
            c2r.viewer.append(str(sys.argv[v + 1]))
            c2r.prnt += f"\n  {i}: {c2r.viewer[-1]}"
            i += 1
    return c2r


def run_viewers(c2r: childs2run, fileListMain: list, cmd: str):
    funcName = "run_viewers"
    viewer_indx, file_indx = cmd.split()
    viewer_indx = int(viewer_indx)
    file_indx = int(file_indx)
    file2run: str = fileListMain[file_indx]
    file2run = file2run[0:len(file2run) - 1]
    file2run = file2run.replace("$", "\$")
    file2run = file2run.replace(";", "\;")
    entry = str(c2r.viewer[viewer_indx]).find("\'")
    exe_file = ""
    viewer_args = ""
    if entry > -1:
        exe_file = str(c2r.viewer[viewer_indx])[0:entry]
        viewer_args = str(c2r.viewer[viewer_indx])[entry:]
        viewer_args = viewer_args.strip("\'")
        cmd = ["powershell", f'& "{exe_file}"', f"'{viewer_args}'", f"'{file2run}'"]
    else:
        exe_file = str(c2r.viewer[viewer_indx])
        cmd = ["powershell", f'& "{exe_file}"', f"'{file2run}'"]
    print(f"{funcName}: cmd = {cmd}")
    t = sp.Popen(cmd, shell=True)
    c2r.running.append(t)


def cmd_page(cmd: str, ps: page_struct, fileListMain: list):
    lp = len(fileListMain) // (ps.num_cols * ps.num_rows)
    if cmd == "np":
        ps.num_page += 1
        if ps.num_page > lp:
            ps.num_page = lp
        return
    if cmd == "pp":
        ps.num_page -= 1
        return
    if cmd == "0p":
        ps.num_page = 0
        return
    if cmd == "lp":
        ps.num_page = lp
        return
    if cmd[0:3] == "go2":
        _, ps.num_page = cmd.split()
        ps.num_page = int(ps.num_page)
        if ps.num_page > lp:
            ps.num_page = lp
        return
    if cmd[0:2] == "fp":
        _, file_indx = cmd.split()
        # achtung(fileListMain[int(file_indx)])
        ps.c2r.full_path = f"file {file_indx}\n{str(fileListMain[int(file_indx)])}"
        return
    run_viewers(ps.c2r, fileListMain, cmd)


def manage_pages(fileListMain: list, ps: page_struct):
    cmd = ""
    c2r = ps.c2r
    while True:
        clear_screen()
        print(f"Viewers: \n{c2r.prnt}\n\nFull path to {c2r.full_path}")
        table, too_short_row = make_page_of_files(fileListMain, ps)
        if too_short_row == 0:
            ps.num_cols = 2
            table, too_short_row = make_page_of_files(fileListMain, ps)
        try:
            print(tabulate(table, tablefmt="fancy_grid", maxcolwidths=[ps.col_width]))
        except IndexError:
            errMsg("Unfortunately, Nothing has been found.", "TAM")
        print(cmd)
        try:
            cmd = input("Please, enter Your command: ")
        except KeyboardInterrupt:
            SYS()
        if cmd == "help" or cmd == "" or cmd == "?":
            clear_screen()
            help()
            cmd = input("Please, enter Your command: ")
        else:
            cmd_page(cmd, ps, fileListMain)
    return


def nop():
    return


def make_page_of_files(fileListMain: list, ps: page_struct):
    row: list = []
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
    too_short_row = len(table)
    return table, too_short_row


# Threads
stopCode = "!:$TOP:!\n"


def GetWindowsCodePage() -> str:
    return f"cp{os.popen('powershell.exe [System.Text.Encoding]::Default.CodePage', mode='r').read().split()[0]}"


class PIPES:
    def __init__(self, outNorm, outErr):
        codepage = GetWindowsCodePage()
        hfile = makeSharedFile(outNorm)
        print(f"hfile = {hfile}")
        self.outNorm_w = open(outNorm, encoding=codepage, mode="w")
        self.outNorm_r = open(outNorm, encoding=codepage, mode="r")
        self.outErr_w = open(outErr, encoding=codepage, mode="w+")
        self.outErr_r = open(outErr, encoding=codepage, mode="r")
        self.outNorm_name = outNorm
        self.outErr_name = outErr
        # self.stdout = open(sys.stdin.name, mode="w+", encoding=codepage)
        self.stop = globals()['stopCode']

    def __del__(self):
        try:
            print("For backup's sake, yet another time:)))")
            SYS()
        except:
            nop()


class lapse:
    find_files_start = 0
    find_files_stop = 0
    read_midway_data_from_pipes_start = 0
    read_midway_data_from_pipes_stop = 0


# manage files
def GetFileNames(fileName: str):
    funcName = "get_fd"
    if fileName == "":
        fileName = "/tmp/tam.out"
    path, name = os.path.split(fileName)
    norm_out = f"{path}\\norm_{name}"
    err_out = f"{path}\\err_{name}"
    return norm_out, err_out


def get_fd(fileName: str = ""):
    funcName = "get_fd"
    if fileName == "":
        fileName = "/tmp/tam.out"
    path, name = os.path.split(fileName)
    well_encoded_path = f"{path}\\norm_{name}".encode(encoding=GetWindowsCodePage())
    norm_out = open(well_encoded_path, mode="w+")
    well_encoded_path = f"{path}\\err_{name}".encode(encoding=GetWindowsCodePage())
    err_out = open(well_encoded_path, mode="w+")
    err_out.write(f"{funcName}")
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
    funcName = "read_midway_data_from_pipes"
    try:
        type(pipes.outNorm_r)
    except AttributeError:
        errMsg(funcName=funcName, msg=f"proc has wrong type {type(pipes)} id: {id(pipes)}")
    # if pipes.outErr_r != "":
    #    errMsg(f"{pipes.outErr_r}", funcName)
    lapse.read_midway_data_from_pipes_start = time.time_ns()
    path0 = ""
    pipes.outNorm_r.flush()
    pipes.outNorm_r.seek(0)
    print(f"\nprobe write for _r {pipes.outNorm_r.read()} pipes.outNorm_r.fileno ={pipes.outNorm_r.fileno()} ")
    prev_pos = 0
    cur_pos = 1
    outNorm_r = open(pipes.outNorm_name, mode="r")
    for path in iter(pipes.outNorm_r.readline, b''):
        if path == pipes.stop:
            print(f"{funcName} {pipes.stop}")
            break
        if len(path) > 0:
            fileListMain.append(path)
        prev_pos = cur_pos
        cur_pos = pipes.outNorm_r.tell()
    lapse.read_midway_data_from_pipes_stop = time.time_ns()
    print(f"prev_pos = {prev_pos}, {cur_pos}")
    fileListMain = set(fileListMain)
    print(f"{funcName} exited")


def find_files(path: str, pipes: PIPES, in_name: str, tmp_file: str = None):
    funcName = "find_files"
    try:
        path = f"{path[0:2].capitalize()}{path[2:len(path)]}"
    except IndexError:
        path = path.capitalize()
    print(f"outNorm.name = {pipes.outNorm_w.name}")
    opts = "Get-ChildItem -Path " + f"{path}" + " -Filter * -Recurse -File | %{$_.FullName}" + f"{in_name}"
    cmd = ["powershell", f"{opts}"]
    # cmd = [f"powershell", "Set-PSDebug -Trace 2;Get-Process;echo 'this tst'"]
    print(f"{funcName} got cmd = {cmd}")
    lapse.find_files_start = time.time_ns()
    try:
        proc = sp.Popen(
            cmd,
            stdout=pipes.outNorm_w,
            stderr=pipes.outErr_w,
            shell=True
        )
    except:
        print(f"{funcName} catched")
        nop()
    proc.communicate()
    outNorm_w = open(pipes.outNorm_name, mode="a", encoding=GetWindowsCodePage())
    outNorm_w.write(f"\n{pipes.stop}")
    outNorm_w.close()
    lapse.find_files_stop = time.time_ns()
    print(f"\n{funcName} exited")
    return proc


# End threads
# measure performance
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
def checkArg(arg: str) -> bool:
    cmd_len = len(sys.argv)
    for i in range(1, cmd_len):
        key0 = sys.argv[i]
        if key0 == arg:
            return True
    return False


def get_arg_in_cmd(key: str, argv):
    cmd_len = len(argv)
    for i in range(1, cmd_len):
        key0 = argv[i]
        if key0 == key:
            return argv[i + 1]
    return None


def if_no_quotes(num0: int, cmd_len: int) -> str:
    grep0 = ''
    i0: int
    SetAlias("grep", "findstr")
    for i0 in range(num0, cmd_len):
        if sys.argv[i0][0:1] != "-":
            grep0 += f" {sys.argv[i0]}"
        else:
            grep0 = f"|Select-String -Pattern '{grep0[1:len(grep0)]}'"
            if grep0 == "|Select-String -Pattern ''":
                grep0 = ""
            if sys.argv[i0] == "-in_name":
                i0 -= 1
            return [grep0, i0]


def put_in_name() -> str:
    cmd_len = len(sys.argv)
    final_grep = ""
    num0 = []
    i = []
    i0 = 1
    i.append(i0)
    while i0 < cmd_len:
        if sys.argv[i0] == "-in_name":
            i0 = i0 + 1
            tmp = if_no_quotes(i0, cmd_len)
            if tmp is not None:
                final_grep += f"{tmp[0]}"
                i0 = tmp[1]
        i0 += 1
    return final_grep


def is_key_in_cmdline(key: str):
    for arg in sys.argv:
        if arg == key:
            return True
    return False


def cmd():
    SetAlias("grep", "findstr")
    os.system("echo 'tst string\nwrong str'|grep -i tst")
    sys.argv.append("-!")  # Stop code
    print(f"argv = {sys.argv}")
    SetDefaultKonsoleTitle()
    if is_key_in_cmdline("-dirty"):
        keys.dirty_mode = True
    if is_key_in_cmdline("-ver"):
        info()
        return
    print("start cmd")
    sys.argv[0] = str(sys.argv)
    # self_recursion()
    cmd_len = len(sys.argv)
    cmd_key = ''
    cmd_val = ''
    num_of_samples = 1
    argv = copy.copy(sys.argv)
    for i in range(1, cmd_len):
        cmd_key = sys.argv[i]
        if "-argv0" == cmd_key:
            print(f"argv = {sys.argv}")
            sys.exit()
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
            if checkArg("-argv0"):
                print(f"argv = {sys.argv}")
                sys.exit()
            base_path = get_arg_in_cmd("-path0", argv)
            filter_name = put_in_name()
            if filter_name is None:
                filter_name = "*"
            if base_path is None:
                base_path = "./"
            fileListMain = []
            tmp_file = get_arg_in_cmd("-tmp_file", argv)
            outNorm, outErr = GetFileNames(tmp_file)
            tmp_file = None
            print(f"IDs: norm = {outNorm}, err = {outErr}")
            pipes = PIPES(outNorm, outErr)
            thr_find_files: Thread = thr.Thread(target=find_files, args=(base_path, pipes, filter_name, tmp_file))
            thr_find_files.start()
            thr_read_midway_data_from_pipes: Thread = thr.Thread(target=read_midway_data_from_pipes,
                                                                 args=(pipes, fileListMain))
            thr_read_midway_data_from_pipes.start()
            time.sleep(3)
            # thr_find_files.join()
            # thr_read_midway_data_from_pipes.join()
            delta_4_entries = f"dt for entry points of find_files() & read_midway_data_from_pipes(): {lapse.find_files_start - lapse.read_midway_data_from_pipes_start} ns"
            print(delta_4_entries)
            print(f"len of list = {len(fileListMain)}")
            ps = page_struct()
            cols = get_arg_in_cmd("-cols", argv)
            rows = get_arg_in_cmd("-rows", argv)
            col_w = get_arg_in_cmd("-col_w", argv)
            if rows:
                ps.num_rows = int(rows)
            if cols:
                ps.num_cols = int(cols)
            if col_w:
                ps.col_width = int(col_w)
            ps.c2r = childs2run()
            ps.c2r = init_view(ps.c2r)
            table = make_page_of_files(fileListMain, ps)
            manage_pages(fileListMain, ps)


cmd()
