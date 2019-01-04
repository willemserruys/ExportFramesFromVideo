import sys
from cv2 import cv2
import configparser

def extractImages():
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
        vidcap = cv2.VideoCapture(config['DEFAULT']['Video'])
        length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        if length==0:
            raise Exception('video path is not valid')
        fps = 30
        frames = int(config['DEFAULT']['Frames'])
        if frames > length:
            print(str(frames) + ' frames is more than the amount of frames in video (' + str(length) + '). This amount will be used.')
            frames = length
        incrementTime = fps* length/frames
        success,image = vidcap.read()
        success = True
        count = 0
        currentTime = incrementTime
        print("Generating... ")
        while success:
          vidcap.set(cv2.CAP_PROP_POS_MSEC,(currentTime))    # added this line
          success,image = vidcap.read()
          if success:
              cv2.imwrite( config['DEFAULT']['PathOut'] + "\\frame%d.jpg" % count, image)     # save frame as JPEG file
              count = count + 1
              currentTime = currentTime+incrementTime
        print(str(count) + ' frames generated')
    except Exception as inst:
        print(inst)
          
extractImages()

input('Press enter to continue... ')
