import sys
import time
import numpy as np
import subprocess
import _tam
tst: str = """
print(f'{x} ', sep=' ', flush=True)
"""
x = 7
t = eval(tst)
t0 = exec(tst)
print(f"{t0} 4 exec, {t} 4 eval")
sys.exit(1)
class perf0:
    def __init__(self, vec):
        self.vec = np.array(vec, dtype="int64")
        self.norm_vec = [s[0:3] for s in self.vec]

    def __str__(self):
        return str(self.norm_vec)
    def show_vec(self):
        return str(self.vec)
## normalize mask
def norm_msk(vecs: perf0):
    strip_msk = vecs.norm_vec[-1][1] ^ vecs.norm_vec[-2][1]
    msk_tail = 0
    while strip_msk > 0:
        msk_tail = msk_tail + 1
        strip_msk = strip_msk >> 1
    msk = vecs.norm_vec[-1][1] >> msk_tail
    msk = msk << msk_tail
    norm = [(s[0] ^ msk, s[1] ^ msk, s[2]) for s in vecs.norm_vec]
    print(f"norm = {norm}")
    return np.array(norm)

## mean value for perf0.norm_vec
def mean0(vecs: perf0, lenA):
    mean_vec0 = np.array((0, 0, 0), dtype="int64")
    norm_vec = norm_msk(vecs)
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
    return (t0, t1, t1-t0, no_while)

def measure_w_perfCounter():
    t0 = time.perf_counter_ns()
    t1 = time.perf_counter_ns()
    no_while = True
    while t1 == t0:
        t1 = time.perf_counter_ns()
        no_while = False
    return (t0, t1, t1-t0, no_while)


def time_samples(type0 = "time", num_of_samples = 10):
    if type0 == "time":
        measure = measure_w_time
    else:
        measure = measure_w_perfCounter
    print(f"{type(measure)}")
    samples = perf0([measure() for i in range(num_of_samples)])
    vecs = np.array(samples.norm_vec)
    vec0 = (0, 0, 0)
    vec0 = np.array(vec0, dtype="int64")
    print(f"vecs={vecs}")
    for veci in vecs:
        print(f"veci = {veci}\nvec0 = {vec0}")
        vec0 = veci + vec0
        print(f"veci = {veci}\nvec0 = {vec0}")
    for s in samples.vec:
       print (f"samples={s}\nvec0 = {vec0}")
    print(f"mean val = {mean0(samples, num_of_samples)}")
#search params in cmd line
def get_arg_in_cmd(key: str):
    cmd_len = len(sys.argv)
    key0 = ''
    for i in range(1, cmd_len):
        key0 = sys.argv[i]
        if key0 == key:
            return sys.argv[i + 1]
        else:
            return None
def cmd():
    cmd_len = len(sys.argv)
    cmd_key = ''
    cmd_val = ''
    num_of_samples = 1
    for i in range(1, cmd_len):
        cmd_key = sys.argv[i]
        if cmd_key == "-ver":
            print("Version: 1, Revision: 1")
        if cmd_key == "-time_prec":
            i = i + 1
            cmd_val = sys.argv[i]
            num_of_samples = get_arg_in_cmd("-num_of_samples")
            if num_of_samples is None:
                num_of_samples = 10
            if cmd_val == "time":
                time_samples("time", int(num_of_samples))
            else:
                time_samples(cmd_val, int(num_of_samples))
cmd()

