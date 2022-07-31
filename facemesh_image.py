import cv2
import mediapipe as mp
from helper import *
from get_measurement import *


def facemesh_image(images):
    """Takes a list of static image filesnames and returns measurements
    Parameters:
        images: list of image filenames
    Returns:
        measurements: list of dictionaries of measurements
    """
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_face_mesh = mp.solutions.face_mesh
    drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
    measurements = []
    with mp_face_mesh.FaceMesh(
        static_image_mode=True,
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5) as face_mesh:
        for idx, file in enumerate(images):
            image = cv2.imread(file)
            # Convert the BGR image to RGB before processing.
            results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

            # Print and draw face mesh landmarks on the image.
            if not results.multi_face_landmarks:
                continue
            annotated_image = image.copy()
            for face_landmarks in results.multi_face_landmarks:
            #   print('face_landmarks:', face_landmarks)
                mp_drawing.draw_landmarks(
                    image=annotated_image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_tesselation_style())
                mp_drawing.draw_landmarks(
                    image=annotated_image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_contours_style())
                mp_drawing.draw_landmarks(
                    image=annotated_image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_IRISES,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_iris_connections_style())
            cv2.imwrite('./tmp/annotated_image' + str(idx) + '.png', annotated_image)
            face0_original = results.multi_face_landmarks[0]
            face0 = face0_original.landmark
            curr_measurement = get_measurements(face0, 'annotated_image' + str(idx))
            measurements.append(curr_measurement.measurement_dict)
            curr_measurement.to_json()
            # print(get_measurements(face0))
        return measurements

if __name__ == "__main__":
    facemesh_image(["./sample_images/example_image.jpg", "./sample_images/example_image1.jpg"])