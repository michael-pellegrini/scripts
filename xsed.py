#!/usr/bin/env python3
import subprocess, re, os

def main():
  substitute()

def substitute():
  print('SED script to replace all occurrences of a pattern in a file.')
  file = input('Enter absolute path to file: ')
  pattern = input('Enter pattern in file that needs replaced: ')
  newpattern = input('Enter new pattern that will replace pattern in file: ')

  output = subprocess.run(['sed', '-i', 's/{0}/{1}/g w /dev/stdout'.format(pattern, newpattern), file], capture_output=True, text=True)
  print('\n' + '*** Displaying the lines that changed. ***\n' + output.stdout)





if __name__=='__main__':
      main()
