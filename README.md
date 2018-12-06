# MusicFromHistory

## Introduction
My main source of music is YouTube. Its where I discover new tracks and listen to old ones. I find Spotify and other music streaming services to not be as good as this since I am familiar with YouTube channels that post good music and can reguarly check those.

## Problem
The problem I am faced with is that I don't have that music on my phone when I am in a car or commuting etc. This is because I would have to look for that music on Spotify etc, but I don't remember what music I was listening to, and I don't often have cell service so cannot rely on streaming all the time. Also, It can get pretty expensive for me to keep streaming new music. 

## Solution
The solution I came up with was to read my history, see how many views I have on a video, and then dowload those songs. I then manually transfer those songs onto my phone ( a planned feature to do this automatically ).

## How to use
First of all, clone this project to a directory of your choice. Second, find the History file for your browser. Currently only supporting Chrome, whose History file can be found at

Windows 10 : `C:\Users\[UserName]\AppData\Local\Google\Chrome\User Data\Default`

Then simply run `python3 main.py [path_to_history]`

The program will create a file to store all the URLs that may be music, and then download all music in a `tracks` folder. At termination, the URLs file will be deleted. 

## To Do
- Rename songs correctly, add cover art, and other info etc.
- Convert to a Spotify Playlist
