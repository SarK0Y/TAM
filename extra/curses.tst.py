import curses
import sys
def Main(screen):
   #p = input("enter smth: ")
   for line in sys.stdin:
    # Remove trailing newline characters using strip()
    if 'exit' == line.strip():
        print('Found exit. Terminating the program')
        exit(0)
    else:
        print('Message from sys.stdin: ---> {} <---'.format(line))
   while True:
      ch = screen.getch()
      print("yst")
      if ch == ord('q'):
         break
      elif ch == 27: # ALT was pressed
         screen.nodelay(True)
         ch2 = screen.getch() # get the key pressed after ALT
         if ch2 == -1:
            break
         else:
            screen.addstr(5, 5, 'ALT+'+str(ch2))
            screen.refresh()
         screen.nodelay(False)

#curses.wrapper(Main)
Main("hhhh")