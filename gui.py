import PySimpleGUI as sg
from pytube import YouTube
from pytube.cli import on_progress

def Download(url, qualityList, path):
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
layout = [[sg.Text("Enter video URL :")],
          [sg.Input(key='INPUT')],
          [sg.Text('Select path to store :')],
          [sg.Input(key='FILEPATH'), sg.FolderBrowse()],
          [sg.Combo(qualityList, size = (20,4), enable_events=False, key='QUALITY', change_submits=True)],
          [sg.Text(size=(40,1), key='OUTPUT')],
          [sg.Button('Download'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Youtube Downloader', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    #window['OUTPUT'].update('Hello ' + values['INPUT'] + "! Thanks for trying PySimpleGUI") 
    
    #update the dropdown value
    quality = values['QUALITY']
    path=values['FILEPATH']
    window['FILEPATH'].update(path)

# Finish up by removing from the screen
window.close()