"""subTern == SubTerminal (Nested/Normalized)"""
import os
import sys
import re
import subprocess as sp
import signal
import codecs
#import click
import io
import copy
import time
from datetime import time as clock, datetime
#if __name__ == "__main__":
#from tam import tam.achtung, tam.kCodes, tam.keyCodes, tam.checkArg, tam.get_arg_in_cmd, tam.errMsg
try:
    import tam
except ModuleNotFoundError:
    pass
    """"""""""""
try:
    from sark0y_tam import _tam as tam
except ModuleNotFoundError:
    pass
""""""""
class ctlCodes:
    stop = "∇\n"
    stop0 = "∇"
    locale: str|None = None
    class Prime_subTerminal:
        ExitCode = 101
    class readOutput:
        stopped = 0
        paused = 1
    class checkANDwipeStopCode:
        hOKkey = 1
        noCode = 0
        empty = 2
    class write_log:
        running = False
        failed: int = 0
        count: int = 0
class tmp:
    nope = None
    class term_app:
        dict_f: dict = {}
    class control_subTerm:
        nope = None
    class write_logs:
        none = None
class modes:
    stderr2stdin: bool = False
    prime_stdin: bool = False
    class mc:
        active: bool = False
class env:
    cmd_story: str = ""
    cur_cmd: str = "" 
    USER_HOME_DIR: str = "unknown"
    class fds:
        tamish_logs = None
        tamish_cmds = None
    class tamish_log:
        name: str = ""
class inlines:
    off = """
pass
"""
    write_logs = """
write_logs()
"""
    write_logs_on = """
write_logs()
"""
    reset_modes = """
try:
    import tam
except ModuleNotFoundError:
    pass
try:
    from sark0y_tam import _tam as tam
except ModuleNotFoundError:
    pass
try:
    tam.errMsg_dbg(f"{inlines.reset_modes=}", "inlines")
except AttributeError:
    pass
modes.mc.active = False
modes.prime_stdin = False
modes.stderr2stdin = False
ctlCodes.write_log.running = False
ctlCodes.write_log.failed = 0
"""
    getPressedKey = """
tmp.control_subTerm.Key = "none"
"""
    getPressedKey_off = """
tmp.control_subTerm.Key = "none"
"""
    getPressedKey_on = """
tmp.control_subTerm.Key = getPressedKey()
"""
    red = """
try:
    red = tmp.red
except AttributeError:
    pass
print(red)
"""
def prefix4inlines(inlineCmd: str, prefixes: dict) -> str:
    for k, v in prefixes.items():
        inlineCmd = inlineCmd.replace(k, f"{v}.{k}")
    return inlineCmd
def constBytes2read() -> int:
    return 8192
def subTerminal(cmdInput: str) -> dict:
    rows, cols = os.popen("stty size", 'r').read().split()
    print(f"cols, rows = {cols}, {rows}")
    main, second = os.openpty()
    _, err = os.openpty()
    stop = str(ctlCodes.stop0) * 10
    cmd = [f"stty cols {cols};stty rows {rows};{cmdInput};echo {stop}", ]
    proc = sp.Popen(cmd, stderr=err, stdout=second, stdin=second, shell=True)
    #~red = codecs.decode(os.read(main, 4096))
    #print(red)
    return {"err": err, "out": second, "in": second, "main": main}
def Prime_subTerminal(cmdInput: str, std_in_out = [int, int]) -> dict:
    funcName = "Prime_subTerminal"
    #return {"err": 0, "in": 0, "main": 0, "status": None}
    rows, cols = os.popen("stty size", 'r').read().split()
    print(f"cols, rows = {cols}, {rows}")
    second, main = os.pipe2(os.O_NONBLOCK)
    main0, second0 = os.openpty() 
    Main = main
    display_out, in_display = os.pipe2(os.O_NONBLOCK) 
    in_display, display_out = os.openpty() 
    if modes.prime_stdin: std_in_out[0] = sys.stdin.fileno()
    if modes.stderr2stdin: std_in_out[0] = sys.stderr.fileno()
    if not modes.prime_stdin and not modes.stderr2stdin: std_in_out[0] = second
    yes_to_log = tam.checkArg("-do-logs")|tam.checkArg("-do-bin-logs")|tam.checkArg("-do-txt-logs")
    if yes_to_log: 
        std_in_out[1] = in_display
        std_in_out[0] = second
        tmp.write_logs.input_fd = main
        tmp.write_logs.display_out = display_out
    if modes.mc.active and not yes_to_log:
        std_in_out[0] = second0
        Main = main0
    _, err = os.openpty()
    stop = str(ctlCodes.stop0) * int(cols)
    if ctlCodes.locale is not None:
        cmdInput = f"LC_ALL={ctlCodes.locale} {cmdInput}"
    cmd = [f"stty cols {cols};stty rows {rows};{cmdInput};echo '{stop}\nPress Enter, if command line ain`t seen';sleep .2;exit {ctlCodes.Prime_subTerminal.ExitCode}", ]
    tam.errMsg_dbg(cmd, funcName)
    proc = sp.Popen(cmd, stderr=err, stdout=std_in_out[1], stdin=std_in_out[0], shell=True, close_fds=True)
    """while True:
        try:
            tam.achtung(codecs.decode(os.read(display_out, 1024)))
            break
        except BlockingIOError: pass"""
    return {"err": err, "in": std_in_out[0], "main": Main, "status": proc}
def checkANDwipeStopCode(red: str) -> int:
    if red == "" or red == r'':
        return ctlCodes.checkANDwipeStopCode.empty
    check = re.compile(ctlCodes.stop0)
    res = check.findall(red)
    tam.achtung(f"{str(res) =}\n{red}")
    if res:
        tmp.red = red.replace(ctlCodes.stop, '')
        return ctlCodes.checkANDwipeStopCode.hOKkey
    else:
        tmp.red = red
        return ctlCodes.checkANDwipeStopCode.noCode
def no_back_slash(str0: str) -> str:
    return str0.replace('\\', '')
def readOutput(out) -> int:
    #out = open("hh")
    red = os.read(out, constBytes2read())
    tam.achtung(f"{red=}")
    try:
        red = codecs.decode(red)
    except TypeError:
        pass
    if checkANDwipeStopCode(red) == ctlCodes.checkANDwipeStopCode.empty:
        tam.achtung("empty")
        return ctlCodes.readOutput.paused
    if checkANDwipeStopCode(red) == ctlCodes.checkANDwipeStopCode.hOKkey:
        tam.achtung("hOKkey")
        exec(inlines.red)
        return ctlCodes.readOutput.stopped
    exec(inlines.red)
def getPressedKey() -> str:
    funcName = "getPressedKey"
    if tam.checkArg("-dbg"): tam.achtung(funcName)
    exec(tam.keyCodes())
    Key = ""
    try: Key = codecs.decode(os.read(sys.stdin.fileno(), 32))#click.getchar()
    except IOError: pass
    ord0: int|None = None
    try:
        ord0 = ord(Key)
    except: pass
    #time.sleep(.002)
    #tam.achtung(f"{str(Key)=}, {no_back_slash(tam.kCodes.Alt_0)=}")

    if tam.kCodes.Alt_0 == repr(Key) or Key == no_back_slash(tam.kCodes.Alt_0):
        exec(inlines.reset_modes)
        return ctlCodes.Prime_subTerminal.ExitCode
    if tam.kCodes.INSERT == Key or no_back_slash(tam.kCodes.INSERT) == Key:
        tam.achtung("ins")
    return Key
def isProcRunning(proc: sp.Popen):
    funcName = "isProcRunning"
    tam.achtung(funcName)
    res: int = 0
    new_cycle: bool = True
    res = ""
    try:
        res = proc.wait(.004)
        tam.achtung(str(res))
    except sp.TimeoutExpired: pass
    except AttributeError: return False
    except KeyError: return False
        #time.sleep(20)
        #tam.errMsg_dbg(f"{res=}", funcName) 
    if res == ctlCodes.Prime_subTerminal.ExitCode: 
        reset_main_term()
        return False #and not ctlCodes.write_log.running: return True
    return True
def reset_main_term() -> None:
    if tam.checkArg("-dirty"): return
    os.system("reset")
def activate_mc_mode():
    modes.mc.active = True
    modes.prime_stdin = True
def control_subTerm(cmd: str, std_in_out = [int, int]) -> None:
    Key = None
    if cmd == "":
        cmd = "echo Enter Your command, Please"
    if cmd[:2] == "mc": 
            modes.mc.active = True
            modes.prime_stdin = True
    else: modes.mc.active = False
    if cmd[:3] == "vi " or cmd[:4] == "vim ": 
        modes.stderr2stdin = True
    exec(inlines.write_logs)
    """"""
    #if tam.checkArg("-do-logs") or tam.checkArg("-do-bin-logs") or tam.checkArg("-do-txt-logs"): write_logs()
    tam.achtung(inlines.write_logs)
    dict_f: dict = {}
    if cmd != "":
        dict_f = Prime_subTerminal(cmd, std_in_out)
    tmp.dict_f = dict_f
    res: int = 0
    new_cycle: bool = True
    while True:
        res = ""
        try:
           res = dict_f["status"].wait(.004)
           #tam.achtung(str(res))
        except sp.TimeoutExpired: pass
        except AttributeError: pass
        except KeyError: pass
        #tam.achtung(res) - good example of undefined output
        if res == ctlCodes.Prime_subTerminal.ExitCode and not ctlCodes.write_log.running:
            new_cycle = True
            pid = dict_f["status"].pid
            dict_f["status"].terminate()
            try: os.kill(pid, signal.SIGKILL)
            except ProcessLookupError: pass
            #~print(f'{open(dict_f["err"]).read()}')
            #os.system("clear")
            sys.stdin.flush() 
            exec(inlines.reset_modes)
            env.cur_cmd = cmd = ""
            env.cur_cmd = cmd = input("Please, enter Your command: ")
            cmd_log()
            exec(inlines.write_logs)
            #if tam.checkArg("-do-logs") or tam.checkArg("-do-bin-logs") or tam.checkArg("-do-txt-logs"): write_logs()
            if tam.checkArg("-dbg"): tam.achtung(f"{cmd=}")
            if cmd[:2] == "mc": 
                modes.mc.active = True
                tmp.dict_f = dict_f
            else: modes.mc.active = False
            if cmd[:3] == "vi " or cmd[:4] == "vim ": 
                modes.stderr2stdin = True
            if cmd == "qqq0":
                break
            if cmd != "":
                dict_f = Prime_subTerminal(cmd, std_in_out)
            cmd = ""
        if not modes.mc.active and not modes.prime_stdin and not modes.stderr2stdin:
            if new_cycle and tam.checkArg("-dbg"):
                tam.achtung(f"getPressedKey_on, {dict_f}")
                tam.achtung(f"{modes.mc.active=} {modes.prime_stdin=} {modes.stderr2stdin}")
            new_cycle = False
            inlines.getPressedKey = inlines.getPressedKey_on
        else: inlines.getPressedKey = inlines.getPressedKey_off
        if cmd[:4] == "vim ": inlines.getPressedKey = inlines.getPressedKey_off
        exec(inlines.getPressedKey)
        if inlines.getPressedKey == inlines.getPressedKey_on:
            Key = tmp.control_subTerm.Key
            del tmp.control_subTerm.Key
        if Key == ctlCodes.Prime_subTerminal.ExitCode:
            res = ctlCodes.Prime_subTerminal.ExitCode
            continue
        else:
            if res == ctlCodes.Prime_subTerminal.ExitCode: continue
            if Key != "none" and not modes.mc.active and not modes.prime_stdin and not modes.stderr2stdin:
                #os.write(dict_f["main"], codecs.encode(str(Key), "utf-8"))
                os.write(dict_f["main"], codecs.encode(str(Key), "utf-8"))
           # print(Key)
        #os.write(dict_f["in_"], codecs.ascii_encode(Key))
    return
def term_app(cmd: str, std_in_out = [int, int]) -> sp.Popen:
    funcName = "term_app"
    Key = None
    if cmd == "":
        cmd = "echo Enter Your command, Please"
    #tam.achtung(cmd)
    tam.errMsg(cmd, funcName)
    if cmd[:2] == "mc": 
            modes.mc.active = True
            modes.prime_stdin = True
    else: modes.mc.active = False
    if cmd[:3] == "vi " or cmd[:4] == "vim ": 
        modes.stderr2stdin = True
    exec(inlines.write_logs)
    """"""
    #if tam.checkArg("-do-logs") or tam.checkArg("-do-bin-logs") or tam.checkArg("-do-txt-logs"): write_logs()
    tam.achtung(inlines.write_logs)
    dict_f: dict = Prime_subTerminal(cmd, std_in_out)
    tmp.term_app.dict_f = dict_f
    return dict_f["status"]
def cmd_log():
    funcName = "cmd_log"
    try:
        fd = open(env.cmd_story, "+a")
    except OSError:
        tam.errMsg(f"failed to write in {env.cmd_story}", funcName, 2)
        return
    try:
        fd_bkp = open(f"{env.cmd_story}.bkp", "+w")
    except OSError:
        tam.errMsg(f"failed to write in {env.cmd_story}.bkp", funcName, 2)
        return
    content: str = ""
    cont2list: list = []
    fd.seek(0)
    content = fd.read()
    fd_bkp.write(content)
    cont2list = content.splitlines()
    print(f"{cont2list=}, {content=}")
    cont2list.append(f"{env.cur_cmd}")
    cont2list = list(set(cont2list))
    content = "".join(f"{line}\n" for line in cont2list)
    fd.seek(0)
    fd.truncate(0)
    fd.write(f"{content}")
    fd.close()
    fd_bkp.close()
def write_log():
    funcName = "write_log"
    if ctlCodes.write_log.running: return
    else: ctlCodes.write_log.running = True
    buff_size = 10024
    ID = ctlCodes.write_log.count
    ctlCodes.write_log.count += 1
    if env.fds.tamish_logs is None:
        tam.errMsg(f"{env.fds.tamish_logs=}", funcName)
        sys.exit(-1)
    content = "none"
    """proc = sp.Popen(["tty"], shell=True, stderr=sp.PIPE, stdout=sp.PIPE)
    pts, _ = proc.communicate()
    pts = pts[:-1]
    fd = os.open(pts, os.O_NONBLOCK|os.O_RDWR)
    fd = open(fd)"""
    #os.write(fd.fileno(), b'pwd\n')
    inlines.getPressedKey = inlines.getPressedKey_off
    check_stop_code = re.compile(ctlCodes.stop0)
    while True:
        try:
            output_fd = tmp.write_logs.display_out
            break
        except AttributeError:
            tam.errMsg("no display out", funcName, .1)
    fd = None
    try:
        try:
            fd = open(env.fds.tamish_logs, "ab+")
        except OSError:
            fd = open(env.tamish_log.name, "ab+")
    except OSError:
        inlines.getPressedKey = inlines.getPressedKey_on
        if tam.checkArg("-dbg"): print(f"{env.fds.tamish_logs=} oserr.no ={OSError.errno}")
        tam.errMsg("Press Enter, if command line ain`t seen", funcName, 2)
        ctlCodes.write_log.failed += 1
        return
    while True:
        if env.cur_cmd != "":
            cur_cmd = f">>> {env.cur_cmd}\n"
            fd.write(codecs.encode(cur_cmd, "utf-8"))
            break
    while True:
        """"""
        while True:
            try:
                #tam.achtung(output_fd)
                content = os.read(output_fd, buff_size)
                break
            except BlockingIOError: pass
            except OSError: tam.errMsg("no channel/pty to read", funcName, 2)
        os.write(sys.stdout.fileno(), content)
        try: 
            assert content == ""
        except AssertionError: tam.achtung("")#str(content))
        fd.write(content) #codecs.encode(content, "utf-8"))
        check_stop_code0 = None
        while True:
            try:
                check_stop_code0 = check_stop_code.findall(content.decode())
                break
            except UnicodeDecodeError:
                tam.achtung(content)
                content = content[:-1]
        #tam.achtung(f"{check_stop_code0=}")
        if check_stop_code0 != []: # or not ctlCodes.write_log.running:
            inlines.getPressedKey = inlines.getPressedKey_on
            tam.achtung(f"exit {funcName} {ID}")
            break
        content = ""
    content = os.read(output_fd, buff_size)
    os.write(sys.stdout.fileno(), content)
    os.close(output_fd)
    ctlCodes.write_log.running = False
    del tmp.write_logs.display_out
    fd.close()
        #time.sleep(.04)
def write_logs():
    if tam.checkArg("-do-logs") or tam.checkArg("-do-bin-logs") or tam.checkArg("-do-txt-logs"): pass
    else: return
    log_output: Thread = Thread(target=write_log, args=())
    log_output.start()
def init_user_logs():
    if tam.checkArg("-lc"): ctlCodes.locale = tam.get_arg_in_cmd("-lc")
    if tam.checkArg("-off-getpressedkey"): 
        inlines.getPressedKey_on = inlines.getPressedKey_off
        inlines.getPressedKey = inlines.getPressedKey_off
    if tam.checkArg("-do-logs") or tam.checkArg("-do-bin-logs") or tam.checkArg("-do-txt-logs"): inlines.write_logs = inlines.write_logs_on
    else: inlines.write_logs = inlines.off
    env.USER_HOME_DIR = os.environ['HOME']
    tam_main_path_4logs: str = f"{env.USER_HOME_DIR}/.TAM_MY_LOGS"
    if not os.path.exists(tam_main_path_4logs): os.system(f"mkdir {tam_main_path_4logs}")
    date_msk = "%Y-%m-%d__%H-%M-%S"
    nowtime = datetime.strftime(datetime.now(), date_msk) + "." + str(datetime.now().microsecond)
    env.tamish_log.name = f"{tam_main_path_4logs}/shell{nowtime}.log"
    env.fds.tamish_logs = os.open(env.tamish_log.name, os.O_CREAT|os.O_WRONLY)
    if env.fds.tamish_logs is None:
        print(f"{env.fds.tamish_logs=}")
        sys.exit(-1)
    env.fds.tamish_cmds = os.open(f"{tam_main_path_4logs}/cmds.story", os.O_APPEND|os.O_CREAT)
    if env.fds.tamish_cmds is None:
        print(f"{env.fds.tamish_cmds=}")
        sys.exit(-1)
    env.cmd_story = f"{tam_main_path_4logs}/cmds.story"
    #time.sleep(1000_000)
def read_log(path: str):
    content = "none"
    fd = os.open(path, os.O_RDONLY)
    readBytes = 1024 ** 2
    while content != "":
        content = os.read(fd, readBytes)
        os.write(sys.stdout.fileno(), content)
def main() -> None:
    std_in_out = [sys.stdin.fileno(), sys.stdout.fileno()]
    env.cur_cmd = cmd = input("Please, enter Your cmd: ")
    cmd_log()
    control_subTerm(cmd, std_in_out)
if __name__ == "__main__":
    if tam.checkArg("-get-log"):
        read_log(tam.get_arg_in_cmd("-get-log", sys.argv))
        sys.exit(0)
    from threading import Thread
    """init_logs: Thread = Thread(target=init_user_logs, args=())
    init_logs.start()"""
    init_user_logs()
    main()