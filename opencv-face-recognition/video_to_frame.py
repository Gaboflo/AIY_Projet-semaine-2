# USAGE
# python video_to_frame.py --videoset videoset

# import the necessary packages
from imutils import paths
import argparse
import cv2
import os

def process_videos(videoPaths, dataset_path):
    for (i, videoPath) in enumerate(videoPaths):
        # extract the person name from the image path
        print("[INFO] processing video {}/{}".format(i + 1,len(videoPaths)))
        namemp4 = videoPath.split(os.path.sep)[-1]
        name = namemp4[:-4]

        # Playing video from file:
        cap = cv2.VideoCapture(videoPath)
        try:
            if not os.path.exists(os.path.join(dataset_path, name)):
                os.makedirs(os.path.join(dataset_path, name))
        except OSError:
            print ('Error: Creating directory of data')

        currentFrame = 0
        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            if not ret:
                print("Done")
                break
            # Saves image of the current frame in jpg file
            nam = './' + dataset_path + '/' + name + '/frame' + str(currentFrame) + '.jpg'
            print ('Creating...' + nam)
            cv2.imwrite(nam, frame)

            # To stop duplicate images
            currentFrame += 1
        # When everything done, release the capture
        cap.release()

def main():
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--videoset", required=True,
        help="path to input directory of videos ")
    args = vars(ap.parse_args())

    videoPaths = list(paths.list_files(args['videoset'], validExts=(".mp4"), contains=None))
    dataset_path = 'dataset2'

    process_videos(videoPaths, dataset_path)

if __name__ == "__main___":
    main()
