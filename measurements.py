from helper import *

def get_measurements(face, face_original): 
    """Takes in face landmark and original face 
    and returns the measurements of the face."""
    face0 = face
    face0_original = face_original
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
    return(morphometryResults)