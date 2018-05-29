
# This python script contains functions to make videos from set of plots and also from a plot function.
# The created movie can be published within jupyter notebook using the function "Watch Movie"
# Author : Adekunle Ajayi

# - Load Modules
import os, sys
import matplotlib.pyplot as plt
import io
import base64
from IPython.display import HTML

#-Create movie from a plot function
def Make_Movie_From_Plot_Function(plot_function,frame_number,image_name,image_index,movie_name, fps=10):
    '''This function create movies from a plot function with a precise number of iteration : NumOfFrame.
        fps : frequency per seconds.
        frame_number : Number of interation
        image_name : Image first name . as in eta_0023 => first name = eta_
        image_index : indexing used to define image as in eta_0023 => image_index = 4
        %04d : the index for the image, you can change this to the format on you images
    '''
    for i in range(frame_number):
        plot_function(i)
        name_dummy = image_name+"%0"+str(image_index)+"d.png"
        file_name = name_dummy%i
        plt.savefig(file_name)
        plt.clf()
    os.system("rm "+ movie_name + ".mp4") # - Remove previously generated movie with the same name
    os.system("ffmpeg -r "+str(fps)+" -b 1800 -i " +image_name+"%0"+str(image_index)+"d.png "+ movie_name + ".mp4")
    os.system("rm " + image_name+"*.png") # - Delete all used images


#-Create movie from set of existing plots
def Make_Movie_From_Images(image_path,image_name,image_index,movie_name,fps=10):
    '''
        This function creates a movie from already produced images.
        The movie is stored in the same folder as the images with .mp4 extention
        image_path : the path to the folder containg the images.
        image_name : Image first name . as in eta_0023 => first name = eta_
        image_index : indexing used to define image as in eta_0023 => image_index = 4
        movie_name : intended name for the movie.
        fps : frequency per seconds
        %04d : the index for the image, you can change this to the format on you images
    '''
    os.system("rm "+ movie_name + ".mp4") # - Remove previously generated movie with the same name
    os.system("ffmpeg -r "+str(fps)+" -b 1800 -i " + image_path+image_name+"%0"+str(image_index)+"d.png "+ movie_name + ".mp4")

#-Watch the video
def Watch_Movie(video_path) :
    ''' This function load an Mp4 movie in a jupyter notebook'''
    video = io.open(video_path, 'r+b').read()
    encoded = base64.b64encode(video)
    return HTML(data='''<video alt="test" controls> <source src="data:video/mp4;base64,{0}" type="video/mp4" /></video>'''.format(encoded.decode('ascii')))
