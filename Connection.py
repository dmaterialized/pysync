# test idea
# a way to prompt for path and initiate a connection

import time, copy
import shutil, os, subprocess

# below is a way to run unix inside python subprocess.
proc = subprocess.Popen(["ls","-la"],
                stdin = subprocess.PIPE,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
                        shell=True)
(out, err) = proc.communicate()

sleepvalue = 0.2
def sleeper(sleeps):
    time.sleep(sleeps)

def dotter(dots):
    #pass dotter(5) as example
    tick = 1
    while tick <= dots:
        print(". "*tick)
        sleeper(sleepvalue)
        tick=tick+1

dotter(4)

ip="#"
# ultimately replace the below with import of a settings file.
 # with open('settings.xml','r'):
profile1="Elysium"
profile2="TimeMachine"
profile3="Other"
profile=input("please pick a profile: "+profile1+", "+profile2+", "+profile3+": ")

def synchelper(profile):
    # for now, use Elysium as default
    profile=profile1
    print("syncHelper started.")
    if profile=="Elysium":
        ip="192.168.100.14"
        print("using IP address: "+ip)
    else:
        ip=input("please enter the IP address")





def connection(profile):
  print ("making connection!...")
  print(".")
  sleeper(0.25)
  print("..")
  sleeper(0.25)
  print("...")
  sleeper(0.25)
  print("....")
  sleeper(0.25)
  print(".....")
  sleeper(0.25)
  print("......")
  sleeper(0.25)
  print('using profile: '+ profile)
  if profile == "Elysium":
      # needs a counter
       synchelper(profile)
       print("Syncing...")


# and go.
connection(profile)
