#!/usr/bin/env python3
import subprocess, re, os
from datetime import datetime

def main():
  systime()
  sysuptime()
  sessions()
  loadavg()
  users()
  storage()

def systime():
  time = datetime.now()
  print("")
  print(esc('1;34') + ' System Time: '+ esc(0)  + time.strftime('%I:%M %p'))

def sysuptime():
  output = os.fsdecode(subprocess.check_output(['uptime', '-p']))
  sysuptime = re.search(r"up\s(.*)" , output).group(1)
  print(esc('1;34') + ' System\'s been up for:' + esc(0), sysuptime)

def sessions():
  output = os.fsdecode(subprocess.check_output('uptime'))
  out = re.search(r"(\d+)\s+users", output).group(1)
  print(esc('1;34') + ' Number of active user sessions: ' + esc(0), out + ' user sessions')

def loadavg():
  output = os.fsdecode(subprocess.check_output('uptime'))
  load = re.search(r"(load average):(.*)", output).group(2)
  print(esc('1;34') + ' Load average for last 1, 5 and 15 minutes:' + esc(0), load + '\n')

def users():
  output = str.splitlines(os.fsdecode(subprocess.check_output(['w', '-h'])))
  print(esc('1;34') + " List of logged in users and what they're doing." + esc(0))
  for line in output:
    print(" " + line)
  print('')

def storage():
  output = str.splitlines(os.fsdecode(subprocess.check_output(['lsblk', '-fm', '-o' 'NAME,' 'FSTYPE,' 'FSAVAIL,' 'FSUSE%,' 'MOUNTPOINT,' 'SIZE,' 'OWNER,' 'GROUP,' 'MODE', '-e 7'])))

  print(esc('1;34') + " List of drives, partitions, and details" + esc(0))
  for line in output:
    print(" " + line)
  print('')

def esc(code):
  return f'\033[{code}m'

if __name__=='__main__':
      main()
