#!/usr/bin/env python3
import subprocess, os

def main():
  layer1()
  layer2()
  layer3()
  layer4()
  dns()

def layer1():
  out = os.fsdecode(subprocess.check_output(['ip', '-br', 'link', 'show']))
  print(esc('1;31')  + '\nLayer 1 - Interfaces with physical address.\n' + esc(0) + out)

def layer2():
  out = os.fsdecode(subprocess.check_output(['ip', 'neighbor', 'show']))
  print(esc('1;31') + 'Layer 2 - Address resolution protocol (ARP) table.\n'+ esc(0) + out)

def layer3():
  out = os.fsdecode(subprocess.check_output(['ip', '-4', '-br', 'address']))
  out1 = os.fsdecode(subprocess.check_output(['ip', 'route', 'show']))
  print(esc('1;31') + 'Layer 3 - Network intefaces with Ip address and Route table.\n' + esc(0) + out)
  print(out1)

def layer4():
  out = os.fsdecode(subprocess.check_output(['ss', '-nl4']))
  print(esc('1;31') + 'Layer 4 - TCP and UDP listening sockets.\n' + esc(0) + out)

def dns():
  try:
    out = os.fsdecode(subprocess.check_output(['nslookup', 'google.com']))
    print(esc('1;31') + 'Layer 7 - DNS test to google.com\n' + esc(0) + out)
  except Exception:
    print('Is nslookup installed?')

def esc(code):
  return f'\033[{code}m'


if __name__=='__main__':
      main()
