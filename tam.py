import random
import re
import io
from tabulate import tabulate
import sys, os, signal
import click
#import pysdl2
import keyboard as kbd
import time
from threading import Thread
import fcntl
import codecs
import numpy as np
import subprocess as sp, copy, threading as thr
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from colorama import Back
try:
    from sark0y_tam import _tam as tam0
except ModuleNotFoundError:
    try:
        import tam as tam0
    except ModuleNotFoundError:
        print("TAM can't do 1st loading")
        sys.exit()
try:
    import subTern as subtern
except ModuleNotFoundError: pass #errMsg("subTern module not found", "TAM")
""""""
try:
    if __name__ == "__main__":
       if tam0.checkArg("-no-pkg"): raise ModuleNotFoundError
    from sark0y_tam import _subTern as subtern
except ModuleNotFoundError: pass
except ImportError: pass
""""""
#MAIN
class info_struct:
    ver = 1
    rev = "9-115"
    author = "Evgeney Knyazhev (SarK0Y)"
    year = '2023'
    telega = "https://t.me/+N_TdOq7Ui2ZiOTM6"
stopCode = "∇\n"
class tmp:
    none = None
class inlines:
    switch_make_page = """
tmp.table, tmp.too_short_row = make_page_of_files2(globalLists.fileListMain, ps)
"""
    make_page_of_files2 = """
tmp.table, tmp.too_short_row = make_page_of_files2(globalLists.fileListMain, ps)
"""
    make_page_of_files2_li = """
tmp.table, tmp.too_short_row = make_page_of_files2_li(globalLists.fileListMain, ps)
"""
    switch_run_viewer = """
run_viewers(ps.c2r, fileListMain, cmd)
"""
    run_viewer = """
run_viewers(ps.c2r, fileListMain, cmd)
"""
    run_viewer_li = """
run_viewers_li(ps, fileListMain, cmd)
"""
    me_stop_mode1_on = """
modes.path_autocomplete.state = modes.path_autocomplete.fst_hit = False
"""
    me_stop_mode1 = """
if checkArg("-me-stop-autocompletion"):
    sys.argv.append("-me-stop-mode1")
if not checkArg("-me-stop-mode1"):
    inlines.me_stop_mode1 = inlines.me_stop_mode1_on
else:
    inlines.me_stop_mode1 = "once.nop()"
exec(inlines.me_stop_mode1)
"""
    updateDirList = """
if modes.path_autocomplete.state:
    globalLists.ls = createDirList(partial.path, "-maxdepth 1")
if globalLists.ls != []:
    globalLists.fileListMain = globalLists.ls
    modes.path_autocomplete.page_struct = ps
    return "go2 0"
else:
    return "cont"
"""
class __manage_pages:
    none = None
class modes:
    class file_ops:
        justYes2KillFile: bool = False
        killFile: bool = False
        copyFile: bool = False
    class sieve:
        state: bool = False
    class switch_2_nxt_tam:
        state: bool = False
    class page_indices:
        global_or_not: bool = True
    class mark_the_viewer:
        EXTRN = 0
        TERM  = 1
    class path_autocomplete:
        state = False
        fst_hit = False
        page_struct = None
        letsStop: str = ""
class partial:
    path: str = ""
class globalLists:
    class tam_instances:
        name: list = []
        wid: list = []
    stopCode = globals()["stopCode"]
    fileListMain: list = []
    ls:  list = []
    bkp: list = []
    fileListMain0: list = []
    filtered: list = []
    merge: list = []
    ret = ""
class childs2run:
    running: list = []
    viewer: list = []
    mode2run: list = []
    prnt: str = ""
    full_path = ""
class page_struct:
    left_shift_4_cur = 0
    cur_cur_pos = 0 # cursor's current position
    KonsoleTitle: str
    dontDelFromTableJustMark = True
    num_page: int = 0
    num_cols: int = 3
    col_width = 70
    num_rows: int = 11
    num_spaces: int = 4
    num_files = 0
    count_pages = 0
    news_bar = f"{info_struct.telega} 2 know news & features ;D"
    question_to_User: str = ""
    c2r: childs2run
class ps0:
    init: bool = False
    ps: page_struct
    sieve: page_struct
    def __init__(self) -> None:
        ps0.ps = page_struct()
        ps0.ps.num_cols = 1
        ps0.ps.num_rows = 7
        ps0.ps.col_width = 200
        ps0.init = True
class keys:
    dirty_mode: bool = False
    rename_file_mode: int = 0
    term_app: bool = False
    вар = "дело пошло.. таки :) 147"

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
class var_4_hotKeys:
    prnt: str = ""
    prompt: str = "Please, enter Your command: "
    save_prompt_to_copy_file: str = ""
    save_prnt_to_copy_file: str = ""
    prnt_short: str = ""
    prnt_full: str = ""
    prnt_step_back: str = ""
    copyfile_msg: str = ""
    fileName: str = ""
    fileIndx: int
    full_length: int
    ENTER_MODE = False
    only_1_slash = ""
# Terminals
class Markers:
    console_title: str = "∇∞∇"
    console_title_pefix: str = ""
class kCodes:
    Key = None
def keyCodes():
    keyCodes0 = """
kCodes.ENTER = 13
kCodes.BACKSPACE = 127
kCodes.ESCAPE = 27
kCodes.TAB = 9
kCodes.DELETE = "\x1b[3~"
kCodes.F12 = "\x1b[24~"
kCodes.F5 = "\x1b[15~"
kCodes.F1 = "\x1bOP"
kCodes.INSERT = "\x1b[2~"
kCodes.PgUP = "\x1b[5~"
kCodes.LEFT_ARROW = "\x1b[D"
kCodes.RIGHT_ARROW = "\x1b[C"
kCodes.UP_ARROW = "\x1b[A"
kCodes.DOWN_ARROW = "\x1b[B"
kCodes.Alt_0 = "\x1b0"
kCodes.Alt_2 = "\x1b2"
    """
    keyCodes_extrn = """
try:
    import tam
except ModuleNotFoundError:
    pass
try:
    from sark0y_tam import _tam as tam
except ModuleNotFoundError:
    pass
tam.kCodes.ENTER = 13
tam.kCodes.BACKSPACE = 127
tam.kCodes.ESCAPE = 27
tam.kCodes.TAB = 9
tam.kCodes.DELETE = "\x1b[3~"
tam.kCodes.F12 = "\x1b[24~"
tam.kCodes.F5 = "\x1b[15~"
tam.kCodes.F1 = "\x1bOP"
tam.kCodes.INSERT = "\x1b[2~"
tam.kCodes.LEFT_ARROW = "\x1b[D"
tam.kCodes.RIGHT_ARROW = "\x1b[C"
tam.kCodes.UP_ARROW = "\x1b[A"
tam.kCodes.DOWN_ARROW = "\x1b[B"
tam.kCodes.Alt_0 = "\x1b0"
tam.kCodes.Alt_2 = "\x1b2"
    """
    if __name__ != "__main__": return keyCodes_extrn
    return keyCodes0
def get_proper_indx_4_page(indx: int) -> int|None:
    indx = int(indx)
    if not checkInt(indx): return None
    if indx < 0: return page_struct.num_files + indx
    if modes.page_indices.global_or_not: return indx
    indx += page_struct.num_cols * page_struct.num_rows * page_struct.num_page
    achtung(f"{indx=} {page_struct.num_page=}")
    achtung(f"{page_struct.num_cols=}")
    achtung(f"{page_struct.num_rows=}")
    return indx
def uvdir() -> str:
    funcName = "uvdir"
    path_2_vdir = var_4_hotKeys.prnt[5:]
    while True:
        if path_2_vdir[0] == " ": path_2_vdir = path_2_vdir[1:]
        else: break
    path_2_vdir = path_2_vdir.replace("//", "/")
    if path_2_vdir[-1] != "/": path_2_vdir += "/"
    dir_content: list = createDirList0(path_2_vdir, "-type l", no_grep=True)
    errMsg_dbg(f"{dir_content}", funcName)
    for p in dir_content:
        p = escapeSymbols(p)
        errMsg_dbg(f"{p=}", funcName)
        cmd = f"unlink {p}"
        os.system(cmd)

def vdir() -> str:
    funcName = "vdir"
    path_2_vdir: str = var_4_hotKeys.prnt[4:]
    while True:
        if path_2_vdir[0] == " ": path_2_vdir = path_2_vdir[1:]
        else: break
    path_2_vdir = path_2_vdir.replace("//", "/")
    if path_2_vdir[-1] == "/": path_2_vdir = path_2_vdir[:-1]
    mkdir: str = escapeSymbols(path_2_vdir)
    os.system(f"mkdir -p {mkdir}")
    try:
        ret: list = createDirList0(f"{path_2_vdir}", "-type d")
    except IndexError: pass
    errMsg_dbg(f"{path_2_vdir=}{ret=}", funcName)
    if ret == []:
        errMsg(f"{path_2_vdir} ain't existed", funcName, 1.15)
        return
    path_2_vdir = mkdir
    for p in globalLists.filtered:
        fn: str = os.path.basename(p)
        fn = escapeSymbols(fn)
        p = escapeSymbols(p)
        errMsg_dbg(f"{p=}{fn}", funcName)
        cmd = f"ln -sf {p} {path_2_vdir}/{fn}"
        os.system(cmd)
    return path_2_vdir
def setTermAppStatus(proc: sp.Popen) -> bool:
    funcName: str = "setTermAppStatus"
    errMsg_dbg("running", funcName)
    while keys.term_app:
        os.environ["tamKeysTerm_app"] = str(keys.term_app)
        os.system(f"export tamKeysTerm_app={str(keys.term_app)}")
        keys.term_app = subtern.isProcRunning(proc)
    try:
        funcStatus: str = os.environ["setTermAppStatus_exited"]
    except KeyError:
        funcStatus = 0
    os.system(f"export setTermAppStatus_exited={int(funcStatus) + 1}")
def sieve_list(lst: list, rgx: str) -> list:
    sieve = re.compile(rgx, re.UNICODE|re.IGNORECASE)
    ret_lst: list = []
    for item in lst:
        if sieve.findall(item):
            ret_lst.append(item)
    return ret_lst
def proxy_io():
    funcName:  str = "proxy_io"
    inlineCmd: str = "pass"
    modes = subtern.modes
    dict_f = subtern.tmp.term_app.dict_f
    while keys.term_app:
        if not modes.mc.active and not modes.prime_stdin and not modes.stderr2stdin:
            Key = hotKeys("")
            #os.write(dict_f["main"], codecs.encode(str(Key), "utf-8"))
            os.write(dict_f["main"], codecs.encode(str(Key), "utf-8"))
    inlineCmd = subtern.prefix4inlines(subtern.inlines.reset_modes, {"ctlCodes": "subtern", "modes.": "subtern", "inlines": "subtern"})
    achtung(f"{inlineCmd}")
    errMsg_dbg(inlineCmd, funcName)
    exec(inlineCmd)
        #achtung(f"{keys.term_app=}")
def setTermAppStatus_Thr(proc: sp.Popen) -> None:
    thr: Thread = Thread(target=setTermAppStatus, args=(proc,))
    thr.start()
    thr1: Thread = Thread(target=proxy_io)
    thr1.start()
def handleENTER(fileName: str) -> str:
    funcName = "handleENTER"
    exec(inlines.me_stop_mode1)
    var_4_hotKeys.ENTER_MODE = True
    if var_4_hotKeys.prnt[:3] == 'ren':
        var_4_hotKeys.save_prnt_to_copy_file = var_4_hotKeys.prnt
        var_4_hotKeys.save_prompt_to_copy_file = var_4_hotKeys.prompt
        try:
            renameFile(fileName, var_4_hotKeys.prnt)
        except AttributeError or ValueError:
            errMsg("Command was typed wrong", funcName, 2)
            return "cont"
        var_4_hotKeys.prnt = var_4_hotKeys.save_prnt_to_copy_file
        var_4_hotKeys.prompt = var_4_hotKeys.save_prompt_to_copy_file
        var_4_hotKeys.ENTER_MODE = False
        return f"go2 {page_struct.num_page}"
    if var_4_hotKeys.prnt[:2] == "cp":
        modes.file_ops.copyFile = True
        IsFile = None #todo..
        try:
            file = getFileNameFromCMD(var_4_hotKeys.prnt)
            IsFile = os.path.exists(file) and os.path.isfile(file)
        except AttributeError or ValueError:
            errMsg("Command was typed wrong", funcName, 2)
            return "cont"
        if IsFile:
            var_4_hotKeys.copyfile_msg = f"Do You really want to overwrite {getFileNameFromCMD(var_4_hotKeys.prnt)} ??? Type 'Yeah I do' if You {Fore.RED}{Back.BLACK}REALLY{Style.RESET_ALL} do.. Otherwise just 'no'. "
            if var_4_hotKeys.save_prnt_to_copy_file == '':
                var_4_hotKeys.save_prnt_to_copy_file = var_4_hotKeys.prnt
                var_4_hotKeys.prnt = ""
                var_4_hotKeys.save_prompt_to_copy_file = var_4_hotKeys.prompt
                page_struct.question_to_User = var_4_hotKeys.copyfile_msg
                full_length = len(var_4_hotKeys.prompt) + len(var_4_hotKeys.prnt)
                page_struct.left_shift_4_cur = 0
                page_struct.cur_cur_pos = full_length
                clear_cmd_line(var_4_hotKeys.prompt, var_4_hotKeys.prnt, full_length)
                print(f"{page_struct.question_to_User}")
                writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt, full_length)
                return "cont"
        else:
            copyFile(fileName, var_4_hotKeys.prnt)
            var_4_hotKeys.prnt = var_4_hotKeys.save_prnt_to_copy_file
            var_4_hotKeys.prompt = var_4_hotKeys.save_prompt_to_copy_file
            var_4_hotKeys.ENTER_MODE = False
            return f"go2 {page_struct.num_page}"
    if var_4_hotKeys.prnt[:2] == "rm":
        modes.file_ops.killFile = True
        try:
            var_4_hotKeys.copyfile_msg = f"Do You really want to delete {getFileNameFromCMD_byIndx(var_4_hotKeys.prnt)} ??? Type 'Yeah, kill this file' if You {Fore.RED}{Back.BLACK}REALLY{Style.RESET_ALL} do.. Otherwise just 'no'. "
        except AttributeError or ValueError or IndexError:
            errMsg("Command was typed wrong", funcName, 2)
            return "cont"
        if var_4_hotKeys.save_prnt_to_copy_file == '':
            var_4_hotKeys.save_prnt_to_copy_file = var_4_hotKeys.prnt
            var_4_hotKeys.prnt = ""
            var_4_hotKeys.save_prompt_to_copy_file = var_4_hotKeys.prompt
            page_struct.question_to_User = var_4_hotKeys.copyfile_msg
            full_length = len(var_4_hotKeys.prompt) + len(var_4_hotKeys.prnt)
            page_struct.left_shift_4_cur = 0
            page_struct.cur_cur_pos = full_length
            clear_cmd_line(var_4_hotKeys.prompt, var_4_hotKeys.prnt, full_length)
            print(f"{page_struct.question_to_User}")
            writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt, full_length)
            return "cont"
    if var_4_hotKeys.prnt == "Yeah I do" or (modes.file_ops.copyFile and modes.file_ops.justYes2KillFile and (var_4_hotKeys.prnt.lower() == "y" or \
                                                                                                                         var_4_hotKeys.prnt == "yes")):
        var_4_hotKeys.prompt = ' ' * len(var_4_hotKeys.prompt)
        var_4_hotKeys.prnt = ' ' * len(var_4_hotKeys.prnt)
        writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt)
        var_4_hotKeys.prnt = var_4_hotKeys.save_prnt_to_copy_file
        var_4_hotKeys.prompt = var_4_hotKeys.save_prompt_to_copy_file
        var_4_hotKeys.save_prompt_to_copy_file = var_4_hotKeys.save_prnt_to_copy_file = ''
        fileName = copyFile(fileName, var_4_hotKeys.prnt, dontInsert=True)
        writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt)
        modes.file_ops.copyFile = var_4_hotKeys.ENTER_MODE = False
        page_struct.question_to_User = f"{fileName}"
        return f"go2 {page_struct.num_page}"
    if var_4_hotKeys.prnt == "Yeah, kill this file" or (modes.file_ops.killFile and modes.file_ops.justYes2KillFile and (var_4_hotKeys.prnt.lower() == "y" or \
                                                                                                                                    var_4_hotKeys.prnt == "yes")):
        var_4_hotKeys.prompt = ' ' * len(var_4_hotKeys.prompt)
        var_4_hotKeys.prnt = ' ' * len(var_4_hotKeys.prnt)
        writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt)
        var_4_hotKeys.prnt = var_4_hotKeys.save_prnt_to_copy_file
        var_4_hotKeys.prompt = var_4_hotKeys.save_prompt_to_copy_file
        var_4_hotKeys.save_prompt_to_copy_file = var_4_hotKeys.save_prnt_to_copy_file = ''
        fileName = delFile(fileName, var_4_hotKeys.prnt, dontDelFromTableJustMark=page_struct.dontDelFromTableJustMark)
        page_struct.question_to_User = f"{fileName}"
        writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt)
        modes.file_ops.killFile = var_4_hotKeys.ENTER_MODE = False 
        return f"go2 {page_struct.num_page}"
    if var_4_hotKeys.prnt == "no":
        var_4_hotKeys.prnt = var_4_hotKeys.save_prnt_to_copy_file
        var_4_hotKeys.prompt = var_4_hotKeys.save_prompt_to_copy_file
        var_4_hotKeys.save_prompt_to_copy_file = ''
        var_4_hotKeys.save_prnt_to_copy_file = ''
        writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt)
        modes.file_ops.copyFile = modes.file_ops.killFile = var_4_hotKeys.ENTER_MODE = False
        return f"go2 {page_struct.num_page}"
    if modes.sieve.state: globalLists.fileListMain = globalLists.filtered
    return var_4_hotKeys.prnt
def handleTAB(prompt: str):
    funcName = "handleTAB"
    if modes.sieve.state: globalLists.fileListMain = globalLists.filtered
    ptrn = re.compile('ren\s+\-?\d+|cp\s+\-?\d+', re.IGNORECASE | re.UNICODE)
    regex_result = ptrn.search(var_4_hotKeys.prnt)
    if keys.dirty_mode: print(f"{regex_result.group(0)}, {len(regex_result.group(0))}, {var_4_hotKeys.prnt}")
    if regex_result:
        if len(var_4_hotKeys.prnt_short) == 0:
            var_4_hotKeys.fileName, var_4_hotKeys.fileIndx = regex_result.group(0).split()
            var_4_hotKeys.fileName = globalLists.fileListMain[get_proper_indx_4_page(int(var_4_hotKeys.fileIndx))]
            if var_4_hotKeys.fileName[-1] == '\n':
                var_4_hotKeys.fileName = var_4_hotKeys.fileName[:-1]
            _, var_4_hotKeys.prnt_short = os.path.split(var_4_hotKeys.fileName)
            var_4_hotKeys.prnt_short = var_4_hotKeys.prnt + f" {var_4_hotKeys.prnt_short}"
            var_4_hotKeys.prnt_full = var_4_hotKeys.prnt + f" {var_4_hotKeys.fileName}"
        if len(var_4_hotKeys.prnt) < len(var_4_hotKeys.prnt_full):
            var_4_hotKeys.prnt = var_4_hotKeys.prnt_full
            page_struct.cur_cur_pos = len(var_4_hotKeys.prnt_full)
            page_struct.left_shift_4_cur = 0
        else:
            page_struct.left_shift_4_cur = 0
            var_4_hotKeys.prnt = var_4_hotKeys.prnt_short
            page_struct.cur_cur_pos = len(var_4_hotKeys.prnt_short)
        errMsg_dbg(f"{var_4_hotKeys.prnt_full=}\n{var_4_hotKeys.prnt_short=}", funcName, 2)
        var_4_hotKeys.full_length = len(var_4_hotKeys.prnt)
        writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt, len(var_4_hotKeys.prnt_full))
class once:
    def once_copy() -> None:
       globalLists.fileListMain0 = copy.copy(globalLists.fileListMain)
    def nop(): pass
def list_autocomplete_pages(Key: str): 
    if not modes.path_autocomplete.state:
        return
    modes.path_autocomplete.page_struct.count_pages = len(globalLists.ls) // (modes.path_autocomplete.page_struct.num_cols * modes.path_autocomplete.page_struct.num_rows)
    if Key == kCodes.UP_ARROW:
        if modes.path_autocomplete.page_struct.count_pages > modes.path_autocomplete.page_struct.num_page:
            modes.path_autocomplete.page_struct.num_page += 1 
    if Key == kCodes.DOWN_ARROW:
        if modes.path_autocomplete.page_struct.num_page > 0:
            modes.path_autocomplete.page_struct.num_page -= 1 
def make_page_struct():
       ps = page_struct()
       argv = sys.argv
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
          ps.num_page = 0
       modes.path_autocomplete.page_struct = ps
def updateDirList():
    errMsg_dbg(f"{modes.path_autocomplete.letsStop=} {modes.path_autocomplete.state}", "updateDirList")
    if modes.path_autocomplete.state:
        errMsg_dbg("", "updateDirList")
        globalLists.ls = createDirList(partial.path, "-maxdepth 1")
    if globalLists.ls != []:
          globalLists.fileListMain = globalLists.ls
          return "go2 0"
    else:
        return "cont"
def swtch_2_nxt_tam() -> None:
    funcName = "swtch_2_nxt_tam"
    try:
        indx = int(var_4_hotKeys.prnt)
    except ValueError:
        errMsg("indx must be an integer.", funcName, 2)
        return
    run_cmd(f"wmctrl", f"-i -a {globalLists.tam_instances.wid[indx]}")
def find_all_tam_consoles() -> None:
    globalLists.tam_instances.wid = []
    globalLists.tam_instances.name = []
    find = re.compile(Markers.console_title)
    find_wid = re.compile('0x[abcdef0-9]+')
    list_all_wndws: list = codecs.decode(run_cmd("wmctrl", "-l")[0]).splitlines()
    for window in list_all_wndws:
          if find.findall(window):
            wid = find_wid.match(window).group(0)
            globalLists.tam_instances.wid.append(wid)
            _, window = str(window).split(Markers.console_title)
            window = Markers.console_title + window
            globalLists.tam_instances.name.append(f"{window}")
def switch_global_list(Key: str):
    funcName = "switch_global_list"
    ps = page_struct()
    if Key == kCodes.UP_ARROW or Key == kCodes.DOWN_ARROW or Key == kCodes.LEFT_ARROW or Key == kCodes.RIGHT_ARROW or Key == kCodes.F12 \
    or Key == kCodes.TAB or Key == kCodes.ESCAPE:
        kCodes.Key = Key
        return "cont"
    if kCodes.BACKSPACE == ord0(Key):
        partial.path = partial.path[:-1]
        return updateDirList()
    if modes.path_autocomplete.state:
        if Key == "/": modes.path_autocomplete.letsStop += "/"
        if modes.path_autocomplete.letsStop == "//": 
            modes.path_autocomplete.state = modes.path_autocomplete.fst_hit = False
            Key = ""
            modes.path_autocomplete.letsStop = ""
        if len(globalLists.fileListMain) == 1:
            var_4_hotKeys.prnt = var_4_hotKeys.prnt_step_back
            ΔL = len(globalLists.fileListMain[0]) - len(partial.path)
            page_struct.cur_cur_pos += ΔL
            slash = ""
            if os.path.isdir(str(globalLists.fileListMain[0])):
                slash = "/"
            partial.path = partial.path.replace(r'//', '/')
            var_4_hotKeys.prnt = var_4_hotKeys.prnt.replace(f"{partial.path}", f"{globalLists.fileListMain[0]}{slash}")
            var_4_hotKeys.prnt = var_4_hotKeys.prnt.replace("//", "/")
            partial.path = globalLists.fileListMain[0] + slash
        else:
            partial.path += str(Key)
    if Key == '/' and not modes.path_autocomplete.fst_hit:
        modes.path_autocomplete.state = modes.path_autocomplete.fst_hit = True
        globalLists.bkp = copy.copy(globalLists.fileListMain) # todo has to deprecate bkp list
        partial.path += str(Key)
    if modes.path_autocomplete.state:
        globalLists.ls = createDirList(partial.path, "-maxdepth 1")
    if globalLists.ls != []:
          globalLists.fileListMain = globalLists.ls
          return "go2 0"
    else:
        return "cont"
def list_from_file(cmd: str) -> list:
    funcName = "list_from_file"
    list0 = run_cmd1(cmd)
    try:
        out = copy.copy(list0[0])
        err = copy.copy(list0[1])
        list0 = open(out)
        #list0 = codecs.decode(list0)
    except TypeError:
        print("type err")
        pass
    retList = []
    if list0 is None: achtung("no fd")
    if keys.dirty_mode: print(err, out)
    #while True:
     #   path = list0.readline()
    for path in iter(list0.readline, b''):
        if path !="":
          if path[-1] == '\n':
              retList.append(path[:-1])
          else:
              retList.append(path)
        else:
          break
    return retList
def createDirList(dirname: str, opts: str, no_grep: bool = False) -> list:
    funcName = "createDirList"
    path, head = os.path.split(dirname)
    head0 = head.replace('\\', '')
    path = escapeSymbols(path)
   # if no_grep: cmd = f"find -L {path} {opts}"
    cmd = f"find -L {path} {opts}|grep -Ei '{head0}'"
    errMsg_dbg(f"{cmd=}", funcName)
    list0 = list_from_file(cmd)
    if list0 == []:
        cmd = f"find -L {path} {opts}"
        list0 = list_from_file(cmd)
    partial.retList = list0
    return list0
def createDirList0(dirname: str, opts: str, no_grep: bool = False) -> list:
    funcName = "createDirList0"
    path, head = os.path.split(dirname)
    #path = dirname.replace(f"{head}", '')
    head0 = head.replace('\\', '')
    path = escapeSymbols(path)
    #path = path.replace("\\\\", "\\")
    #path = path.replace("\\\\", "\\")
    cmd = f"find {path} {opts}|grep -Ei '{head0}'"
    errMsg_dbg(f"{cmd=}", funcName)
    if no_grep: cmd = f"find {path} {opts}"
    os.system(f"echo 'cmd == {cmd}'")
    list0 = list_from_file(cmd)
    partial.retList = list0
    return list0
def run_cmd(cmd: str, opts: str, timeout0: float = 100) -> list:
    cmd = [f"{str(cmd)} {str(opts)}", ]
    p = sp.Popen(cmd, shell=True, stderr=sp.PIPE, stdout=sp.PIPE)
    return p.communicate(timeout=timeout0)
def run_cmd1(cmd: str, timeout0: float = 100) -> list:
    cmd = [f"{str(cmd)}", ]
    stderr0_name = f"/tmp/run_cmd_err{str(random.random())}"
    stderr0 = open(stderr0_name, "w+")
    stdout0_name = f"/tmp/run_cmd_out{str(random.random())}"
    stdout0 = open(stdout0_name, "w+")
    p = sp.Popen(cmd, shell=True, stderr=stderr0, stdout=stdout0)
    p.communicate()
    return [stdout0_name, stderr0_name]
def run_cmd0(cmd: str, timeout0: float = 100) -> list:
    cmd = [f"{str(cmd)}", ]
    stderr0_name = f"/tmp/run_cmd_err{str(random.random())}"
    stderr0 = open(stderr0_name, "w+")
    stdout0_name = f"/tmp/run_cmd_out{str(random.random())}"
    stdout0 = open(stdout0_name, "w+")
    p = sp.Popen(cmd, shell=True, stderr=stderr0, stdout=stdout0)
    p.communicate()
    return [stdout0_name, stderr0_name]
def stop_autocomplete():
    modes.path_autocomplete.state = modes.path_autocomplete.fst_hit = False
    modes.path_autocomplete.letsStop = ""
def reset_autocomplete():
    var_4_hotKeys.ENTER_MODE = modes.path_autocomplete.state = modes.path_autocomplete.fst_hit = False
    var_4_hotKeys.prnt  = ""
    var_4_hotKeys.fileName = ""
    var_4_hotKeys.save_prnt_to_copy_file = ""
    var_4_hotKeys.prnt_step_back = ""
    var_4_hotKeys.prnt_full = ""
    var_4_hotKeys.prnt_short = ""
    var_4_hotKeys.full_length = 0
    page_struct.cur_cur_pos = 0
    page_struct.left_shift_4_cur = 0
    partial.path = ""
    modes.path_autocomplete.letsStop = ""
    globalLists.ls = []
    var_4_hotKeys.only_1_slash = ""
    if globalLists.bkp != []:
        globalLists.fileListMain = copy.copy(globalLists.fileListMain0)
def flushInputBuffer():
    page_struct.left_shift_4_cur = 0
    page_struct.cur_cur_pos = 0
    modes.path_autocomplete.state = modes.path_autocomplete.fst_hit = False
    return ""
def apostrophe_split(str0: str, delim: str) -> str:
    bulks = str0.split(delim)
    strLoc = ''
    for i in range(0, len(bulks)):
        strLoc += f"{bulks[i]}\{delim}"
    strLoc = strLoc[:-2]
    return strLoc

def escapeSymbols(name: str, symbIndx = -1):
    try:
        if len(name) == 0: return name
    except TypeError:
        return name
    quote = ''
    if (name[0] == "\'" or name[0] == "\`") and name[0] == name[-1]:
        quote = name[0]
        name = name[1:-1]
    if symbIndx == -1:
        name = name.replace(" ", "\ ")
        name = name.replace("$", "\$")
        name = name.replace(";", "\;")
        name = name.replace('`', '\`')
        name = apostrophe_split(name, "'")
        name = name.replace("&", "\&")
        name = name.replace("(", "\(")
        name = name.replace(")", "\)")
        name = name.replace("}", "\}")
        name = name.replace("{", "\{")
    if symbIndx == 0:
        name = name.replace(" ", "\ ")
    if symbIndx == 1:
        name = name.replace("$", "\$")
    if symbIndx == 2:
        name = name.replace(";", "\;")
    if symbIndx == 3:
        name = name.replace('`', '\`')
    if symbIndx == 4:
        name = name.replace("'", "\'")
    if symbIndx == 5:
        name = name.replace("&", "\&")
    name = name.replace("\n", "")
    if name[-1] == "\n":
        name = name[:-1]
    if quote != '':
        name = quote + name + quote
    return name
def renameFile(fileName: str, cmd: str):
    funcName = "renameFile"
    cmd = cmd[4:]
    getFileIndx = re.compile('\d+\s+')
    fileIndx = getFileIndx.match(cmd)
    cmd = cmd.replace(fileIndx.group(0), '')
    if modes.sieve.state: old_name = globalLists.filtered[get_proper_indx_4_page(int(fileIndx.group(0)))]
    else: old_name = globalLists.fileListMain0[get_proper_indx_4_page(int(fileIndx.group(0)))]
    res = re.match('\/', cmd)
    if not res:
        fileName = old_name
        fileName, _ = os.path.split(fileName)
        fileName += f"/{cmd}"
    else:
        fileName = f"{cmd}"
    fileName = fileName.replace("//", "/")
    fileName_copy: str = fileName
    if os.path.isdir(fileName): 
        _, fileName_copy = os.path.split(old_name)
        fileName_copy = f"{fileName}/{fileName_copy}"
    globalLists.fileListMain[get_proper_indx_4_page(int(fileIndx.group(0)))] = fileName_copy
    globalLists.fileListMain0[get_proper_indx_4_page(int(fileIndx.group(0)))] = fileName_copy
    if modes.sieve.state: globalLists.filtered[get_proper_indx_4_page(int(fileIndx.group(0)))] = fileName_copy
    fileName = escapeSymbols(fileName)
    old_name = escapeSymbols(old_name)
    if_path_not_existed, _ = os.path.split(fileName)
    cmd = f"mkdir -p {if_path_not_existed}"
    os.system(cmd)
    cmd = "mv -f --backup " + f'{old_name}' + " " + f'{fileName}'
    reset_autocomplete()
    sp.Popen([cmd,], shell=True)
    return
def getFileNameFromCMD_byIndx(cmd: str):
    cmd = cmd[3:]
    getFileIndx = re.compile('-?\d+')
    fileIndx = getFileIndx.match(cmd)
    if modes.sieve.state: fileName = globalLists.filtered[get_proper_indx_4_page(int(fileIndx.group(0)))]
    else: fileName = globalLists.fileListMain0[get_proper_indx_4_page(int(fileIndx.group(0)))]
    if fileName[-1] == "\n":
        fileName = fileName[:-1]
    return fileName
def getFileNameFromCMD(cmd: str):
    cmd = cmd[3:]
    getFileIndx = re.compile('-?\d+\s+')
    fileIndx = getFileIndx.match(cmd)
    cmd = cmd.replace(fileIndx.group(0), '')
    if modes.sieve.state: fileName = globalLists.filtered[get_proper_indx_4_page(int(fileIndx.group(0)))]
    else: old_name = globalLists.fileListMain0[get_proper_indx_4_page(int(fileIndx.group(0)))]
    res = re.match('\/', cmd)
    if not res:
        fileName = old_name
        fileName, _ = os.path.split(fileName)
        fileName += f"/{cmd}"
    else:
        fileName = f"{cmd}"
    return fileName
def delFile(fileName: str, cmd: str, dontDelFromTableJustMark = True) -> str:
    cmd = cmd[3:]
    getFileIndx = re.compile('-?\d+')
    fileIndx = getFileIndx.match(cmd)
    fileName = globalLists.fileListMain0[get_proper_indx_4_page(int(fileIndx.group(0)))]
    if modes.sieve.state: fileName = globalLists.filtered[get_proper_indx_4_page(int(fileIndx.group(0)))]
    fileName = escapeSymbols(fileName)
    cmd = "rm -f " + f"{fileName}"
    os.system(cmd)
    heyFile = os.path.exists(fileName)
    if False == heyFile and dontDelFromTableJustMark == False:
        globalLists.fileListMain.remove(int(fileIndx.group(0)))
    if not heyFile and dontDelFromTableJustMark:
        if modes.sieve.state: 
            globalLists.fileListMain0.insert(int(fileIndx.group(0)), f"{globalLists.filtered[int(fileIndx.group(0))]}::D")
            globalLists.filtered[int(fileIndx.group(0))] = f"{globalLists.filtered[int(fileIndx.group(0))]}::D"
            globalLists.fileListMain = globalLists.fileListMain0
        #elif modes.path_autocomplete.state: globalLists.fileListMain0[int(fileIndx.group(0))] = f"{globalLists.fileListMain0[int(fileIndx.group(0))]}::D"
        else: 
            globalLists.fileListMain[int(fileIndx.group(0))] = f"{globalLists.fileListMain0[int(fileIndx.group(0))]}::D"
            globalLists.fileListMain0[int(fileIndx.group(0))] = f"{globalLists.fileListMain0[int(fileIndx.group(0))]}::D"
    return f"{fileName}::D"
def copyFile(fileName: str, cmd: str, dontInsert = False) -> str:
    cmd = cmd[3:]
    getFileIndx = re.compile('-?\d+\s+')
    fileIndx = getFileIndx.match(cmd)
    cmd = cmd.replace(fileIndx.group(0), '')
    if modes.sieve.state: old_name = globalLists.filtered[get_proper_indx_4_page(int(fileIndx.group(0)))]
    else: old_name = globalLists.fileListMain0[get_proper_indx_4_page(int(fileIndx.group(0)))]
    res = re.match('\/', cmd)
    if not res:
        fileName = old_name
        fileName, _ = os.path.split(fileName)
        fileName += f"/{cmd}"
    else:
        fileName = f"{cmd}"
    fileName = fileName.replace("//", "/")
    fileName_copy: str = fileName
    if os.path.isdir(fileName): 
        _, fileName_copy = os.path.split(old_name)
        fileName_copy = f"{fileName}/{fileName_copy}"
    if not dontInsert:
        globalLists.fileListMain.insert(get_proper_indx_4_page(int(fileIndx.group(0))), fileName_copy)
        globalLists.fileListMain0.insert(get_proper_indx_4_page(int(fileIndx.group(0))), fileName_copy)
    fileName = escapeSymbols(fileName)
    old_name = escapeSymbols(old_name)
    if_path_not_existed, _ = os.path.split(fileName)
    cmd = f"mkdir -p {if_path_not_existed}"
    os.system(cmd)
    cmd = "cp -f " + f"{old_name}" + " " + f"{fileName}"
    reset_autocomplete()
    os.system(cmd)
    return f"{fileName}::D"
def writeInput_str(prompt: str, prnt: str, blank_len = 0):
    prompt_len = len(prompt)
    if blank_len == 0:
        blank = ' ' * (prompt_len + len(prnt) + 1)
    else:
        blank = ' ' * (prompt_len + blank_len + 1)
    print(f"\r{blank}", end='', flush=True)
    print(f"\r{prompt}{prnt}", end=' ', flush=True)
    print(f'\033[{page_struct.left_shift_4_cur + 1}D', end='', flush=True)
def clear_cmd_line(prompt: str, prnt: str, blank_len = 0):
    prompt_len = len(prompt)
    if blank_len == 0:
        blank = ' ' * (prompt_len + len(prnt) + 1)
    else:
        blank = ' ' * (prompt_len + blank_len + 1)
    print(f"\r{blank}", end='', flush=True)
    print(f"\r", end='', flush=True)
def pressKey():
    prnt = ""
    ENTER = 13
    while True:
        p = input()
        try:
            Key = click.getchar()
            if Key == "\x1b[A":
                print("yes", end='')
            if ENTER == ord0(Key):
                nop()
            else:
                prnt += f"{Key}"
                print(f"{Key} = {ord0(Key)}", end='', flush=True)
        except TypeError:
             print(f"{Key} = {Key}", end='', flush=True)
def ord0(Key):
    try:
        Key = ord(Key)
        return Key
    except TypeError:
        return -1
def hotKeys(prompt: str) -> str|None:
    funcName = "hotKeys"
    full_length = 0
    #if not modes.path_autocomplete.state:
       # var_4_hotKeys.prnt = ""
    var_4_hotKeys.save_prnt_to_copy_file = ''
    var_4_hotKeys.save_prompt_to_copy_file = ''
    var_4_hotKeys.save_cur_cur_pos = page_struct.cur_cur_pos
    prnt0 = ''
    prnt_short = ''
    prnt_full = ''
    ptrn = ''
    fileIndx = 0
    fileName = ''
    regex_result = ''
    Key = None
    exec(keyCodes())
    no_back_slash = subtern.no_back_slash
    while True:
        if kCodes.Key is None:
            """try: Key = codecs.decode(os.read(sys.stdin.fileno(), 32))#click.getchar()
            except IOError:
                errMsg_dbg("got no Key", funcName)
                pass
            achtung(Key)"""
            Key = click.getchar()
            if keys.term_app: return Key
        else:
            Key = kCodes.Key
            kCodes.Key = None
        if kCodes.Alt_0 == Key or no_back_slash(kCodes.Alt_0) == Key:
            modes.page_indices.global_or_not = not modes.page_indices.global_or_not
            return "slgi"
        if kCodes.Alt_2 == Key or no_back_slash(kCodes.Alt_2) == Key:
            find_all_tam_consoles()
            modes.switch_2_nxt_tam.state = True
            globalLists.fileListMain = globalLists.tam_instances.name
            inlines.switch_make_page = """
ps: ps0 = ps0()
tmp.table, tmp.too_short_row = make_page_of_tam_list(globalLists.fileListMain, ps.ps)
"""
            return "none"
        if kCodes.INSERT == Key or no_back_slash(kCodes.INSERT) == Key:
            try:
                indx = int(input("Please, enter indx of dir/file name to autocomplete: "))
            except ValueError:
                return ""
            slash = ""
            try:
                if os.path.isdir(str(globalLists.fileListMain[indx])):
                   slash = "/"
                name = (globalLists.fileListMain[indx]) + slash
            except IndexError:
                errMsg("the indx is out of range.", funcName, 2)
                kCodes.Key = kCodes.INSERT
                continue
            """
            """
            var_4_hotKeys.prnt = var_4_hotKeys.prnt.replace(f"{partial.path}", name)
            page_struct.cur_cur_pos += (len(name) - len(partial.path))
            partial.path = name
            switch_global_list(slash)
            partial.path = partial.path.replace("//", "/")
            updateDirList()
            if partial.path[-1] == "/": modes.path_autocomplete.letsStop = ""
            errMsg_dbg(f"{slash=}", funcName)
            return f"go2 {modes.path_autocomplete.page_struct.num_page}"
        if kCodes.PgUP == Key:
            if len(var_4_hotKeys.prnt) == page_struct.cur_cur_pos:
                stop_autocomplete()
            return None
        if kCodes.F5 == Key:
            create_or_updateMainList()
            return "go2 0"
        if kCodes.F1 == Key:
            if modes.sieve.state:
                globalLists.fileListMain = globalLists.fileListMain0
                modes.sieve.state = False
                return f"go2 {page_struct.num_page}"
            if globalLists.ls == [] and not modes.switch_2_nxt_tam.state:
                continue
            go2 = ""
            full_length = len(var_4_hotKeys.prnt) + len(var_4_hotKeys.prompt)
            if modes.path_autocomplete.state or modes.switch_2_nxt_tam.state:
                inlines.switch_make_page = inlines.make_page_of_files2
                globalLists.fileListMain = globalLists.fileListMain0
                modes.path_autocomplete.state = modes.switch_2_nxt_tam.state = False
                globalLists.ls = []
                try:
                    go2 = f"go2 {__manage_pages.ps_bkp.num_page}"
                except AttributeError:
                    go2 = "go2 0"
            writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt, full_length)
            return go2
        if kCodes.F12 == Key:
            full_length = len(var_4_hotKeys.prnt)
            var_4_hotKeys.prnt = flushInputBuffer()
            reset_autocomplete()
            writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt, full_length)
            continue
        if Key == kCodes.UP_ARROW:
            list_autocomplete_pages(Key)
            return "np"
        if Key == kCodes.DOWN_ARROW:
            list_autocomplete_pages(Key)
            writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt)
            return "pp"
        if Key == kCodes.RIGHT_ARROW:
            if page_struct.left_shift_4_cur > 0:
                page_struct.left_shift_4_cur -= 1
                page_struct.cur_cur_pos = page_struct.cur_cur_pos + 1
                print('\033[C', end='', flush=True)
            continue
        if Key == kCodes.LEFT_ARROW:
            if page_struct.cur_cur_pos > 0:
                page_struct.left_shift_4_cur += 1
                page_struct.cur_cur_pos = page_struct.cur_cur_pos - 1
                print('\033[D', end='', flush=True)
            continue
        if kCodes.ENTER == ord0(Key):
            if modes.switch_2_nxt_tam.state:
                swtch_2_nxt_tam()
                continue
            ret = var_4_hotKeys.prnt
            if not var_4_hotKeys.ENTER_MODE:
                var_4_hotKeys.save_prnt = var_4_hotKeys.prnt
                var_4_hotKeys.save_prompt = var_4_hotKeys.prompt
                try:
                    ret = handleENTER(fileName)
                except IndexError:
                    errMsg("Wrong indx was picked", "handleEnter", 2)
                    continue
                try:
                    raise AttributeError
                    var_4_hotKeys.prnt = ""
                    page_struct.left_shift_4_cur = 0
                    page_struct.cur_cur_pos = 0
                except AttributeError:
                    var_4_hotKeys.ENTER_MODE = False
            else:
                ret = handleENTER(fileName)
            if "cont" == ret:
                continue
            var_4_hotKeys.prompt = var_4_hotKeys.save_prompt
            return ret
        if kCodes.DELETE == Key:
            if page_struct.left_shift_4_cur == 0:
                continue
            else:
                var_4_hotKeys.prnt = var_4_hotKeys.prnt[:len(var_4_hotKeys.prnt) - page_struct.left_shift_4_cur] + var_4_hotKeys.prnt[len(var_4_hotKeys.prnt) - page_struct.left_shift_4_cur + 1:]
            if page_struct.left_shift_4_cur > 0:
                page_struct.left_shift_4_cur -= 1
            prnt0 = var_4_hotKeys.prnt
            full_length = len(var_4_hotKeys.prnt)
            writeInput_str(var_4_hotKeys.prompt, prnt0)
            continue
        if kCodes.BACKSPACE == ord0(Key):
            if page_struct.left_shift_4_cur == 0:
                var_4_hotKeys.prnt = var_4_hotKeys.prnt[:len(var_4_hotKeys.prnt) - 1]
                page_struct.cur_cur_pos = len(var_4_hotKeys.prnt)
            else:
                var_4_hotKeys.prnt = var_4_hotKeys.prnt[:len(var_4_hotKeys.prnt) - page_struct.left_shift_4_cur - 1] + var_4_hotKeys.prnt[len(var_4_hotKeys.prnt) - page_struct.left_shift_4_cur:]
            if page_struct.cur_cur_pos > 0:
                page_struct.cur_cur_pos = page_struct.cur_cur_pos - 1
            full_length = len(var_4_hotKeys.prnt)
            writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt)
            globalLists.ret = switch_global_list(Key)
            if globalLists.ret == "cont":
                continue
            else:
                return globalLists.ret
        if kCodes.ESCAPE == ord0(Key): SYS(), sys.exit(0)
        if kCodes.TAB == ord0(Key):
            handleTAB(prompt)
            continue
        else:
            if var_4_hotKeys.only_1_slash == Key and Key == '/':
                var_4_hotKeys.prnt = var_4_hotKeys.prnt.replace('//', '/')
                partial.path = partial.path.replace('//', '/')
                writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt)
                """"""
            else:
                page_struct.cur_cur_pos = page_struct.cur_cur_pos + 1
            var_4_hotKeys.only_1_slash = Key
            if page_struct.cur_cur_pos == full_length and page_struct.left_shift_4_cur == 0:
                var_4_hotKeys.prnt_step_back = var_4_hotKeys.prnt
                var_4_hotKeys.prnt += f"{Key}"
                writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt)
                globalLists.ret = switch_global_list(Key)
                if globalLists.ret == "cont":
                    continue
                else:
                    return globalLists.ret
            else:
                var_4_hotKeys.prnt_step_back = var_4_hotKeys.prnt
                var_4_hotKeys.prnt =f"{var_4_hotKeys.prnt[:page_struct.cur_cur_pos - 1]}{Key}{var_4_hotKeys.prnt[page_struct.cur_cur_pos - 1:]}"
            writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt)
            globalLists.ret = switch_global_list(Key)
            if globalLists.ret == "cont":
                continue
            else:
                return globalLists.ret
def custom_input(prompt: str) -> str:
    if keys.term_app: return ""
    if page_struct.question_to_User != "":
        print(f"{page_struct.question_to_User}")
        page_struct.question_to_User = ""
    if modes.path_autocomplete.state:
        writeInput_str(prompt, var_4_hotKeys.prnt)
    else:
        print(f"{prompt}{var_4_hotKeys.prnt}", end='', flush=True)
    return hotKeys(prompt)
def signal_manager(sig, frame):
    print(f"sig = {sig}")
#signal.signal(signal.CTRL_BREAK_EVENT, signal_manager)
def SYS():
    no_SYS = os.path.exists("/tmp/no_SYS")
    no_SYS1 = get_arg_in_cmd("-SYS", sys.argv)
    Markers.console_title = "Exited"
    SetDefaultKonsoleTitle()
    if no_SYS == True or no_SYS1 == "1":
        os.system("rm -f /tmp/no_SYS")
        sys.exit(0)
    print("\r\nSee You Soon\nBye.. bye, my Dear User 🙂")
    sys.exit(0)
def SetDefaultKonsoleTitle(addStr = ""):
    out = get_arg_in_cmd("-path0", sys.argv)
    find_all_tam_consoles()
    konsole_id = len(globalLists.tam_instances.name)
    not_sure_4_uniq = re.compile(f"{Markers.console_title}{konsole_id}")
    for id in globalLists.tam_instances.name:
        try:
            if not_sure_4_uniq.match(id).group(0):
                konsole_id += 1
                break
        except AttributeError:
            pass
    try:
        out += f" {put_in_name()}"
        out = out.replace("'", "")
        if(checkArg("-dirty")): print(f"konsole title = {out}")
    except TypeError:
        out = f"cmd is empty {put_in_name()}"
    page_struct.KonsoleTitle = f"{Markers.console_title_pefix}{Markers.console_title}{konsole_id} {out}"
    os.system(f"echo -ne '\033]30;{page_struct.KonsoleTitle}{addStr}\007'")
def adjustKonsoleTitle(addStr: str, ps: page_struct) -> None:
    if modes.switch_2_nxt_tam.state: return
    os.system(f"echo -ne '\033]30;{ps.KonsoleTitle}{addStr}\007'")
def self_recursion():
    no_SYS = os.path.exists("/tmp/no_SYS")
    no_SYS1 = get_arg_in_cmd("-SYS", sys.argv)
    if no_SYS == True or no_SYS1 == "1":
        os.system("rm -f /tmp/no_SYS")
        sys.exit(0)
    else:
        os.system("touch -f /tmp/no_SYS")
    cmd_line=""
    for i in range(1, len(sys.argv)):
        cmd_line += f" {sys.argv[i]}"
    cmd_line += f";{sys.executable} {sys.argv[0]} -SYS 1"
    cmd = f"{sys.executable} {sys.argv[0]} {cmd_line}"
    os.system(cmd)
    os.system("rm -f /tmp/no_SYS")
def banner0(delay: int):
    _, colsize = os.popen("stty size", 'r').read().split()
    while True:
        typeIt = f"© SarK0Y {info_struct.year}".center(int(colsize), "8")
        print(f"\r{typeIt}", flush=True, end='')
        time.sleep(delay)
        typeIt = f"© Knyazhev Evgeney {info_struct.year}".center(int(colsize), "|")
        print(f"\r{typeIt}", flush=True, end='')
        time.sleep(delay)
        typeIt = f"© Knyazhev Evgeney {info_struct.year}".center(int(colsize), "/")
        print(f"\r{typeIt}", flush=True, end='')
        time.sleep(delay)
        typeIt = f"© Knyazhev Evgeney {info_struct.year}".center(int(colsize), "-")
        print(f"\r{typeIt}", flush=True, end='')
        time.sleep(delay)
        typeIt = f"© Knyazhev Evgeney {info_struct.year}".center(int(colsize), "+")
        print(f"\r{typeIt}", flush=True, end='')
        time.sleep(delay)
        typeIt = f"© Knyazhev Evgeney {info_struct.year}".center(int(colsize), "=")
        typeIt = f"© SarK0Y {info_struct.year}".center(int(colsize), "∞")
        print(f"\r{typeIt}", flush=True, end='')
        time.sleep(delay)
def info():
    os.system(f"echo -ne '\033]30;TAM {info_struct.ver}.{info_struct.rev}\007'") # set konsole title
    clear_screen()
    _, colsize = os.popen("stty size", 'r').read().split()
    print(" Project: Tiny Automation Manager. ".center(int(colsize), "◑"))
    print(f" TELEGRAM: {info_struct.telega} ".center(int(colsize), "◑"))
    print(" ALG0Z RU: https://dzen.ru/alg0z ".center(int(colsize), "◑"))
    print(" ALG0Z EN: https://alg0z.blogspot.com ".center(int(colsize), "◑"))
    print(" ChangeLog: https://alg0z8n8its9lovely6tricks.blogspot.com/2023/09/tam-changelog.html ".center(int(colsize), "◑"))
    print(" E-MAIL: sark0y@protonmail.com ".center(int(colsize), "◑"))
    print(" Supported platforms: TAM  for Linux & alike; TAW for Windows. ".center(int(colsize), "◑"))
    print(f" Version: {info_struct.ver}. ".center(int(colsize), "◑"))
    print(f" Revision: {info_struct.rev}. ".center(int(colsize), "◑"))
    print(f"\nlicense/Agreement:".title())
    print("Personal usage will cost You $0.00, but don't be shy to donate me.. or You could support me any other way You want - just call/mail me to discuss possible variants for mutual gains. 🙂")
    print("Commercial use takes $0.77 per month from You.. or just Your Soul 😇😜")
    print("my the Best Wishes to You 🙃")
    print(" Donations: https://boosty.to/alg0z/donate ".center(int(colsize), "◑"))
    print("\n")
    try:
        banner0(.3)
    except KeyboardInterrupt:
        SYS()
    except:
        SYS()
def help():
    print("np - next page pp - previous page 0p - 1st page lp - last page go2 <number of page>", end='')
def achtung(msg):
    if not checkArg("-dbg") and not checkArg("-use-achtung"): return
    os.system(f"notify-send -t 30000 '{str(msg)}' 1>&2 2>/dev/null")
def log(msg, num_line: int, funcName: str):
    f = open("/tmp/it.log", mode="w")
    print(f"{funcName} said cmd = {msg} at line: {str(num_line)}", file=f)
def clear_screen():
    if keys.dirty_mode:
        return
    os.system('clear')
def mark_the_viewer(tag: str) -> int:
    if tag == "-term-app": return 1
    if tag == "-view_w" or tag == "-view-w": return 0
def init_view(c2r: childs2run):
    i = 0
    for v in range(1, len(sys.argv)):
        if sys.argv[v] == "-view_w" or sys.argv[v] == "-term-app":
            c2r.viewer.append(str(sys.argv[v + 1]))
            c2r.prnt += f"\n  {i}: {c2r.viewer[-1]}"
            c2r.mode2run.append(mark_the_viewer(sys.argv[v]))
            i += 1
    return c2r
def run_viewers(c2r: childs2run, fileListMain: list, cmd: str):
    if modes.switch_2_nxt_tam.state: return
    funcName = "run_viewers"
    viewer_indx: int = 0
    file_indx: int = 0
    try:
        viewer_indx, file_indx = cmd.split()
        viewer_indx = int(viewer_indx)
        file_indx = int(file_indx)
    except ValueError:
        file_indx = cmd.split()
        file_indx = file_indx[0]
        try:
            file_indx = int(file_indx)
        except ValueError:
            return
    if partial.path == "":
        file2run: str = globalLists.fileListMain[file_indx]
        file2run = escapeSymbols(file2run)
    else:
        file2run = escapeSymbols(partial.path)
    if c2r.viewer[viewer_indx] == "mc": subtern.activate_mc_mode()
    if subtern.modes.mc.active: file2run, _ = os.path.split(file2run)
    cmd = f'{c2r.viewer[viewer_indx]}'
    cmd_line: str
    if c2r.mode2run[viewer_indx] == modes.mark_the_viewer.EXTRN:
        cmd_line = f'{c2r.viewer[viewer_indx]}' + ' ' + f"{file2run} > /dev/null 2>&1"
    else: cmd_line = f'{c2r.viewer[viewer_indx]}' + ' ' + f"{file2run}"
    cmd = [cmd_line,]
    stderr0 = f"/tmp/run_viewers{str(random.random())}"
    stderr0 = open(stderr0, "w+")
    t = None
    if c2r.mode2run[viewer_indx] == modes.mark_the_viewer.EXTRN:
        t = sp.Popen(cmd, shell=True, stderr=stderr0)
        c2r.running.append(t)
    else:
        keys.term_app = True
        std_in_out = [sys.stdin.fileno(), sys.stdout.fileno()]
        t = subtern.term_app(cmd[0], std_in_out)
        c2r.running.append(t)
        setTermAppStatus_Thr(c2r.running[-1])
    if t.stderr is not None:
        os.system(cmd_line)
    if keys.dirty_mode:
        os.system(f"echo '{t.stderr} {t.stdout}' > /tmp/wrong_cmd")
def run_viewers_li(ps: page_struct, fileListMain: list, cmd: str): # w/ local indices
    if modes.switch_2_nxt_tam.state: return
    funcName = "run_viewers_li"
    c2r: childs2run = ps.c2r
    num_page = ps.num_cols * ps.num_rows * ps.num_page
    viewer_indx: int = 0
    file_indx: int = 0
    try:
        viewer_indx, file_indx = cmd.split()
        viewer_indx = int(viewer_indx)
        file_indx = get_proper_indx_4_page(int(file_indx))
    except ValueError:
        file_indx = cmd.split()
        try:
            file_indx = get_proper_indx_4_page(int(file_indx[0]))
        except ValueError:
            return
    if partial.path == "":
        try:
            file2run: str = globalLists.fileListMain[file_indx]
        except IndexError:
            errMsg(f"indx {file_indx} gets out of range", funcName, 2)
            return
        file2run = escapeSymbols(file2run)
    else:
        file2run = escapeSymbols(partial.path)
    if c2r.viewer[viewer_indx] == "mc": subtern.activate_mc_mode()
    if subtern.modes.mc.active: file2run, _ = os.path.split(file2run)
        #file2run += '//'
    errMsg_dbg(f"{file2run}{subtern.modes.mc.active}", funcName)
    achtung(f"{file2run}")
    achtung(f"{subtern.modes.mc.active}")
    cmd = f'{c2r.viewer[viewer_indx]}'
    if c2r.mode2run[viewer_indx] == modes.mark_the_viewer.EXTRN:
        cmd_line = f'{c2r.viewer[viewer_indx]}' + ' ' + f"{file2run} > /dev/null 2>&1"
    else: cmd_line = f'{c2r.viewer[viewer_indx]}' + ' ' + f"{file2run}"
    cmd = [cmd_line,]
    stderr0 = f"/tmp/run_viewers{str(random.random())}"
    stderr0 = open(stderr0, "w+")
    t = None
    if c2r.mode2run[viewer_indx] == modes.mark_the_viewer.EXTRN:
        t = sp.Popen(cmd, shell=True, stderr=stderr0)
        c2r.running.append(t)
    else:
        keys.term_app = True
        std_in_out = [sys.stdin.fileno(), sys.stdout.fileno()]
        t = subtern.term_app(cmd[0], std_in_out)
        c2r.running.append(t)
        setTermAppStatus_Thr(c2r.running[-1])
    if t.stderr is not None:
        os.system(cmd_line)
    if keys.dirty_mode:
        os.system(f"echo '{t.stderr} {t.stdout}' > /tmp/wrong_cmd")
    c2r.running.append(t)
def cmd_page(cmd: str, ps: page_struct, fileListMain: list):
    funcName = "cmd_page"
    if cmd == None: return
    if cmd == "ver":
        page_struct.question_to_User = f"VER {info_struct.ver}.{info_struct.rev}"
        return
    if var_4_hotKeys.prnt == "вар":
        var_4_hotKeys.prnt = keys.вар
        return
    if cmd[:4] == "deli":
        try:
            _, index = cmd.split()
            page_struct.question_to_User = f"deleted record {globalLists.fileListMain.pop(int(index))}"
        except IndexError:
            errMsg(f"Indx has to be in range 0 - {len(globalLists.fileListMain)}", funcName, 0.7)
        return
    if cmd[:5] == "f2mrg" or (cmd[:3] == "mrg" and len(cmd) > 3):
        try:
            _, index = cmd.split()
            index = get_proper_indx_4_page(index)
            globalLists.merge.append(globalLists.fileListMain[index])
            globalLists.merge = list(set(globalLists.merge))
        except IndexError:
            errMsg(f"Indx has to be in range 0 - {len(globalLists.fileListMain)}", funcName, 0.7)
            return
        except ValueError:
            errMsg("Indx has to be an integer", funcName, 0.7)
        return
    if cmd == "cl mrg" or cmd == "clear mrg" or cmd == "clear merge":
        modes.sieve.state = False
        globalLists.fileListMain = globalLists.fileListMain0
        globalLists.filtered = globalLists.merge = [] 
        return
    if cmd == "show mrg" or cmd == "show merge" or cmd == "switch to merged list":
        if globalLists.merge == []:
            errMsg("Merge list is empty", funcName, 1)
            return
        globalLists.fileListMain = globalLists.merge
        globalLists.filtered = globalLists.merge
        modes.sieve.state = True
        ps.num_page = 0
        return
    if cmd == "mrg" or cmd == "merge":
        globalLists.merge += globalLists.filtered
        globalLists.merge = list(set(globalLists.merge))
        return
    if cmd == "slgi":
        if inlines.switch_make_page == inlines.make_page_of_files2:
            inlines.switch_make_page = inlines.make_page_of_files2_li
        else:
            inlines.switch_make_page = inlines.make_page_of_files2
        if inlines.switch_run_viewer == inlines.run_viewer:
            inlines.switch_run_viewer = inlines.run_viewer_li
        else:
            inlines.switch_run_viewer = inlines.run_viewer
        return
    if cmd[0:5] == "sieve":
        _, rgx = cmd.split()
        globalLists.filtered = sieve_list(globalLists.fileListMain, rgx)
        if globalLists.filtered != []:
            modes.sieve.state = True
            globalLists.fileListMain = globalLists.filtered
            ps.num_page = 0
            return
        else: errMsg("No records were found", funcName, 1)
        modes.sieve.state = False
        return
    lp = len(globalLists.fileListMain) // (ps.num_cols * ps.num_rows)
    if cmd == "np":
       ps.num_page += 1
       page_struct.num_page = ps.num_page
       if ps.num_page > lp:
            ps.num_page = lp
       return
    if cmd == "pp":
        if ps.num_page > 0:
            ps.num_page -= 1
            page_struct.num_page = ps.num_page
        return
    if cmd == "0p":
        ps.num_page = 0
        return
    if cmd == "lp":
        ps.num_page = lp
        page_struct.num_page = ps.num_page
        return
    if cmd[0:3] == "go2":
        _, ps.num_page = cmd.split()
        ps.num_page = int(ps.num_page)
        if ps.num_page > lp:
            ps.num_page = lp
        return
    if cmd[0:2] == "fp":
        try:
            _, file_indx = cmd.split()
            file_indx = get_proper_indx_4_page(int(file_indx))
            ps.c2r.full_path = f"file {file_indx}\n{str(globalLists.fileListMain[file_indx])}"
            if modes.sieve.state: ps.c2r.full_path = f"file {file_indx}\n{str(globalLists.filtered[file_indx])}"
        except ValueError:
            errMsg("Type fp <file index>", funcName, 2)
            return
        except IndexError:
            top = len(globalLists.fileListMain) - 2
            errMsg(f"You gave index out of range, acceptable values [0, {top}]", funcName, 2)
            return
    if cmd[:4] == "vdir":
        subtern.activate_mc_mode()
        path: str = vdir()
        std_in_out = [sys.stdin.fileno(), sys.stdout.fileno()]
        cmd = f"mc {path}" 
        keys.term_app = True
        proc = subtern.term_app(cmd, std_in_out)
        setTermAppStatus_Thr(proc)
        return
    if cmd[:5] == "uvdir":
        uvdir()
        return
    if cmd == "just [y]es to kill file": 
        modes.file_ops.justYes2KillFile = True
        var_4_hotKeys.prnt = "just-[y]es-to-kill-file mode is activated"
    if modes.path_autocomplete.state == False:
        try:
            p = __manage_pages.ps_bkp.num_page = copy.copy(ps.num_page)
        except AttributeError:
            pass
    exec(inlines.switch_run_viewer)
    #reset_autocomplete()
def manage_pages(fileListMain: list, ps: page_struct): #once0: once = once.once_copy):
    exec(keyCodes())
    tmp.ps = ps
    make_page_struct() #(modes.path_autocomplete.page_struct)
    funcName = "manage_pages"
    cmd = ""
    looped = 0
    c2r = ps.c2r
    while True:
        if keys.term_app:
            time.sleep(.2)
            continue
        if modes.path_autocomplete.state:
            __manage_pages.ps_bkp = copy.copy(ps)
            __manage_pages.c2r_bkp = c2r
            ps = copy.copy(modes.path_autocomplete.page_struct)
        else:
            try:
                ps = copy.copy(__manage_pages.ps_bkp)
                c2r = __manage_pages.c2r_bkp
            except UnboundLocalError:
                pass
            except AttributeError:
                pass
        try:
            if globalLists.stopCode != globalLists.fileListMain[-1] or modes.path_autocomplete.state:
                page_struct.count_pages = ps.count_pages = len(globalLists.fileListMain) // (ps.num_cols * ps.num_rows) + 1
                page_struct.num_files = ps.num_files = len(globalLists.fileListMain)
        except IndexError:
            continue
        if not modes.path_autocomplete.state or not modes.switch_2_nxt_tam.state:
            try:
                ps0.ps.num_page = page_struct.num_page = ps.num_page
            except AttributeError:
                page_struct.num_page = ps.num_page
        addStr = f" files/pages: {ps.num_files}/{ps.count_pages} p. {ps.num_page}"
        adjustKonsoleTitle(addStr, ps)
        clear_screen()
        print(f"{Fore.RED}      NEWS: {ps.news_bar}\n{Style.RESET_ALL}")
        print(f"Viewers: \n{c2r.prnt}\n\nNumber of files/pages: {ps.num_files}/{ps.count_pages} p. {ps.num_page}\nFull path to {c2r.full_path}")
        #achtung(f"{globalLists.bkp}\n{globalLists.fileListMain}")
        exec(inlines.switch_make_page)
        table = tmp.table
        too_short_row = tmp.too_short_row
        del tmp.too_short_row
        del tmp.table
        if keys.dirty_mode:
            print(table)
        try:
            print(tabulate(table, tablefmt="fancy_grid", maxcolwidths=[ps.col_width]))
        except IndexError:
            ps0.ps.num_page = modes.path_autocomplete.page_struct.num_page = ps.num_page = 0
            if checkArg("-dont-exit") and looped < 1: 
                looped += 1
                #cmd = custom_input(var_4_hotKeys.prompt)
                continue
            looped = 0
            errMsg("Unfortunately, Nothing has been found.", "TAM")
            SYS()
            sys.exit(-2)
        print(f"{partial.path = :.^30}")
        try:
            cmd = custom_input(var_4_hotKeys.prompt)
        except KeyboardInterrupt:
            SYS()
        if cmd == "help" or cmd == "" or cmd == "?":
            clear_screen()
            help()
            cmd = custom_input("Please, enter Your command: ")
        else:
            if modes.sieve.state: globalLists.fileListMain = globalLists.filtered
            if modes.path_autocomplete.state: 
                if globalLists.ls != []: globalLists.fileListMain = globalLists.ls
            cmd_page(cmd, ps, globalLists.fileListMain)
        try:
            if modes.path_autocomplete.state:
               ps = copy.copy(__manage_pages.ps_bkp)
               c2r = __manage_pages.c2r_bkp
        except AttributeError:
            pass
        looped = 0
def nop():
    return
def make_page_of_tam_list(fileListMain: list, ps: page_struct):
    row: list =[]
    item = ""
    table: list = []
    none_row = 0
    len_item = 0
    num_page = ps.num_page * ps.num_cols * ps.num_rows
    num_rows = ps.num_rows
    for i in range(0, num_rows):
        for j in range(0, ps.num_cols):
            indx = j + ps.num_cols * i + num_page
            slash = ""
            try:
                item = fileListMain[indx]
                if keys.dirty_mode: print(f"len item = {len(item)}")
                len_item += len(item)
                if modes.path_autocomplete.state or modes.switch_2_nxt_tam.state:
                    len_item = 5
                if len(item) == 1:
                    raise IndexError
                row.append(str(indx) + ":" + item + slash + " " * ps.num_spaces)
            except IndexError:
                none_row += 1
                if keys.dirty_mode: print(f"none row = {none_row}; i,j = {i},{j}")
                row.append(f"{Back.BLACK}{str(indx)}:{' ' * ps.num_spaces}{Style.RESET_ALL}")
                num_rows = i
        if none_row < 3 and len_item > 4:
            table.append(row)
        if num_rows != ps.num_rows:
            break
        row = []
        none_row = 0
    too_short_row = len(table)
    return table, too_short_row
def make_page_of_files2(fileListMain: list, ps: page_struct):
    row: list =[]
    item = ""
    table: list = []
    none_row = 0
    len_item = 0
    num_page = ps.num_page * ps.num_cols * ps.num_rows
    num_rows = ps.num_rows
    for i in range(0, num_rows):
        for j in range(0, ps.num_cols):
            indx = j + ps.num_cols * i + num_page
            slash = ""
            try:
                if os.path.isdir(str(fileListMain[indx])):
                   slash = "/"
                fs_obj = escapeSymbols(fileListMain[indx])
                _, item = os.path.split(fs_obj)
                item = item.replace("\\", "")
                if keys.dirty_mode: print(f"len item = {len(item)}")
                len_item += len(item)
                if modes.path_autocomplete.state or modes.switch_2_nxt_tam.state:
                    len_item = 5
                if len(item) == 1 and not os.path.exists(fs_obj):
                    raise IndexError
                row.append(str(indx) + ":" + item + slash + " " * ps.num_spaces)
            except IndexError:
                none_row += 1
                if keys.dirty_mode: print(f"none row = {none_row}; i,j = {i},{j}")
                row.append(f"{Back.BLACK}{str(indx)}:{' ' * ps.num_spaces}{Style.RESET_ALL}")
                num_rows = i
        if none_row < 3 and len_item > 4:
            table.append(row)
        if num_rows != ps.num_rows:
            break
        row = []
        none_row = 0
    too_short_row = len(table)
    return table, too_short_row
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
    too_short_row = len(table)
    return table, too_short_row
def make_page_of_files2_li(fileListMain: list, ps: page_struct):
    row: list =[]
    item = ""
    table: list = []
    none_row = 0
    len_item = 0
    num_page = ps.num_page * ps.num_cols * ps.num_rows
    num_rows = ps.num_rows
    for i in range(0, num_rows):
        for j in range(0, ps.num_cols):
            indx = j + ps.num_cols * i + num_page
            slash = ""
            try:
                if os.path.isdir(str(fileListMain[indx])):
                   slash = "/"
                fs_obj = escapeSymbols(fileListMain[indx])
                _, item = os.path.split(fs_obj)
                item = item.replace("\\", "")
                if keys.dirty_mode: print(f"len item = {len(item)}")
                len_item += len(item)
                if modes.path_autocomplete.state:
                    len_item = 5
                if len(item) == 1 and not os.path.exists(fs_obj):
                    raise IndexError
                row.append(str(indx - num_page) + ":" + item + slash + " " * ps.num_spaces)
            except IndexError:
                none_row += 1
                if keys.dirty_mode: print(f"none row = {none_row}; i,j = {i},{j}")
                row.append(f"{Back.BLACK}{str(indx)}:{' ' * ps.num_spaces}{Style.RESET_ALL}")
                num_rows = i
        if none_row < 3 and len_item > 4:
            table.append(row)
        if num_rows != ps.num_rows:
            break
        row = []
        none_row = 0
    too_short_row = len(table)
    return table, too_short_row

# Threads
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
def checkInt(i) -> bool:
    if str(i)[0] in ('-'):
        return str(i)[1:].isdigit()
    return str(i).isdigit()
def errMsg(msg: str, funcName: str, delay: float|int = -1):
    """if not checkInt(delay):
        achtung(f"delay has to be int in errMsg(), {str(type(delay))}")
        return"""
    if delay == -1:
        print(f"{Fore.RED}{funcName} said: {msg}{Style.RESET_ALL}")
    else:
        full_length = len(var_4_hotKeys.prnt) + len(var_4_hotKeys.prompt)
        msg = f"{Fore.RED}{funcName} said: {msg}{Style.RESET_ALL}"
        clear_cmd_line("", "", full_length)
        writeInput_str(msg, "")
        time.sleep(delay)
        writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt, full_length)
def errMsg_dbg(msg: str, funcName: str, delay: float|int = -1):
    if not checkArg("-dbg"): return
    if delay == -1:
        print(f"{Fore.RED}{funcName} said: {msg}{Style.RESET_ALL}")
    else:
        full_length = len(var_4_hotKeys.prnt) + len(var_4_hotKeys.prompt)
        msg = f"{Fore.RED}{funcName} said: {msg}{Style.RESET_ALL}"
        clear_cmd_line("", "", full_length)
        writeInput_str(msg, "")
        time.sleep(delay)
        writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt, full_length)
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
    if keys.dirty_mode: print(f"\nprobe write for _r {pipes.outNorm_r.read()} pipes.outNorm_r.fileno ={pipes.outNorm_r.fileno()} ")
    prev_pos = 0
    cur_pos = 1
    for path in iter(pipes.outNorm_r.readline, b''):
        if path == pipes.stop:
            break
        if path !="": globalLists.fileListMain0.append(path)
        prev_pos = cur_pos
        cur_pos = pipes.outNorm_r.tell()
    lapse.read_midway_data_from_pipes_stop = time.time_ns()
    globalLists.fileListMain = list(set(globalLists.fileListMain0))
    achtung(f"{len(globalLists.fileListMain)=}")
    if keys.dirty_mode:
        print(f"{funcName} exited")
def find_files(path: str, pipes: PIPES, in_name: str, tmp_file: str = None):
    funcName = "find_files"
    cmd = [f"find -L '{path}' -type f{in_name} > {pipes.outNorm_w.name};echo '\n{pipes.stop}'"]
    if tmp_file is None:
        cmd = [f"find -L '{path}' -type f{in_name};echo '\n{pipes.stop}'"]

    if keys.dirty_mode: print(f"{funcName} {cmd}")
    lapse.find_files_start = time.time_ns()
    proc = sp.Popen(
        cmd,
        stdout=pipes.outNorm_w,
        stderr=pipes.outErr_w,
        shell=True
        )
    lapse.find_files_stop = time.time_ns()
    if keys.dirty_mode: print(f"{funcName} exited")
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
def checkArg(arg: str) -> bool:
    cmd_len = len(sys.argv)
    for i in range(1, cmd_len):
        key0 = sys.argv[i]
        if key0 == arg:
            return True
    return False
def get_arg_in_cmd(key: str, argv: list = sys.argv) -> str|None:
    cmd_len = len(argv)
    ret: str|None = None
    for i in range(1, cmd_len):
        key0 = argv[i]
        if key0 == key:
            ret = argv[i + 1]
    return ret
def if_no_quotes(num0: int, cmd_len:int) -> str:
    funcName = "if_no_quotes"
    grep0 = ''
    grep_keys = ''
    i0: int
    if keys.dirty_mode: print(f"num0 = {num0}, cmdLen = {cmd_len}, argv = {sys.argv}")
    for i0 in range(num0, cmd_len):
        if sys.argv[i0][0:1] != "-":
           grep0 += f" {sys.argv[i0]}"
        else:
            grep0 = grep0.replace("grep==", "pass==")
            if grep0[1:7] == 'pass==':
                grep0 = grep0[7:]
                grep_keys, grep0 = grep0.split(" ", 2)
            grep0 = f"|grep  {grep_keys} '{grep0[0:len(grep0)]}'"
            if sys.argv[i0] == "-in_name":
                i0 -=1
            return [grep0, i0]
    if keys.dirty_mode: print(f"num0 from if_ = {sys.argv[num0]}")
def put_in_name() -> str:
    funcName = "put_in_name"
    cmd_len = len(sys.argv)
    final_grep = ""
    grep0 = ""
    num0 = []
    i = []
    i0 = 1
    i.append(i0)
    while i0 < cmd_len:
        if sys.argv[i0] == "-in_name":
            i0 = i0 + 1
            tmp = if_no_quotes(i0, cmd_len)
            if keys.dirty_mode: print(f"tmp {tmp}")
            if tmp is not None:
                final_grep += f" {tmp[0]}"
                i0 = tmp[1]
        i0 += 1
        if keys.dirty_mode: print(f"{funcName} i0 = {i0} final_grep = {final_grep}")
    return final_grep
def create_or_updateMainList(mod = None) -> None:
    if var_4_hotKeys.prnt == "hot reload":
        loaded: bool = False
        try:
            if checkArg("-no-pkg"): raise ImportError
            import sark0y_tam
            loaded = True
        except ModuleNotFoundError: pass
        except ImportError: pass
        try:
            if loaded: raise ModuleNotFoundError
            import subTern as subtern
        except ModuleNotFoundError: pass
        try:
            if loaded: raise ModuleNotFoundError
            import tam as tam
        except ModuleNotFoundError: pass
        except ImportError: pass
        from importlib import reload
        from importlib.machinery import SourceFileLoader
        if loaded:
            errMsg_dbg("sark0y_tam to reload", "TAM")
            sark0y_tam = sys.modules["sark0y_tam"]
            tam_desc: str = f"{sark0y_tam}"
            path_2_tam: str = re.findall("/.*sark0y_tam/", tam_desc)[0]
            errMsg_dbg(f"{sark0y_tam}... {path_2_tam}", "TAM")
            os.system(f"rm -f {path_2_tam}__pycache__/*")
            subtern = SourceFileLoader("_subTern", f"{path_2_tam}_subTern.py").load_module()
            tam = SourceFileLoader("_tam", f"{path_2_tam}_tam.py").load_module()
            errMsg_dbg(f"{tam.info_struct.rev}", "TAM")
        else:
            subtern = reload(subtern)
            tam = reload(tam)
        tam.globalLists = copy.copy(globalLists)
        tam.kCodes = copy.copy(kCodes)
        var = copy.copy(keys.вар)
        tam.keys = copy.copy(keys)
        keys.вар = copy.copy(var)
        tam.var_4_hotKeys = copy.copy(var_4_hotKeys)
        tam.modes = copy.copy(modes)
        tam.page_struct = copy.copy(page_struct)
        try: tam.manage_pages(tam.globalLists.fileListMain, copy.copy(tmp.ps))
        except AttributeError: pass
        return
    argv: list = sys.argv
    if checkArg("-argv0"):
                print(f"argv = {sys.argv}")
                sys.exit()
    base_path: str = get_arg_in_cmd("-path0", argv)
    filter_name = put_in_name()
    if filter_name is None:
        filter_name = "*"
    if base_path is None:
        base_path = "./"
    globalLists.bkp = globalLists.fileListMain0 = globalLists.fileListMain = []
    achtung(f"'{globalLists.filtered}'")
    tmp_file = get_arg_in_cmd("-tmp_file", argv)
    outNorm, outErr = get_fd(tmp_file)
    tmp_file = None
    if checkArg("-dirty"): print(f"IDs: norm = {outNorm}, err = {outErr}")
    pipes = PIPES(outNorm, outErr)
    thr_find_files: Thread = thr.Thread(target=find_files, args=(base_path, pipes, filter_name, tmp_file))
    thr_find_files.start()
    thr_read_midway_data_from_pipes: Thread = thr.Thread(target=read_midway_data_from_pipes, args=(pipes, globalLists.fileListMain))
    thr_read_midway_data_from_pipes.start()
            #time.sleep(3)
            #thr_find_files.join()
            #thr_read_midway_data_from_pipes.join()
    delta_4_entries = f"Δt for entry points of find_files() & read_midway_data_from_pipes(): {lapse.find_files_start - lapse.read_midway_data_from_pipes_start} ns"
    if checkArg("-dirty"): 
        print(delta_4_entries)
        print(f"len of list = {len(globalLists.fileListMain)}")
    ps = page_struct()
    cols = get_arg_in_cmd("-cols", argv)
    rows = get_arg_in_cmd("-rows", argv)
    col_w = get_arg_in_cmd("-col_w", argv)
    if rows: page_struct.num_rows = ps.num_rows = int(rows)
    if cols: page_struct.num_cols = ps.num_cols = int(cols)
    if col_w: page_struct.col_width = ps.col_width = int(col_w)
    ps.c2r = childs2run()
    ps.c2r = init_view(ps.c2r)
    manage_pages(globalLists.fileListMain, ps)
def cmd():
    ps1: ps0 = ps0()
    del ps1
    if checkArg("-ver") or checkArg("--version"):
        info()
    if checkArg("-title-mark"): Markers.console_title = get_arg_in_cmd("-title-mark")
    if checkArg("-prefix-title-mark"): Markers.console_title_pefix = f"{get_arg_in_cmd('-prefix-title-mark')}"
    subtern.init_user_logs()
    var_4_hotKeys.prnt = ""
    if checkArg("-dirty"):
        keys.dirty_mode = True
    sys.argv.append("-!") # Stop code
    print(f"argv = {sys.argv}")
    SetDefaultKonsoleTitle()
    sys.argv[0] = str(sys.argv)
   # self_recursion()
    cmd_len = len(sys.argv)
    cmd_key = ''
    cmd_val = ''
    num_of_samples = 1
    argv = copy.copy(sys.argv)
    for i in range(1, cmd_len):
        cmd_key = sys.argv[i]
        if cmd_key == "-ver":
            info()
        if "-argv0" == cmd_key:
            if keys.dirty_mode: print(f"argv = {sys.argv}")
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
            create_or_updateMainList()
#pressKey()
if __name__ == "__main__":
    cmd()