import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

def distance(p1, p2):
    """Takes two points in R^2 and returns the distance between them."""
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def square(x):
    """Takes a number and returns the square of that number."""
    return x**2

def polygon_area(points):
    """Takes a list of points in R^2 and returns the 
    area of the polygon using shoelace formula
    """
    x = []
    y = []
    for i in points:
        x.append(i[0])
        y.append(i[1])
    correction = x[-1] * y[0] - y[-1]* x[0]
    main_area = np.dot(x[:-1], y[1:]) - np.dot(y[:-1], x[1:])
    return 0.5*np.abs(main_area + correction)

def intersect(p1, p2, p3, p4):
    """Takes four points in R^2 and returns the intersection
    of the two lines defined by the points.
    """
    line1 = [p1, p2]
    line2 = [p3, p4]
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return [x, y]

# For static images:
IMAGE_FILES = []
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
with mp_face_mesh.FaceMesh(
    static_image_mode=True,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5) as face_mesh:
  for idx, file in enumerate(IMAGE_FILES):
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
    cv2.imwrite('/tmp/annotated_image' + str(idx) + '.png', annotated_image)

# For webcam input:
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
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
        boxOD =  {
                    "height": distance((face0[119].x,face0[119].y), (face0[52].x,face0[52].y)),
                    "width": distance([face0[245].x,face0[245].y], [face0[35].x,face0[35].y]),
                    "xMax": face0[245].x,
                    "xMin": face0[35].x,
                    "yMax": face0[119].y,
                    "yMin": face0[52].y,
                        }
        boxOS = {
            "height": distance([face0[348].x,face0[348].y], [face0[282].x,face0[282].y]),
            "width": distance([face0[446].x,face0[446].y], [face0[465].x,face0[465].y]),
            "xMax": face0[446].x,
            "xMin": face0[465].x,
            "yMax": face0[348].y,
            "yMin": face0[282].y,
        }
        # define cornea
        corneaOD = {
            "x": face0[468].x,
            "y": face0[468].y,
            "h1": [face0[469].x,face0[469].y],
            "h2": [face0[471].x,face0[471].y],
            "radius": ( distance([face0[469].x,face0[469].y],
                                [face0[471].x,face0[471].y])  )/2
        }
        corneaOS = {
            "x": face0[473].x,
            "y": face0[473].y,
            "h1": [face0[474].x,face0[474].y],
            "h2": [face0[476].x,face0[476].y],
            "radius": ( distance([face0[474].x,face0[474].y],
                                [face0[476].x,face0[476].y])  )/2
        }
        # define palpebral fissure
        palpebralOD = {
            # points: [
            #     {x:, y:}
            # ],
            "medialCanthus": {"x":face0[133].x, "y":face0[133].y},
            "lateralCanthus": {"x":face0[33].x, "y":face0[33].y},
            "infPoint": {"x":face0[145].x, "y":face0[145].y},
            "supPoint": {"x":face0[159].x, "y":face0[159].y},
            "outline": [ 
                [face0[33].x,face0[33].y],
                [face0[246].x,face0[246].y],
                [face0[161].x,face0[161].y],
                [face0[160].x,face0[160].y],
                [face0[159].x,face0[159].y],
                [face0[158].x,face0[158].y],
                [face0[157].x,face0[157].y],
                [face0[173].x,face0[173].y],
                [face0[133].x,face0[133].y],
                [face0[155].x,face0[155].y],
                [face0[154].x,face0[154].y],
                [face0[153].x,face0[153].y],
                [face0[145].x,face0[145].y],
                [face0[144].x,face0[144].y],
                [face0[163].x,face0[163].y],
                [face0[7].x,face0[7].y]
            ]
        }
        palpebralOS = {
            # points: [
            #     {x:, y:}
            # ],
            "medialCanthus": {"x":face0[362].x, "y":face0[362].y},
            "lateralCanthus": {"x":face0[263].x, "y":face0[263].y},
            "infPoint": {"x":face0[374].x, "y":face0[374].y},
            "supPoint": {"x":face0[386].x, "y":face0[386].y},
            "outline": [ 
                [face0[263].x,face0[263].y],
                [face0[466].x,face0[466].y],
                [face0[388].x,face0[388].y],
                [face0[387].x,face0[387].y],
                [face0[386].x,face0[386].y],
                [face0[385].x,face0[385].y],
                [face0[384].x,face0[384].y],
                [face0[398].x,face0[398].y],
                [face0[362].x,face0[362].y],
                [face0[382].x,face0[382].y],
                [face0[381].x,face0[381].y],
                [face0[380].x,face0[380].y],
                [face0[374].x,face0[374].y],
                [face0[373].x,face0[373].y],
                [face0[390].x,face0[390].y],
                [face0[249].x,face0[249].y]
            ]
        }

        # scaleFactor: au to mm, scaleFactor2 au^2 to mm^2. Average OD and OS cornea for 2 samples
        corneaRadius = 5.855 # white to white = 11.71mm doi: 10.1097/01.ico.0000148312.01805.53
        scaleFactor = ((corneaOD["radius"] / corneaRadius) + (corneaOS["radius"] / corneaRadius))/2
        scaleFactor2 = ((square(corneaOD["radius"]) / square(corneaRadius)) + (square(corneaOS["radius"]) / square(corneaRadius)))/2

        # Calculated measures
        # Use distance from intersect between mid corneal horizontal line and sup-inf PF line and sup or inf PF point for MRD1/MRD2
        MidCornealIntersectOD = intersect(corneaOD["h1"], corneaOD["h2"], [palpebralOD["supPoint"]["x"], palpebralOD["supPoint"]["y"]], [palpebralOD["infPoint"]["x"], palpebralOD["infPoint"]["y"]])
        mrd1OD = distance(MidCornealIntersectOD,
                        [palpebralOD["supPoint"]["x"], palpebralOD["supPoint"]["y"]])
        mrd2OD = distance(MidCornealIntersectOD,
                        [palpebralOD["infPoint"]["x"],palpebralOD["infPoint"]["y"]])
        pfhOD = distance([palpebralOD["infPoint"]["x"],palpebralOD["infPoint"]["y"]],
                        [palpebralOD["supPoint"]["x"],palpebralOD["supPoint"]["y"]])
        pfwOD = distance([palpebralOD["medialCanthus"]["x"],palpebralOD["medialCanthus"]["y"]],
                        [palpebralOD["lateralCanthus"]["x"],palpebralOD["lateralCanthus"]["y"]])
        pfaOD = polygon_area(palpebralOD["outline"])

        MidCornealIntersectOS = intersect(corneaOS["h1"], corneaOS["h2"], [palpebralOS["supPoint"]["x"], palpebralOS["supPoint"]["y"]], [palpebralOS["infPoint"]["x"], palpebralOS["infPoint"]["y"]])
        mrd1OS = distance(MidCornealIntersectOS,
                        [palpebralOS["supPoint"]["x"], palpebralOS["supPoint"]["y"]])
        mrd2OS = distance(MidCornealIntersectOS,
                        [palpebralOS["infPoint"]["x"],palpebralOS["infPoint"]["y"]])
        pfhOS = distance([palpebralOS["infPoint"]["x"],palpebralOS["infPoint"]["y"]],
                        [palpebralOS["supPoint"]["x"],palpebralOS["supPoint"]["y"]])
        pfwOS = distance([palpebralOS["medialCanthus"]["x"],palpebralOS["medialCanthus"]["y"]],
                        [palpebralOS["lateralCanthus"]["x"],palpebralOS["lateralCanthus"]["y"]])
        pfaOS = polygon_area(palpebralOS["outline"])

        ipd = distance(MidCornealIntersectOD, MidCornealIntersectOS)
        innerCanthal = distance([palpebralOS["medialCanthus"]["x"], palpebralOS["medialCanthus"]["y"]],
                                [palpebralOD["medialCanthus"]["x"], palpebralOD["medialCanthus"]["y"]])
        outerCanthal = distance([palpebralOS["lateralCanthus"]["x"], palpebralOS["lateralCanthus"]["y"]],
                                [palpebralOD["lateralCanthus"]["x"], palpebralOD["lateralCanthus"]["y"]])
        morphometryResults = {
        # canvas: canvasCtx,
        "scaleFactor": scaleFactor,
        # calculated values
        "mrd1OD": mrd1OD/scaleFactor,
        "mrd2OD": mrd2OD/scaleFactor,
        "pfhOD": pfhOD/scaleFactor,
        "pfwOD": pfwOD/scaleFactor,
        "pfaOD": pfaOD/scaleFactor2,

        "mrd1OS": mrd1OS/scaleFactor,
        "mrd2OS": mrd2OS/scaleFactor,
        "pfhOS": pfhOS/scaleFactor,
        "pfwOS": pfwOS/scaleFactor,
        "pfaOS": pfaOS/scaleFactor2,

        "ipd": ipd/scaleFactor,
        "innerCanthal": innerCanthal/scaleFactor,
        "outerCanthal": outerCanthal/scaleFactor,
        # points
        "faceMesh": face0_original,
        "boxOD": boxOD,
        "boxOS": boxOS,
        "corneaOD": corneaOD,
        "corneaOS": corneaOS,
        "palpebralOD": palpebralOD,
        "palpebralOS": palpebralOS
    }
    print(morphometryResults)
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Face Mesh', cv2.flip(image, 1))


    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()