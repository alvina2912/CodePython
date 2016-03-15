import Tkinter
import Image, ImageTk

# open a SPIDER image and convert to byte format
im = Image.open('weather-1.jpg').convert2byte()

root = Tkinter.Tk()
# A root window for displaying objects

 # Convert the Image object into a TkPhoto object
tkimage = ImageTk.PhotoImage(im)

Tkinter.Label(root, image=tkimage).pack()
# Put it in the display window

root.mainloop() # Start the GUI
