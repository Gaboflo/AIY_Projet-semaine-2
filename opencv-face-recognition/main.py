# python main.py --videoset videoset --dataset dataset2
#  --embeddings output/embeddings.pickle --detector face_detection_model --embeddingmodel openface_nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle

import argparse
from imutils import paths

from video_to_frame import process_videos
from extract_embeddings import extract_embeddings
from train_model import train_model

def create_database(videoPaths, dataset_path, embeddings_path, detector_path, embemodel_path, confidence_path, data_path,recognizer_path, le_path ):
    # Process videos
    process_videos(videoPaths, dataset_path)

    # Extract embeddings and update pickle files
    extract_embeddings ( embeddings_path , detector_path, embemodel_path, confidence_path, data_path )

    # train model and update le.pickle file
    train_model (recognizer_path, embeddings_path, le_path)

    print("All Done.")

def main():
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--videoset", required=True,
        help="path to input directory of videos ")
    ap.add_argument("-t", "--dataset", required=True, help="path to input directory of faces + images")
    ap.add_argument("-e", "--embeddings", required=True, help="path to output serialized db of facial embeddings")
    ap.add_argument("-d", "--detector", required=True, help="path to OpenCV's deep learning face detector")
    ap.add_argument("-m", "--embeddingmodel", required=True, help="path to OpenCV's deep learning face embedding model")
    ap.add_argument("-c", "--confidence", type=float, default=0.5, help="minimum probability to filter weak detections")
    ap.add_argument("-r", "--recognizer", required=True, help="path to output model trained to recognize faces")
    ap.add_argument("-l", "--le", required=True, help="path to output label encoder")
    args = vars(ap.parse_args())

    #Process each video and write image to dataset folders.
    videoPaths = list(paths.list_files(args['videoset'], validExts=(".mp4"), contains=None))
    dataset_path = args['dataset']
    embeddings_path = args['embeddings']
    detector_path = args['detector']
    embemodel_path = args['embeddingmodel']
    confidence_path = args['confidence']
    recognizer_path = args['recognizer']
    le_path = args['le']

    create_database(videoPaths, dataset_path, embeddings_path, detector_path, embemodel_path, confidence_path, dataset_path,recognizer_path, le_path )




if __name__ == "__main__":
    main()

