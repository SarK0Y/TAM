import sys
import os
import time
import numpy as np
import subprocess, copy
import asyncio as aio
from asyncio.subprocess import Process
#async funcs
path, head = os.path.split("/us")
print(head)
sys.exit()
async def read_midway_data_from_pipes(tnp_file0: str, fileListMain: list) -> None:
    print(f"tmpFile = {tnp_file0}")
    return
    tmpFile = open(tmp_file0, "r")
    fileSize = os.path.getsize(tmp_file)
    fileSize_cur = 0
    fileGotFinalSize = 0
    countLines = 0
    while fileGotFinalSize < 3:
        if fileSize != fileSize_cur:
            fileList = tmpFile.readlines()
            fileListMain += fileList
            countLines = len(fileListMain)
        fileSize_cur = os.path.getsize(tnp_file)
        if fileSize == fileSize_cur:
            fileGotFinalSize += 1
        else:
            fileSize = fileSize_cur
    fileListMain = set(fileListMain)

async def find_files(path: str, name: str, tmp_file: str):
    if tmp_file == "":
        tmp_file = "/tmp/find_files4TAM.tmp"
    cmd = f"find {path} -type f|grep -i {name} >> {tmp_file} "
    proc = await aio.create_subprocess_exec(
        "find", "/", "-type", "d",
        stdout=aio.subprocess.PIPE,
        stderr=aio.subprocess.PIPE,
        )
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


async def cmd():
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
            filter_name = get_arg_in_cmd("-in_name", argv)
            if filter_name is None:
                filter_name = "*"
            if base_path is None:
                base_path = "./"
            fileListMain = []
            tmp_file = get_arg_in_cmd("-tmp_file", argv)
            task_find_files = aio.create_task(find_files(base_path, filter_name, tmp_file))
            task_read_midway = aio.create_task(read_midway_data_from_pipes(tmp_file, fileListMain))
            await task_find_files
            await task_read_midway
aio.run(cmd())
