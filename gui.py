import PySimpleGUI as sg
from pytube import YouTube
from pytube.cli import on_progress

def Download(url, quality, path):
    try:
        video=YouTube(url, on_progress_callback=on_progress)
        streams=video.streams.all()
        qualityList={}
        for stream in streams:
            if stream.mime_type=='video/mp4'and stream.is_progressive==False:
                qualityList[stream.resolution]=stream.itag
        return qualityList
        
    except EOFError as err:
        print(err)
    else:
        print('Done!')

# Define the window's contents
qualityList=['1080p','720p','480p','360p','240p','144p']
layout = [[sg.Text("Enter video URL :")],
          [sg.Input(key='URL')],
          [sg.Text('Select path to store :')],
          [sg.Input(key='FILEPATH'), sg.FolderBrowse()],
          [sg.Combo(qualityList,'Readonly', size = (20,4), enable_events=False, key='QUALITY', change_submits=True)],
          [sg.Text(size=(40,10), key='OUTPUT')],
          [sg.Button('Download'), sg.Button('Quit')]]

window = sg.Window('Youtube Downloader', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    url=values['URL']
    quality = values['QUALITY']
    path=values['FILEPATH']
    window['FILEPATH'].update(path)

    video=YouTube(url)
    streams=video.streams.all()
    qualityAvail={}
    for stream in streams:
            if stream.mime_type=='video/mp4'and stream.is_progressive==False:
                qualityAvail[stream.resolution.strip()]=stream.itag
    if quality not in qualityAvail.keys():
        qualPrint='\n-> '.join([str(k) for k in qualityAvail.keys()])
        window['OUTPUT'].update('Selected video quality is not available for this video. \nSelect another. Available :\n->'+qualPrint)



window.close()