import ftplib

from ftplib import FTP

import urllib

import time

import os

import re



def urlify(s):

     s=s[:-4]

     # Remove all non-word characters (everything except numbers and letters)

     s = re.sub(r"[^\w\s]", '', s)

     # Replace all runs of whitespace with a single dash

     s = re.sub(r"\s+", '_', s)

     return s+'.mp4'

def get_latest_dir(which_dir):

 ftp = FTP('203.X.X.X') #IP of the FTP server from which we are going to download the file

 ftp.login()

 data = []

 ftp.cwd(which_dir)

 ftp.dir(data.append)

 curent_date = time.strftime("%m-%d-%y") #Latest videos to be downloaded you can also change the date manually to 01-28-2015 to 
                                         #to download videos for a specific date

 directory_name = []

 for line in data:

  if curent_date == line[:8]:

    directory_name.append(line.rsplit('  ',1)[1])

 return directory_name 

s = []

s = get_latest_dir('/')

print s

sub =[]

for char in s:

  sub.append(get_latest_dir(char))

sub = sum(sub,[])  


for i in range(len(s)):

 filenames = ftp.nlst('/'+s[i]+'/'+sub[i]) # get filenames within the directory


 print filenames

 ftp.cwd('/'+s[i]+'/'+sub[i])



 for filename in filenames:
    #Create a path and download all the videos on that path 
    # below is the windows path to which the videos will be dowloaded you can change it to 
    # whatever path you want
    pth = r'H:\oct18\\'

    if not os.path.exists(pth):

         os.makedirs(pth)

    local_filename = os.path.join(pth, urlify(filename.rsplit('/',1)[1]))

    file = open(local_filename, 'wb')
    #This will download the mp4 files and save it at the path
    ftp.retrbinary('RETR '+ filename.rsplit('/',1)[1], file.write)

    file.close()

ftp.quit()
