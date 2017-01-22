# linkextractor
## Description
linkextractor is a small Python script that will extract all links from a jDownloader 2 file list. jDownloader 2 does not support exporting all links as plain text at the moment.

## What linkextractor does
It will read in all of your links from jDownloader that are stored in seperate files in an archive called 'downloadList*.zip' and write all links in separate lines into a file called 'linklist.txt'.

## Prerequisites
linkextractor has been tested with Python 2.7 and requires an existing Python 2.7 install. If you haven't installed Python on your system, get it directly at the [Python Website](https://www.python.org/).

linkextractor uses the two standard libraries 'os' and 'json'.

## Installation
Clone the repository into a new directory or just download the file 'getlinks.py' and copy it into a new directory. 

## Get Information from jDownloader2
jDownloader 2 stores all information in a separate directory called 'config'. You will find this directory in your jDownloader installation directory.

If you look into this directory you will find a lot of files called downloadListXXX.zip. Be sure to close jDownloader2 before proceeding.

Find the latest downloadListXXX.zip file. Extract all files into the directory that you have created before and that has the file getlinks.py included.

Your directory should now contain several files called '0000' and '0000_00' and so on, as well as 'getlinks.py'.

## Run the programme

Open a terminal. On Windows you can do this by pressing 'WinKey + R' and then type 'cmd' and 'Enter'.

Change to the respective directory using the 'cd' command.

Once in the directory, run 'python getlinks.py'. 

Once done, you will find a new file called 'linklist.txt' in this directory. When you open it, you will find all links from your download. 

This file will be overwritten if you run the programme again.

You can now import them to another jDownloader 2 by copy + pasting the links.
