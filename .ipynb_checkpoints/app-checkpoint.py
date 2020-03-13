import argparse
import cv2
import numpy as np

def get_args():
    '''
    Gets the arguments from the command line.
    '''
    parser = argparse.ArgumentParser("Handle an input stream")
    # -- Create the descriptions for the commands
    i_desc = "The location of the input file"

    # -- Create the arguments
    parser.add_argument("-i", help=i_desc)
    args = parser.parse_args()

    return args


def capture_stream(args):
    ### TODO: Handle image, video or webcam
    #create a flag for image files
    image_flag = False
    # Determine the input, if it is a webcam
    if args.i == 'CAM':
        args.i = 0
    elif args.i.endswith('.jpg') or args.i.endswith('.bmp'):
        image_flag = True
    
    ### TODO: Get and open video capture
    capt = cv2.VideoCapture(args.i)
    capt.open(args.i)
    
    # In case it is video, processing:
    
    if not image_flag:
        # Define the codec and initialize videowriter
        out = cv2.VideoWriter("outvid.mp4", 0x00000021, 30, (100, 100))
    else:
        out = None
    # Create an infinite loop that processes the frames until the video ends
    
    while capt.isOpened():
        # Read the next frame
        
        flag, frame = capt.read()
        if not flag:
            break
        key_pressed = cv2.waitKey(60)
        
        ### TODO: Re-size the frame to 100x100
        frame = cv2.resize(frame, (100,100))
    
        ### TODO: Add Canny Edge Detection to the frame, 
        ###       with min & max values of 100 and 200
        ###       Make sure to use np.dstack after to make a 3-channel image
        
        
        frame = cv2.Canny(frame, 100, 200)
        frame = np.dstack((frame, frame, frame))
        
        ### TODO: Write out the frame, depending on image or video
        if image_flag:
            cv2.imwrite("out_image.jpg", frame)
        else:
            out.write(frame)
        # break if the ESC key is pressed( ESC is 27)
        if  key_pressed == 27:
            break
    
    ### TODO: Close the stream and any windows at the end of the application

    if not image_flag:
            out.release()
    capt.release()
    cv2.destroyAllWindows()
        
def main():
    args = get_args()
    capture_stream(args)


if __name__ == "__main__":
    main()
