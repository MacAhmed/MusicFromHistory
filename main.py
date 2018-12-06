import parsehistory, db
import os, sys, csv
import urllib.request
import json
import datetime


def download_mp3(youtube_url):
    if( not db.haveDownloaded('videos.db', youtube_url) ):
        os.system("youtube-dl --extract-audio --audio-format mp3 " + youtube_url + ' -o "tracks/%(title)s.mp3"')
    else:
        print("Not Downloading as already Downloaded once!")

def isMusicVideo(youtube_url):
    now = datetime.datetime.now()
    video_id = youtube_url.split('=')[1]
    video_info = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/videos?id=" + video_id + "&part=snippet%20&key=AIzaSyCntMIdOn5qtr5l5P9LIHKRGeiIZJg147Q").read()
    json_video_info = json.loads(video_info.decode('utf-8'))
    try :
        title = json_video_info['items'][0]['snippet']['title']
        categoryId = json_video_info['items'][0]['snippet']['categoryId']
        print(title + " - " + categoryId)

        if(categoryId == '10' or ('song' in title.lower() and not 'songs' in title.lower()) or 'soundtrack' in title.lower() ):
            db.saveVideo('videos.db', now.strftime("%d-%m-%Y"), title, video_id, youtube_url )
            return True
    except IndexError as ex:
        return False
    return False


def main():
    output = 'history_cleaned'
    parsehistory.readHistory_getURLs(sys.argv[1], output)
    db.setUp_database('videos.db')
    if not os.path.exists("tracks"): os.makedirs('tracks')
    
    with open(output, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            print('Downloading ... ' + row[0])
            if( isMusicVideo(row[0]) ):
                download_mp3(row[0])

    os.remove('history_cleaned')


main()