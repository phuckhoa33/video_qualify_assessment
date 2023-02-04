from tkinter import *
from tkVideoPlayer import TkinterVideo
from tkinter import filedialog as fd
from contentAssessment.video_to_text import from_video_to_file
from contentAssessment.wordsAssessment import validate_swear_words
from imageClassfication.getImageFromVideo import getImages
import threading
import imageio
from PIL import Image, ImageTk

root = Tk()


def setting_for_interface():
    root.geometry("1000x500")
    root.maxsize(1000, 500)
    root.minsize(1000, 500)
    root.title("Video Qualify Assessment")


def setting_for_video_position():
    ## Choose video 
    filename = fd.askopenfilename()

    ## Display video 
    videoplayer = TkinterVideo(master=root, scaled=True)
    videoplayer.load(f"{filename}")
    videoplayer.pack(expand=True, side=LEFT)

    play_video_thread = threading.Thread(target=videoplayer.play, args=())
    play_video_thread.start()
    check_video_quality_thread = threading.Thread(target=check_video_quality, args=(filename))
    check_video_quality_thread.start()
    
def read_and_assess_content(path_name):
    informed_label = Label(root, text='')
    informed_label.pack()
    checkable = validate_swear_words(path_name)
    if checkable:
        informed_label.configure(text="This video has good quality")
    else:
        informed_label.configure(text="This video has bad quality")
def check_video_quality(filename):
    from_video_to_file(filename)
    getImages(filename)
    
    read_and_assess_content("contentAssessment/readContent/recognized.txt")
def Home():
    # Setting for frame about size, color,..
    setting_for_interface()
    open_file_button = Button(root, text='Choose video file', command=setting_for_video_position)
    open_file_button.pack(side='left')
    
    root.mainloop()
Home()