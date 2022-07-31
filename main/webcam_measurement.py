import math
import cv2
import mediapipe as mp
from helper import *
from get_measurement import *
from statistics import summary_statistics
from measurement import MeasurementStatistics

def webcam_measurement(time):
  """Takes in amount of time to run webcam and returns measurement 
  summary statitics
  Parameters:
    time: amount of time in seconds to run the webcam for
  Returns:
    summary_statistics: dictionary of dictionaries of 
      measurement summary statistics
      - key: measurement name (e.g. "cornea10Dx")
      - value: dictionary of measurement summary statistics
        - key: summary statistic name (mean, std, min, max, median, range)
        - value: summary statistic value
  """
  sample_max = math.floor(time * 30)
  measurements = dict()
  sample_num = 0
  mp_drawing = mp.solutions.drawing_utils
  mp_drawing_styles = mp.solutions.drawing_styles
  mp_face_mesh = mp.solutions.face_mesh
  # drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
  cap = cv2.VideoCapture(0)
  with mp_face_mesh.FaceMesh(
      max_num_faces=1,
      refine_landmarks=True,
      min_detection_confidence=0.5,
      min_tracking_confidence=0.5) as face_mesh:
    while cap.isOpened():
      success, image = cap.read()
      if not success:
        print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
        continue

      # To improve performance, optionally mark the image as not writeable to
      # pass by reference.
      image.flags.writeable = False
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      results = face_mesh.process(image)

      # Draw the face mesh annotations on the image.
      image.flags.writeable = True
      image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
      if results.multi_face_landmarks:
          for face_landmarks in results.multi_face_landmarks:
              mp_drawing.draw_landmarks(
                  image=image,
                  landmark_list=face_landmarks,
                  connections=mp_face_mesh.FACEMESH_TESSELATION,
                  landmark_drawing_spec=None,
                  connection_drawing_spec=mp_drawing_styles
                  .get_default_face_mesh_tesselation_style())
              mp_drawing.draw_landmarks(
                  image=image,
                  landmark_list=face_landmarks,
                  connections=mp_face_mesh.FACEMESH_CONTOURS,
                  landmark_drawing_spec=None,
                  connection_drawing_spec=mp_drawing_styles
                  .get_default_face_mesh_contours_style())
              mp_drawing.draw_landmarks(
                  image=image,
                  landmark_list=face_landmarks,
                  connections=mp_face_mesh.FACEMESH_IRISES,
                  landmark_drawing_spec=None,
                  connection_drawing_spec=mp_drawing_styles
                  .get_default_face_mesh_iris_connections_style())
          
          face0_original = results.multi_face_landmarks[0]
          face0 = face0_original.landmark
          curr_measurent = get_measurements(face0).measurement_dict
          # print(curr_measurent)
          if sample_num == 0:
             for key in curr_measurent.keys():
              measurements[key] = [curr_measurent[key]]
          else:
            for key in curr_measurent.keys():
              measurements[key].append(curr_measurent[key])
          sample_num += 1
          if sample_num == sample_max:
            break
      # Flip the image horizontally for a selfie-view display.
          cv2.imshow('MediaPipe Face Mesh', cv2.flip(image, 1))
          
      if cv2.waitKey(5) & 0xFF == 27:
        break

  measurement_statistics = dict()
  for measurement in measurements.keys():
    measurement_statistics[measurement] = summary_statistics(measurements[measurement])
  # print(measurement_statistics)
  cap.release()
  measurement_statistics = MeasurementStatistics(measurement_statistics)
  measurement_statistics.to_json()
  return measurement_statistics.measurement_dict

if __name__ == "__main__":
    webcam_measurement(5)
