# MusicFromHistory

## Introduction
My main source of music is YouTube. Its where I discover new tracks and listen to old ones. I find Spotify and other music streaming services to not be as good as this since I am familiar with YouTube channels that post good music and can reguarly check those.

## Problem
The problem I am faced with is that I don't have that music on my phone when I am in a car or commuting etc. This is because I would have to look for that music on Spotify etc, but I don't remember what music I was listening to, and I don't often have cell service so cannot rely on streaming all the time. Also, It can get pretty expensive for me to keep streaming new music. 

## Solution
The solution I came up with was to read my Chrome history, see how many views I have on a video, and then dowload those songs. I then manually transfer those songs onto my phone ( a planned feature to do this automatically ).

## How to use
1. Clone this project to a directory of your choice
2. Find the Chrome History file:

Windows 10 : `C:\Users\[UserName]\AppData\Local\Google\Chrome\User Data\Default`  
Mac: `~/Library/Application Support/Google/Chrome/Default/History`

3. Open a command terminal and Run `python3 main.py [path_to_history_file]`

The program:
1. Creates a temp file to store all the URLs that could be music
2. Downloads all music in a `tracks` folder
3. At termination, the temp file is deleted.

## To Do
- Rename songs correctly, add cover art, and other info etc.
- Convert to a Spotify Playlist
