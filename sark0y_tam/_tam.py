import random
import re
import subprocess
from tabulate import tabulate
import sys, os, signal
import click
import keyboard as kbd
import time
from threading import Thread
import fcntl
import numpy as np
import subprocess as sp, copy, threading as thr
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from colorama import Back
#MAIN
class info_struct:
    ver = 1
    rev = "7-39"
    author = "Evgeney Knyazhev (SarK0Y)"
    year = '2023'
    telega = "https://t.me/+N_TdOq7Ui2ZiOTM6"
stopCode = "∇\n"
class globalLists:
    stopCode = globals()["stopCode"]
    fileListMain: list
class childs2run:
    running: list = []
    viewer: list = []
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
class tst:
    class subtst:
        h = 1
        class lvl2:
            h = 0
class keys:
    tst.subtst.h = tst.subtst.lvl2.h
    dirty_mode = False
    rename_file_mode = 0
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
    copyfile_msg: str = ""
    fileName: str = ""
    fileIndx: int
    full_length: int
    ENTER_MODE = False
# Terminals
def handleENTER(fileName: str) -> str:
    funcName = "handleENTER"
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
        IsFile = None
        try:
            IsFile = os.path.isfile(getFileNameFromCMD(var_4_hotKeys.prnt))
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
    if var_4_hotKeys.prnt == "Yeah I do":
        var_4_hotKeys.prompt = ' ' * len(var_4_hotKeys.prompt)
        var_4_hotKeys.prnt = ' ' * len(var_4_hotKeys.prnt)
        writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt)
        var_4_hotKeys.prnt = var_4_hotKeys.save_prnt_to_copy_file
        var_4_hotKeys.prompt = var_4_hotKeys.save_prompt_to_copy_file
        var_4_hotKeys.save_prompt_to_copy_file = var_4_hotKeys.save_prnt_to_copy_file = ''
        copyFile(fileName, var_4_hotKeys.prnt, dontInsert=True)
        writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt)
        var_4_hotKeys.ENTER_MODE = False
        return f"go2 {page_struct.num_page}"
    if var_4_hotKeys.prnt == "Yeah, kill this file":
        var_4_hotKeys.prompt = ' ' * len(var_4_hotKeys.prompt)
        var_4_hotKeys.prnt = ' ' * len(var_4_hotKeys.prnt)
        writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt)
        var_4_hotKeys.prnt = var_4_hotKeys.save_prnt_to_copy_file
        var_4_hotKeys.prompt = var_4_hotKeys.save_prompt_to_copy_file
        var_4_hotKeys.save_prompt_to_copy_file = var_4_hotKeys.save_prnt_to_copy_file = ''
        delFile(fileName, var_4_hotKeys.prnt, dontDelFromTableJustMark=page_struct.dontDelFromTableJustMark)
        writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt)
        var_4_hotKeys.ENTER_MODE = False
        return f"go2 {page_struct.num_page}"
    if var_4_hotKeys.prnt == "no":
        var_4_hotKeys.prnt = var_4_hotKeys.save_prnt_to_copy_file
        var_4_hotKeys.prompt = var_4_hotKeys.save_prompt_to_copy_file
        var_4_hotKeys.save_prompt_to_copy_file = ''
        var_4_hotKeys.save_prnt_to_copy_file = ''
        writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt)
        var_4_hotKeys.ENTER_MODE = False
        return f"go2 {page_struct.num_page}"
    return var_4_hotKeys.prnt
def handleTAB(prompt: str):
    ptrn = re.compile('ren\s+\d+|cp\s+\d+', re.IGNORECASE | re.UNICODE)
    regex_result = ptrn.search(var_4_hotKeys.prnt)
    if keys.dirty_mode: print(f"{regex_result.group(0)}, {len(regex_result.group(0))}, {var_4_hotKeys.prnt}")
    if regex_result:
        if len(var_4_hotKeys.prnt_short) == 0:
            var_4_hotKeys.fileName, var_4_hotKeys.fileIndx = regex_result.group(0).split()
            var_4_hotKeys.fileName = globalLists.fileListMain[int(var_4_hotKeys.fileIndx)]
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
        var_4_hotKeys.full_length = len(var_4_hotKeys.prnt)
        writeInput_str(prompt, var_4_hotKeys.prnt, len(var_4_hotKeys.prnt_full))
def flushInputBuffer():
    page_struct.left_shift_4_cur = 0
    page_struct.cur_cur_pos = 0
    return ""
def apostrophe_split(str0: str, delim: str) -> str:
    bulks = str0.split(delim)
    strLoc = ''
    for i in range(0, len(bulks)):
        strLoc += f"{bulks[i]}\{delim}"
    strLoc = strLoc[:-2]
    return strLoc

def escapeSymbols(name: str, symbIndx = -1):
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
        name = name.replace("{", "\{")
        name = name.replace("}", "\}")
        name = name.replace("(", "\(")
        name = name.replace(")", "\)")
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
    cmd = cmd[4:]
    getFileIndx = re.compile('\d+\s+')
    fileIndx = getFileIndx.match(cmd)
    cmd = cmd.replace(fileIndx.group(0), '')
    old_name = globalLists.fileListMain[int(fileIndx.group(0))]
    res = re.match('\/', cmd)
    if not res:
        fileName = old_name
        fileName, _ = os.path.split(fileName)
        fileName += f"/{cmd}"
    else:
        fileName = f"{cmd}"
    globalLists.fileListMain[int(fileIndx.group(0))] = fileName
    fileName = escapeSymbols(fileName)
    old_name = escapeSymbols(old_name)
    if_path_not_existed, _ = os.path.split(fileName)
    cmd = f"mkdir -p {if_path_not_existed}"
    os.system(cmd)
    cmd = "mv -f --backup " + f'{old_name}' + " " + f'{fileName}'
    if os.path.exists(fileName):
        achtung(f"{fileName} doesnt exist\n cmd ={cmd}")
    sp.Popen([cmd,], shell=True)
    return
def getFileNameFromCMD_byIndx(cmd: str):
    cmd = cmd[3:]
    getFileIndx = re.compile('\d+')
    fileIndx = getFileIndx.match(cmd)
    fileName = globalLists.fileListMain[int(fileIndx.group(0))]
    if fileName[-1] == "\n":
        fileName = fileName[:-1]
    return fileName
def getFileNameFromCMD(cmd: str):
    cmd = cmd[3:]
    getFileIndx = re.compile('\d+\s+')
    fileIndx = getFileIndx.match(cmd)
    cmd = cmd.replace(fileIndx.group(0), '')
    old_name = globalLists.fileListMain[int(fileIndx.group(0))]
    res = re.match('\/', cmd)
    if not res:
        fileName = old_name
        fileName, _ = os.path.split(fileName)
        fileName += f"/{cmd}"
    else:
        fileName = f"{cmd}"
    return fileName
def delFile(fileName: str, cmd: str, dontDelFromTableJustMark = True):
    cmd = cmd[3:]
    getFileIndx = re.compile('\d+')
    fileIndx = getFileIndx.match(cmd)
    fileName = globalLists.fileListMain[int(fileIndx.group(0))]
    fileName = escapeSymbols(fileName)
    cmd = "rm -f " + f"{fileName}"
    os.system(cmd)
    heyFile = os.path.exists(fileName)
    if False == heyFile and dontDelFromTableJustMark == False:
        globalLists.fileListMain.remove(int(fileIndx.group(0)))
    if not heyFile and dontDelFromTableJustMark:
        globalLists.fileListMain[int(fileIndx.group(0))] = f"{globalLists.fileListMain[int(fileIndx.group(0))]}::D"
    return
def copyFile(fileName: str, cmd: str, dontInsert = False):
    cmd = cmd[3:]
    getFileIndx = re.compile('\d+\s+')
    fileIndx = getFileIndx.match(cmd)
    cmd = cmd.replace(fileIndx.group(0), '')
    old_name = globalLists.fileListMain[int(fileIndx.group(0))]
    res = re.match('\/', cmd)
    if not res:
        fileName = old_name
        fileName, _ = os.path.split(fileName)
        fileName += f"/{cmd}"
    else:
        fileName = f"{cmd}"
        if not dontInsert:
            globalLists.fileListMain.insert(int(fileIndx.group(0)), fileName)
    fileName = escapeSymbols(fileName)
    old_name = escapeSymbols(old_name)
    if_path_not_existed, _ = os.path.split(fileName)
    cmd = f"mkdir -p {if_path_not_existed}"
    os.system(cmd)
    cmd = "cp -f " + f"{old_name}" + " " + f"{fileName}"
    os.system(cmd)
    return
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
def hotKeys(prompt: str) -> str:
    full_length = 0
    var_4_hotKeys.prnt = ""
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
    ENTER = 13
    BACKSPACE = 127
    ESCAPE = 27
    TAB = 9
    DELETE = "\x1b[3~"
    F12 = "\x1b[24~"
    LEFT_ARROW = "\x1b[D"
    RIGHT_ARROW = "\x1b[C"
    UP_ARROW = "\x1b[A"
    DOWN_ARROW = "\x1b[B"
    while True:
        Key = click.getchar()
        if F12 == Key:
            full_length = len(var_4_hotKeys.prnt)
            var_4_hotKeys.prnt = flushInputBuffer()
            writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt, full_length)
            continue
        if Key == UP_ARROW:
            return "np"
        if Key == DOWN_ARROW:
            return "pp"
        if Key == RIGHT_ARROW:
            if page_struct.left_shift_4_cur > 0:
                page_struct.left_shift_4_cur -= 1
                page_struct.cur_cur_pos = page_struct.cur_cur_pos + 1
                print('\033[C', end='', flush=True)
            continue
        if Key == LEFT_ARROW:
            if page_struct.cur_cur_pos > 0:
                page_struct.left_shift_4_cur += 1
                page_struct.cur_cur_pos = page_struct.cur_cur_pos - 1
                print('\033[D', end='', flush=True)
            continue
        if ENTER == ord0(Key):
            ret = var_4_hotKeys.prnt
            if not var_4_hotKeys.ENTER_MODE:
                var_4_hotKeys.save_prnt = var_4_hotKeys.prnt
                var_4_hotKeys.save_prompt = var_4_hotKeys.prompt
                ret = handleENTER(fileName)
                try:
                    var_4_hotKeys.prnt = ""
                    page_struct.left_shift_4_cur = 0
                    page_struct.cur_cur_pos = 0
                except AttributeError:
                    var_4_hotKeys.ENTER_MODE = False
            else:
                var_4_hotKeys.prnt = var_4_hotKeys.prnt
                ret = handleENTER(fileName)
            if "cont" == ret:
                continue
            var_4_hotKeys.prompt = var_4_hotKeys.save_prompt
            var_4_hotKeys.prnt = ret
            return var_4_hotKeys.prnt
        if DELETE == Key:
            if page_struct.left_shift_4_cur == 0:
                continue
            else:
                var_4_hotKeys.prnt = var_4_hotKeys.prnt[:len(var_4_hotKeys.prnt) - page_struct.left_shift_4_cur + 1] + var_4_hotKeys.prnt[len(var_4_hotKeys.prnt) - page_struct.left_shift_4_cur + 2:]
            if page_struct.left_shift_4_cur > 0:
                page_struct.left_shift_4_cur -= 1
            prnt0 = var_4_hotKeys.prnt
            full_length = len(var_4_hotKeys.prnt)
            writeInput_str(var_4_hotKeys.prompt, prnt0)
            continue
        if BACKSPACE == ord0(Key):
            if page_struct.left_shift_4_cur == 0:
                var_4_hotKeys.prnt = var_4_hotKeys.prnt[:len(var_4_hotKeys.prnt) - 1]
            else:
                var_4_hotKeys.prnt = var_4_hotKeys.prnt[:len(var_4_hotKeys.prnt) - page_struct.left_shift_4_cur - 1] + var_4_hotKeys.prnt[len(var_4_hotKeys.prnt) - page_struct.left_shift_4_cur:]
            if page_struct.cur_cur_pos > 0:
                page_struct.cur_cur_pos = page_struct.cur_cur_pos - 1
            prnt0 = var_4_hotKeys.prnt
            full_length = len(var_4_hotKeys.prnt)
            writeInput_str(var_4_hotKeys.prompt, prnt0)
            continue
        if ESCAPE == ord0(Key): SYS(), sys.exit(0)
        if TAB == ord0(Key):
            var_4_hotKeys.prnt_full = prnt_full
            var_4_hotKeys.fileIndx = fileIndx
            var_4_hotKeys.prnt_short = prnt_short
            var_4_hotKeys.full_length = full_length
            handleTAB(prompt)
            prnt_full = var_4_hotKeys.prnt_full
            fileIndx = var_4_hotKeys.fileIndx
            prnt_short = var_4_hotKeys.prnt_short
            full_length = var_4_hotKeys.full_length
            continue
        else:
            if page_struct.cur_cur_pos + 1 == full_length and page_struct.left_shift_4_cur == 0:
                var_4_hotKeys.prnt += f"{Key}"
            else:
                var_4_hotKeys.prnt =f"{var_4_hotKeys.prnt[:page_struct.cur_cur_pos]}{Key}{var_4_hotKeys.prnt[page_struct.cur_cur_pos:]}"
            page_struct.cur_cur_pos = page_struct.cur_cur_pos + 1
            writeInput_str(var_4_hotKeys.prompt, var_4_hotKeys.prnt)
def custom_input(prompt: str) -> str:
    print(f"{prompt}", end='', flush=True)
    return hotKeys(prompt)
def signal_manager(sig, frame):
    print(f"sig = {sig}")
#signal.signal(signal.CTRL_BREAK_EVENT, signal_manager)
def SYS():
    no_SYS = os.path.exists("/tmp/no_SYS")
    no_SYS1 = get_arg_in_cmd("-SYS", sys.argv)
    if no_SYS == True or no_SYS1 == "1":
        os.system("rm -f /tmp/no_SYS")
        sys.exit(0)
    print("\r\nSee You Soon\nBye.. bye, my Dear User 🙂")
    sys.exit(0)
def SetDefaultKonsoleTitle(addStr = ""):
    out = get_arg_in_cmd("-path0", sys.argv)
    try:
        out += f" {put_in_name()}"
        out = out.replace("'", "")
        print(f"konsole title = {out}")
    except TypeError:
        out = f"cmd is empty {put_in_name()}"
    page_struct.KonsoleTitle = out
    os.system(f"echo -ne '\033]30;{out}{addStr}\007'")
def adjustKonsoleTitle(addStr: str, ps: page_struct):
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
    print(" WWW: https://alg0z.blogspot.com ".center(int(colsize), "◑"))
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
    os.system(f"wall '{msg}'")
def log(msg, num_line: int, funcName: str):
    f = open("/tmp/it.log", mode="w")
    print(f"{funcName} said cmd = {msg} at line: {str(num_line)}", file=f)
def clear_screen():
    if keys.dirty_mode:
        return
    os.system('clear')
def init_view(c2r: childs2run):
    i = 0
    for v in range(1, len(sys.argv)):
        if sys.argv[v] == "-view_w":
            c2r.viewer.append(str(sys.argv[v + 1]))
            c2r.prnt += f"\n  {i}: {c2r.viewer[-1]}"
            i += 1
    return c2r
def run_viewers(c2r: childs2run, fileListMain: list, cmd: str):
    viewer_indx: int = 1
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
    file2run: str = globalLists.fileListMain[file_indx]
    file2run = escapeSymbols(file2run)
    cmd = f'{c2r.viewer[viewer_indx]}'
    cmd_line = f'{c2r.viewer[viewer_indx]}' + ' ' + f"{file2run} > /dev/null 2>&1"
    cmd = [cmd_line,]
    stderr0 = f"/tmp/run_viewers{str(random.random())}"
    stderr0 = open(stderr0, "w+")
    t = sp.Popen(cmd, shell=True, stderr=stderr0)
    if t.stderr is not None:
        os.system(cmd_line)
    if keys.dirty_mode:
        os.system(f"echo '{t.stderr} {t.stdout}' > /tmp/wrong_cmd")
    c2r.running.append(t)

def cmd_page(cmd: str, ps: page_struct, fileListMain: list):
    funcName = "cmd_page"
    lp = len(fileListMain) // (ps.num_cols * ps.num_rows)
    if cmd == "np":
        ps.num_page += 1
        if ps.num_page > lp:
            ps.num_page = lp
        return
    if cmd == "pp":
        if ps.num_page > 0:
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
        try:
            _, file_indx = cmd.split()
            ps.c2r.full_path = f"file {file_indx}\n{str(globalLists.fileListMain[int(file_indx)])}"
        except ValueError:
            errMsg("Type fp <file index>", funcName, 2)
        except IndexError:
            top = len(globalLists.fileListMain) - 2
            errMsg(f"You gave index out of range, acceptable values [0, {top}]", funcName, 2)
        return
    run_viewers(ps.c2r, fileListMain, cmd)
def manage_pages(fileListMain: list, ps: page_struct):
    cmd = ""
    c2r = ps.c2r
    while True:
        try:
            if globalLists.stopCode != globalLists.fileListMain[-1]:
                ps.count_pages = len(globalLists.fileListMain) // (ps.num_cols * ps.num_rows) + 1
                ps.num_files = len(globalLists.fileListMain)
        except IndexError:
            continue
        page_struct.num_page = ps.num_page
        addStr = f" files/pages: {ps.num_files}/{ps.count_pages} p. {ps.num_page}"
        adjustKonsoleTitle(addStr, ps)
        clear_screen()
        print(f"{Fore.RED}      NEWS: {ps.news_bar}\n{Style.RESET_ALL}")
        print(f"Viewers: \n{c2r.prnt}\n\nNumber of files/pages: {ps.num_files}/{ps.count_pages} p. {ps.num_page}\nFull path to {c2r.full_path}")
        table, too_short_row = make_page_of_files2(globalLists.fileListMain, ps)
        if too_short_row == 0:
            ps.num_cols = 2
            table, too_short_row = make_page_of_files2(globalLists.fileListMain, ps)
        try:
            print(tabulate(table, tablefmt="fancy_grid", maxcolwidths=[ps.col_width]))
        except IndexError:
            errMsg("Unfortunately, Nothing has been found.", "TAM")
            SYS()
            sys.exit(-2)
        print(cmd)
        try:
            cmd = custom_input(var_4_hotKeys.prompt)
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
            try:
                _, item = os.path.split(fileListMain[indx])
                if keys.dirty_mode: print(f"len item = {len(item)}")
                len_item += len(item)
                if len(item) == 1:
                    raise IndexError
                row.append(str(indx) + ":" + item + " " * ps.num_spaces)
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
def errMsg(msg: str, funcName: str, delay: int = -1):
    if not checkInt(delay):
        achtung(f"delay has to be int in errMsg(), {str(type(delay))}")
        return
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
    print(f"\nprobe write for _r {pipes.outNorm_r.read()} pipes.outNorm_r.fileno ={pipes.outNorm_r.fileno()} ")
    prev_pos = 0
    cur_pos = 1
    for path in iter(pipes.outNorm_r.readline, b''):
        if path == pipes.stop:
            break
        if path !="":
          fileListMain.append(path)
        prev_pos = cur_pos
        cur_pos = pipes.outNorm_r.tell()
    lapse.read_midway_data_from_pipes_stop = time.time_ns()
    globalLists.fileListMain = set(globalLists.fileListMain)
    globalLists.fileListMain = list(fileListMain)
    if keys.dirty_mode:
        print(f"{funcName} exited")
def find_files(path: str, pipes: PIPES, in_name: str, tmp_file: str = None):
    funcName = "find_files"
    cmd = [f"find -L '{path}' -type f{in_name} > {pipes.outNorm_w.name};echo '\n{pipes.stop}'"]
    if tmp_file is None:
        cmd = [f"find -L '{path}' -type f{in_name};echo '\n{pipes.stop}'"]

    print(f"{funcName} {cmd}")
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
def if_no_quotes(num0: int, cmd_len:int) -> str:
    funcName = "if_no_quotes"
    grep0 = ''
    grep_keys = ''
    i0: int
    print(f"num0 = {num0}, cmdLen = {cmd_len}, argv = {sys.argv}")
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
    print(f"num0 from if_ = {sys.argv[num0]}")
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
            print(f"tmp {tmp}")
            if tmp is not None:
                final_grep += f" {tmp[0]}"
                i0 = tmp[1]
        i0 += 1
        print(f"{funcName} i0 = {i0} final_grep = {final_grep}")
    return final_grep
def cmd():
    if checkArg("-dirty"):
        keys.dirty_mode = True
    sys.argv.append("-!") # Stop code
    print(f"argv = {sys.argv}")
    SetDefaultKonsoleTitle()
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
        if cmd_key == "-ver":
            info()
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
            globalLists.fileListMain = []
            tmp_file = get_arg_in_cmd("-tmp_file", argv)
            outNorm, outErr = get_fd(tmp_file)
            tmp_file = None
            print(f"IDs: norm = {outNorm}, err = {outErr}")
            pipes = PIPES(outNorm, outErr)
            thr_find_files: Thread = thr.Thread(target=find_files, args=(base_path, pipes, filter_name, tmp_file))
            thr_find_files.start()
            thr_read_midway_data_from_pipes: Thread = thr.Thread(target=read_midway_data_from_pipes, args=(pipes, globalLists.fileListMain))
            thr_read_midway_data_from_pipes.start()
            #time.sleep(3)
            #thr_find_files.join()
            #thr_read_midway_data_from_pipes.join()
            delta_4_entries = f"Δt for entry points of find_files() & read_midway_data_from_pipes(): {lapse.find_files_start - lapse.read_midway_data_from_pipes_start} ns"
            вар = 5
            print(delta_4_entries)
            print(f"len of list = {len(globalLists.fileListMain)}")
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
            table = make_page_of_files(globalLists.fileListMain, ps)
            manage_pages(globalLists.fileListMain, ps)
#pressKey()
if __name__ == "__main__":
    cmd()