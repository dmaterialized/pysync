# test idea
# a way to prompt for path and initiate a connection

import time, copy
import shutil, os, subprocess

ip="#"
# ultimately replace the below with import of a settings file.
 # with open('settings.xml','r'):
profile1="Elysium"
profile2="TimeMachine"
profile3="Other"

# below is a way to run unix inside python subprocess.
proc = subprocess.Popen(["ls","-la"],
                stdin = subprocess.PIPE,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
                        shell=True)
(out, err) = proc.communicate()

sleepvalue = 0.21
def sleeper(sleeps):
    time.sleep(sleeps)

def dotter(dots):
    tick = 1
    while tick <= dots:
        print(". " * tick)
        sleeper(sleepvalue)
        tick=tick+1

dotter(8)

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
    if ip != "":
        # rsync -rltDWz src/ dest/



<<<<<<< Updated upstream
def connection(profile):
=======

def makeConnection(profile):
>>>>>>> Stashed changes
  print('using profile: '+ profile)
  if profile == "Elysium":
       synchelper(profile)
       print ("making connection!...")
       dotter(16)
       print("Syncing...")

# don't hardcode profile names...

makeConnection(profile)
