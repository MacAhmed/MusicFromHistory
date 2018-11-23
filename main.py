import parsehistory
import os, sys, csv
import urllib.request
import json


def download_mp3(youtube_url):
    
    os.system("youtube-dl --extract-audio --audio-format mp3 " + youtube_url + ' -o "tracks/%(title)s.mp3"')

def isMusicVideo(youtube_url):
    video_info = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/videos?id=" + youtube_url.split('=')[1] + "&part=snippet%20&key=AIzaSyCntMIdOn5qtr5l5P9LIHKRGeiIZJg147Q").read()
    json_video_info = json.loads(video_info.decode('utf-8'))
    try :
        print(json_video_info['items'][0]['snippet']['title'] + " - " + json_video_info['items'][0]['snippet']['categoryId'])
        title = json_video_info['items'][0]['snippet']['title']
        categoryId = json_video_info['items'][0]['snippet']['categoryId']

        if(categoryId == '10' or ('song' in title.lower() and not 'songs' in title.lower()) or 'soundtrack' in title.lower() ):
            return True
    except IndexError as ex:
        return False
    return False


def main():
    output = 'youtube-data-4.csv'
    parsehistory.readHistory_getURLs('History', output)
    if not os.path.exists("tracks"): os.makedirs('tracks')

    with open(output) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            print('Downloading ... ' + row[0])
            if( isMusicVideo(row[0]) ):
                download_mp3(row[0])

    # TODO : Add history functionality, not download songs already downloaded
    # TODO : Rename songs correctly and mp3 info updated

main()