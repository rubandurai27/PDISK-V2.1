from moviepy.editor import *

    
# loading video dsa gfg intro video  

clip = VideoFileClip("./public/VID-20210417-WA0003.mp4")  

     
# getting only first 5 seconds  

clips = clip.subclip(0, 15)  

print (clips)
# cutting out some part from the clip 

#clip = clip.cutout(3, 10) 

  
# showing  clip  

#clip.ipython_display(width = 360)
