import os
import sys
import re
import subprocess as sp
import codecs
class ctlCodes:
    stop = "∇\n"
    class readOutput:
        stopped = 0
        paused = 1
def subTerminal(cmdInput: str) -> dict:
    main, second = os.openpty()
    _, err = os.openpty()
    cmd = [f"{cmdInput};echo {ctlCodes.stop}", ]
    proc = sp.Popen(cmd, stderr=err, stdout=second, stdin=second, shell=True)
    #~red = codecs.decode(os.read(main, 4096))
    #print(red)
    return {"err": err, "out": second, "in": second, "main": main}
def readOutput(out) -> int:
    #out = open("hh")
    red = os.read(out, 4096)
    while(red != ctlCodes.stop):
        try:
            red = codecs.decode(red)
        except TypeError:
            pass
        if red == "":
            return ctlCodes.readOutput.paused
        print(red)
        red = os.read(out, 4096)
    return ctlCodes.readOutput.stopped
def control_subTerm(cmd: str) -> None:
    dict_f = subTerminal(cmd)
    while True:
        if readOutput(dict_f["main"]) == ctlCodes.readOutput.stopped:
            cmd = input("Please, enter Your command: ")
            if cmd == "qqq0":
                break
            if ctlCodes.readOutput.paused:
                os.write(dict_f["main"])
    return
def srch_pkgs():
    return
def main() -> None:
    cmd = input("Please, enter Your cmd: ")
    control_subTerm(cmd)
main()