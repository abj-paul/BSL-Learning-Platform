from model_lib import *
import joblib
from collectData import *


activities = joblib.load("labels.joblib")
model = get_neural_model(activities)[0]
model.load_weights("trained_activity_model.h5")

def dummy_testing():
    dataset, outputs = load_activity_data(activities)
    print(dataset[0].shape)
    print(model.predict(np.expand_dims(dataset[0], axis=0)))


# Live Testing
def live_testing_continuous():
    videoCaptureObject = cv2.VideoCapture(VIDEO_STREAM_LINK)
    EVERY_N_FRAME = 3
    STARTING_FRAME = 100
    numOfSamples = 30


    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        numOfFrames = 0
        captured_activity = []
        predictedActivity = "No activity"
        while True:
            success, frame = videoCaptureObject.read()
            if not success:
                print(f"Error reading frames from video stream " + VIDEO_STREAM_LINK)
                break
            
            if numOfFrames % 29 == 0 and numOfFrames!=0:
                predictedActivity = activities[np.argmax(model.predict(np.expand_dims(captured_activity, axis=0)))]
                print(predictedActivity)
            keypointImage, keypoints = get_keypoints(frame, holistic)
            captured_activity.append(keypoints)
            numOfFrames+=1

            cv2.putText(keypointImage, f"{predictedActivity}", (0,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,255), 1)
            cv2.imshow("Testing BSL", keypointImage)
            if cv2.waitKey(1) == ord('q'):
                videoCaptureObject.release()
                cv2.destroyAllWindows()
                break
    return


def live_testing(framesPerSample):
    videoCaptureObject = cv2.VideoCapture(VIDEO_STREAM_LINK)
    EVERY_N_FRAME = 3
    STARTING_FRAME = 100

    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        cv2.waitKey(3000)
        infinite = True
        while infinite:
            predictedActivity= "No Activity"
            frame_number = 0
            saved_frame_number = 0
            captured_activity = []
            while True:
                success, frame = videoCaptureObject.read()
                if not success:
                    print(f"Error reading frames from videostream {VIDEO_STREAM_LINK}")
                    break

                if STARTING_FRAME!=0:
                    cv2.putText(frame, f"{predictedActivity}", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2)
                    STARTING_FRAME-=1
                    cv2.imshow("Testing BSL Activity", frame)
                    frame_number = 0

                elif frame_number%EVERY_N_FRAME==0: 
                    keypointImage, keypoints = get_keypoints(frame, holistic)
                    cv2.putText(keypointImage, f"COLLECTING ACTIVITY FRAME {frame_number}", (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,255), 2)
                    
                    cv2.imshow("Testing BSL Activity", keypointImage)
                    captured_activity.append(keypoints)
                    saved_frame_number+=1

       
                if saved_frame_number >= framesPerSample:
                    predictedActivity = activities[np.argmax(model.predict(np.expand_dims(captured_activity, axis=0)))]
                    print(predictedActivity)
                    STARTING_FRAME = 300
                    frame_number = 0
                    saved_frame_number = 0
                         
                if cv2.waitKey(1) == ord('q'): 
                    videoCaptureObject.release()
                    cv2.destroyAllWindows()
                    infinite = False
                    break
                frame_number+=1

live_testing(framesPerSample = 29)