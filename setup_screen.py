# setup screen
from tkinter import *
from PIL import Image, ImageTk

from pygame import mixer
mixer.init()

# window = Tk()
# window.mainloop()

# creating class
class musicplayer:
    def __init__(self, Tk):
        self.root = Tk
        self.root.title('Music_Player')
        self.root.configure(background = 'black')
        self.root.geometry('400x400')

        # menubar
        # self.menubar = Menu(self.root)
        # self.root.configure(menu = self.menubar)

        # self.submenu = Menu(self.menubar)
        # self.menubar.add_cascade(label= 'File', menu = self.submenu)

        # adding label
        self.label = Label(text='lets make it!', bg = 'black', fg="white", font=22).place(x=55, y = 15)

        # adding leftside image
        # L = left
        self.L_photo = ImageTk.PhotoImage(file = 'leftsideimage.png')
        L_photo = Label(self.root, image = self.L_photo, bg = 'black').place(x=680,y=80)


        # adding img
        self.photo = ImageTk.PhotoImage(file = 'mainimg.png')
        photo = Label(self.root, image=self.photo, bg='black').place(x=100, y=50)

        # adding label
        self.label1 = Label(text='The best feeling is getting lost in music', bg = 'magenta', fg="white", font=22)
        self.label1.pack(side=BOTTOM, fill=X)

        # song = ['theClimb.mp3','lovelyXmas.mp3']
        # i = 0
        # while(i<len(song)):
            # sway = print(song[i])
        # functions
        def playmusic() :
                try:
                    paused
                except NameError:
                    try:
                      mixer.music.load('theClimb.mp3')
                      mixer.music.play()
                      self.label1['text'] = 'Music Playing...'
                    except:
                      pass
                else:
                  mixer.music.unpause()
                  self.label1['text'] = 'Music Playing...'
        
            

        # creating buttons
        # creating play button
        self.photo_B1 = ImageTk.PhotoImage(file='playbutton.png')
        photo_B1 = Button(self.root, image=self.photo_B1, bd=0,bg='black',command= playmusic).place(x=40,y=525)

        # func pause button
        def pausemusic() :
              global paused

              paused = TRUE
              mixer.music.pause()
              self.label1['text'] = 'Music Paused'


        # pause button
        self.photo_B2 = ImageTk.PhotoImage(file='pausebutton.png')
        photo_B2 = Button(self.root, image=self.photo_B2, bd=0,bg='black', command=pausemusic).place(x=150,y=530)

        # function stopbutton
        def stopmusic() :
               mixer.music.stop()
               self.label1['text'] = 'Music Stopped'

        # stop button
        self.photo_B3 = ImageTk.PhotoImage(file='stopbutton.png')
        photo_B3 = Button(self.root, image=self.photo_B3, bd=0,bg='black', command= stopmusic).place(x=240,y=525)
        
        # def restart():
        #   # restart button
        #   self.restart = ImageTk.PhotoImage(file = 'restartbutton.png')
        #   restart = Button(self.root, image=self.restart, bd=0, bg='black', command= playmusic).place(x=300, y=500
        #   )

        
        # mute func
        def mute():
              self.scale.set(0)
              self.mute = ImageTk.PhotoImage(file = 'mute.png')
              mute = Button(self.root, image=self.mute, bd=0,bg='black', command=unmute).place(x=892,y=557)
              self.label1['text']='Music Muted'
        
        # unmute func
        def unmute():
              self.scale.set(25)
              self.volimage = ImageTk.PhotoImage(file ='volimg.png')
              volimage = Button(self.root, image=self.volimage, bd=0,bg='black', command=mute).place(x=890,y=558)
              self.label1['text']='Music Playing...'

        # vol img
        self.volimage = ImageTk.PhotoImage(file ='volimg.png')
        volimage = Button(self.root, image=self.volimage, bd=0,bg='black', command=mute).place(x=890,y=558)

        # vol function
        def volume(vol):
              volume = int(vol)/100
              mixer.music.set_volume(volume)


        # volume bar
        self.scale = Scale(self.root, from_=0, to=100, length=300, bd=0,bg='orange', width=4, orient=HORIZONTAL, command=volume)
        self.scale.set(25)
        self.scale.place(x=950, y=570)

    
root = Tk()
obj = musicplayer(root)
root.mainloop()