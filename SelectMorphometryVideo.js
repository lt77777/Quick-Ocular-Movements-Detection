
import { defineComponent } from "vue";
// import Header from "./Header.vue";
// import {IonPage, IonContent} from '@ionic/vue';
import { cameraOutline, folderOpenOutline, timerOutline } from 'ionicons/icons/index.js';
// import { FaceMesh, FACEMESH_RIGHT_EYE, FACEMESH_RIGHT_EYEBROW, FACEMESH_RIGHT_IRIS, FACEMESH_LEFT_EYE , FACEMESH_LEFT_EYEBROW, FACEMESH_LEFT_IRIS, FACEMESH_FACE_OVAL } from './face_mesh.cjs';
// import { drawConnectors } from '@mediapipe/drawing_utils';
import pkg from '@mediapipe/camera_utils';
const { Camera } = pkg;
// import pkg2 from './face_mesh.cjs';
// const { FaceMesh, FACEMESH_RIGHT_EYE, FACEMESH_RIGHT_EYEBROW, FACEMESH_RIGHT_IRIS, FACEMESH_LEFT_EYE , FACEMESH_LEFT_EYEBROW, FACEMESH_LEFT_IRIS, FACEMESH_FACE_OVAL } = pkg2;
import pkg3 from '@mediapipe/drawing_utils';
const { drawConnectors } = pkg3;
import pkg4 from './face_mesh.cjs';
const { FaceMesh, FACEMESH_RIGHT_EYE, FACEMESH_RIGHT_EYEBROW, FACEMESH_RIGHT_IRIS, FACEMESH_LEFT_EYE , FACEMESH_LEFT_EYEBROW, FACEMESH_LEFT_IRIS, FACEMESH_FACE_OVAL } = pkg4;
import {
  mean, median, std, round, distance, square, intersect
} from 'mathjs';
const area = require('area-polygon')

export default defineComponent({
  name: "SelectMorphometryVideo",
//   components: {
//     Header,
//     IonPage,
//     IonContent
//   },
  
  data() {
      return {
          imageDataOD: "",
          imageDataOS: "",
          computeBtnIsDisabled: true,
          sampleCount: 0,
          sampleMax: 300,
          recordData: [],

          ipd: {},
          innerCanthal: {},
          outerCanthal: {},

          mrd1OD: {},
          mrd2OD: {},
          pfhOD: {},
          pfwOD: {},
          pfaOD: {},

          mrd1OS: {},
          mrd2OS: {},
          pfhOS: {},
          pfwOS: {},
          pfaOS: {},

          camera: {}
      }
      
  },

  setup() {
    // Load icons
      return {
          cameraOutline, folderOpenOutline, timerOutline
      }
  },

  mounted() {
      if (this.$route.name === "SelectMorphometryVideo") {
          this.runVideoMorphometry()
      } 
  },
  beforeRouteLeave (to, from , next) {
    // stop camera before moving to another page
    if (this.camera.camera) {
        this.camera.camera.stop()
        delete this.camera.camera
    }
    next()
    },
  methods: {
      async runVideoMorphometry() {
            const videoElement = document.getElementsByClassName('input_video')[0];
            const canvasElement = document.getElementsByClassName('output_canvas')[0];
            const canvasCtx = canvasElement.getContext('2d');
            
            // Display loading message
            canvasCtx.font = "20px Arial"
            canvasCtx.fillText("Loading...", 30, 50)

            let onResults = function(results) {
            canvasCtx.save();
            canvasCtx.canvas.width = window.innerWidth;
            canvasCtx.canvas.height = window.innerWidth;
            canvasCtx.clearRect(0, 0, canvasElement.width, canvasElement.height);
            canvasCtx.drawImage(
                results.image, 0, 0, canvasElement.width, canvasElement.height);
            if (results.multiFaceLandmarks) {
                // calculate result values
                let face0 = results.multiFaceLandmarks[0]

                if (face0) {  // calculate result values only if a face is present in frame
                    // define eye bounding boxes
                    const boxOD = {
                        height: distance([face0[119]['x'],face0[119]['y']], [face0[52]['x'],face0[52]['y']]),
                        width: distance([face0[245]['x'],face0[245]['y']], [face0[35]['x'],face0[35]['y']]),
                        xMax: face0[245]['x'],
                        xMin: face0[35]['x'],
                        yMax: face0[119]['y'],
                        yMin: face0[52]['y'],
                    }
                    const boxOS = {
                        height: distance([face0[348]['x'],face0[348]['y']], [face0[282]['x'],face0[282]['y']]),
                        width: distance([face0[446]['x'],face0[446]['y']], [face0[465]['x'],face0[465]['y']]),
                        xMax: face0[446]['x'],
                        xMin: face0[465]['x'],
                        yMax: face0[348]['y'],
                        yMin: face0[282]['y'],
                    }
                    // define cornea
                    const corneaOD = {
                        x: face0[468]['x'],
                        y: face0[468]['y'],
                        h1: [face0[469]['x'],face0[469]['y']],
                        h2: [face0[471]['x'],face0[471]['y']],
                        radius: ( distance([face0[469]['x'],face0[469]['y']],
                                           [face0[471]['x'],face0[471]['y']])  )/2
                    }
                    const corneaOS = {
                        x: face0[473]['x'],
                        y: face0[473]['y'],
                        h1: [face0[474]['x'],face0[474]['y']],
                        h2: [face0[476]['x'],face0[476]['y']],
                        radius: ( distance([face0[474]['x'],face0[474]['y']],
                                           [face0[476]['x'],face0[476]['y']])  )/2
                    }
                    // define palpebral fissure
                    const palpebralOD = {
                        // points: [
                        //     {x:, y:}
                        // ],
                        medialCanthus: {x:face0[133]['x'], y:face0[133]['y']},
                        lateralCanthus: {x:face0[33]['x'], y:face0[33]['y']},
                        infPoint: {x:face0[145]['x'], y:face0[145]['y']},
                        supPoint: {x:face0[159]['x'], y:face0[159]['y']},
                        outline: [ 
                            [face0[33]['x'],face0[33]['y']],
                            [face0[246]['x'],face0[246]['y']],
                            [face0[161]['x'],face0[161]['y']],
                            [face0[160]['x'],face0[160]['y']],
                            [face0[159]['x'],face0[159]['y']],
                            [face0[158]['x'],face0[158]['y']],
                            [face0[157]['x'],face0[157]['y']],
                            [face0[173]['x'],face0[173]['y']],
                            [face0[133]['x'],face0[133]['y']],
                            [face0[155]['x'],face0[155]['y']],
                            [face0[154]['x'],face0[154]['y']],
                            [face0[153]['x'],face0[153]['y']],
                            [face0[145]['x'],face0[145]['y']],
                            [face0[144]['x'],face0[144]['y']],
                            [face0[163]['x'],face0[163]['y']],
                            [face0[7]['x'],face0[7]['y']]
                        ]
                    }
                    const palpebralOS = {
                        // points: [
                        //     {x:, y:}
                        // ],
                        medialCanthus: {x:face0[362]['x'], y:face0[362]['y']},
                        lateralCanthus: {x:face0[263]['x'], y:face0[263]['y']},
                        infPoint: {x:face0[374]['x'], y:face0[374]['y']},
                        supPoint: {x:face0[386]['x'], y:face0[386]['y']},
                        outline: [ 
                            [face0[263]['x'],face0[263]['y']],
                            [face0[466]['x'],face0[466]['y']],
                            [face0[388]['x'],face0[388]['y']],
                            [face0[387]['x'],face0[387]['y']],
                            [face0[386]['x'],face0[386]['y']],
                            [face0[385]['x'],face0[385]['y']],
                            [face0[384]['x'],face0[384]['y']],
                            [face0[398]['x'],face0[398]['y']],
                            [face0[362]['x'],face0[362]['y']],
                            [face0[382]['x'],face0[382]['y']],
                            [face0[381]['x'],face0[381]['y']],
                            [face0[380]['x'],face0[380]['y']],
                            [face0[374]['x'],face0[374]['y']],
                            [face0[373]['x'],face0[373]['y']],
                            [face0[390]['x'],face0[390]['y']],
                            [face0[249]['x'],face0[249]['y']]
                        ]
                    }

                    // scaleFactor: au to mm, scaleFactor2 au^2 to mm^2. Average OD and OS cornea for 2 samples
                    const corneaRadius = 5.855 // white to white = 11.71mm doi: 10.1097/01.ico.0000148312.01805.53
                    const scaleFactor = ((corneaOD.radius / corneaRadius) + (corneaOS.radius / corneaRadius))/2
                    const scaleFactor2 = ((square(corneaOD.radius) / square(corneaRadius)) + (square(corneaOS.radius) / square(corneaRadius)))/2

                    // Calculated measures
                    // Use distance from intersect between mid corneal horizontal line and sup-inf PF line and sup or inf PF point for MRD1/MRD2
                    const MidCornealIntersectOD = intersect(corneaOD.h1, corneaOD.h2, Object.values(palpebralOD.supPoint), Object.values(palpebralOD.infPoint))
                    const mrd1OD = distance(MidCornealIntersectOD,
                                            [palpebralOD.supPoint.x, palpebralOD.supPoint.y])
                    const mrd2OD = distance(MidCornealIntersectOD,
                                            [palpebralOD.infPoint.x,palpebralOD.infPoint.y])
                    const pfhOD = distance([palpebralOD.infPoint.x,palpebralOD.infPoint.y],
                                           [palpebralOD.supPoint.x,palpebralOD.supPoint.y])
                    const pfwOD = distance([palpebralOD.medialCanthus.x,palpebralOD.medialCanthus.y],
                                           [palpebralOD.lateralCanthus.x,palpebralOD.lateralCanthus.y])
                    const pfaOD = area(palpebralOD.outline)

                    const MidCornealIntersectOS = intersect(corneaOS.h1, corneaOS.h2, Object.values(palpebralOS.supPoint), Object.values(palpebralOS.infPoint))
                    const mrd1OS = distance(MidCornealIntersectOS,
                                            [palpebralOS.supPoint.x, palpebralOS.supPoint.y])
                    const mrd2OS = distance(MidCornealIntersectOS,
                                            [palpebralOS.infPoint.x,palpebralOS.infPoint.y])
                    const pfhOS = distance([palpebralOS.infPoint.x,palpebralOS.infPoint.y],
                                           [palpebralOS.supPoint.x,palpebralOS.supPoint.y])
                    const pfwOS = distance([palpebralOS.medialCanthus.x,palpebralOS.medialCanthus.y],
                                           [palpebralOS.lateralCanthus.x,palpebralOS.lateralCanthus.y])
                    const pfaOS = area(palpebralOS.outline)

                    const ipd = distance(MidCornealIntersectOD, MidCornealIntersectOS)
                    const innerCanthal = distance([palpebralOS.medialCanthus.x, palpebralOS.medialCanthus.y],
                                                  [palpebralOD.medialCanthus.x, palpebralOD.medialCanthus.y])
                    const outerCanthal = distance([palpebralOS.lateralCanthus.x, palpebralOS.lateralCanthus.y],
                                                  [palpebralOD.lateralCanthus.x, palpebralOD.lateralCanthus.y])

                    const morphometryResults = {
                        // canvas: canvasCtx,
                        scaleFactor: scaleFactor,
                        // calculated values
                        mrd1OD: mrd1OD/scaleFactor,
                        mrd2OD: mrd2OD/scaleFactor,
                        pfhOD: pfhOD/scaleFactor,
                        pfwOD: pfwOD/scaleFactor,
                        pfaOD: pfaOD/scaleFactor2,

                        mrd1OS: mrd1OS/scaleFactor,
                        mrd2OS: mrd2OS/scaleFactor,
                        pfhOS: pfhOS/scaleFactor,
                        pfwOS: pfwOS/scaleFactor,
                        pfaOS: pfaOS/scaleFactor2,

                        ipd: ipd/scaleFactor,
                        innerCanthal: innerCanthal/scaleFactor,
                        outerCanthal: outerCanthal/scaleFactor,
                        // points
                        faceMesh: face0,
                        boxOD: boxOD,
                        boxOS: boxOS,
                        corneaOD: corneaOD,
                        corneaOS: corneaOS,
                        palpebralOD: palpebralOD,
                        palpebralOS: palpebralOS
                    }

                    // log results
                    if (this.sampleCount > 0 ) {
                        this.recordData.push(morphometryResults)
                        console.log(this.recordData)
                        // console.log(this.sampleCount)
                        this.sampleCount += 1

                    }
                    // Calculate and display final results when all samples collected
                    if (this.sampleCount > this.sampleMax) {

                        // log values in array
                        let mrd1ODArray = []
                        let mrd2ODArray = []
                        let pfhODArray = []
                        let pfwODArray = []
                        let pfaODArray = []

                        let mrd1OSArray = []
                        let mrd2OSArray = []
                        let pfhOSArray = []
                        let pfwOSArray = []
                        let pfaOSArray = []

                        let ipdArray = []
                        let innerCanthalArray = []
                        let outerCanthalArray = []
                        for (const sample of this.recordData) {
                            mrd1ODArray.push(sample['mrd1OD'])
                            mrd2ODArray.push(sample['mrd2OD'])
                            pfhODArray.push(sample['pfhOD'])
                            pfwODArray.push(sample['pfwOD'])
                            pfaODArray.push(sample['pfaOD'])

                            mrd1OSArray.push(sample['mrd1OS'])
                            mrd2OSArray.push(sample['mrd2OS'])
                            pfhOSArray.push(sample['pfhOS'])
                            pfwOSArray.push(sample['pfwOS'])
                            pfaOSArray.push(sample['pfaOS'])

                            ipdArray.push(sample['ipd'])
                            innerCanthalArray.push(sample['innerCanthal'])
                            outerCanthalArray.push(sample['outerCanthal'])
                        }

                        // calculate mean/SD
                        // console.log(pfwODArray)
                        //OD
                        // console.log(this.pfwODArray)
                        this.mrd1OD.mean = round(mean(mrd1ODArray),1)
                        this.mrd1OD.median = round(median(mrd1ODArray),1)
                        this.mrd1OD.sd = round(std(mrd1ODArray),1)
                        this.mrd2OD.mean = round(mean(mrd2ODArray),1)
                        this.mrd2OD.median = round(median(mrd2ODArray),1)
                        this.mrd2OD.sd = round(std(mrd2ODArray),1)
                        this.pfhOD.mean = round(mean(pfhODArray),1)
                        this.pfhOD.median = round(median(pfhODArray),1)
                        this.pfhOD.sd = round(std(pfhODArray),1)
                        this.pfwOD.mean = round(mean(pfwODArray),1)
                        this.pfwOD.median = round(median(pfwODArray),1)
                        this.pfwOD.sd = round(std(pfwODArray),1)
                        this.pfaOD.mean = round(mean(pfaODArray),0)
                        this.pfaOD.median = round(median(pfaODArray),0)
                        this.pfaOD.sd = round(std(pfaODArray),0)

                        this.mrd1OS.mean = round(mean(mrd1OSArray),1)
                        this.mrd1OS.median = round(median(mrd1OSArray),1)
                        this.mrd1OS.sd = round(std(mrd1OSArray),1)
                        this.mrd2OS.mean = round(mean(mrd2OSArray),1)
                        this.mrd2OS.median = round(median(mrd2OSArray),1)
                        this.mrd2OS.sd = round(std(mrd2OSArray),1)
                        this.pfhOS.mean = round(mean(pfhOSArray),1)
                        this.pfhOS.median = round(median(pfhOSArray),1)
                        this.pfhOS.sd = round(std(pfhOSArray),1)
                        this.pfwOS.mean = round(mean(pfwOSArray),1)
                        this.pfwOS.median = round(median(pfwOSArray),1)
                        this.pfwOS.sd = round(std(pfwOSArray),1)
                        this.pfaOS.mean = round(mean(pfaOSArray),0)
                        this.pfaOS.median = round(median(pfaOSArray),0)
                        this.pfaOS.sd = round(std(pfaOSArray),0)

                        this.ipd.mean = round(mean(ipdArray),0)
                        this.ipd.median = round(median(ipdArray),0)
                        this.ipd.sd = round(std(ipdArray),0)
                        this.innerCanthal.mean = round(mean(innerCanthalArray),0)
                        this.innerCanthal.median = round(median(innerCanthalArray),0)
                        this.innerCanthal.sd = round(std(innerCanthalArray),1)
                        this.outerCanthal.mean = round(mean(outerCanthalArray),0)
                        this.outerCanthal.median = round(median(outerCanthalArray),0)
                        this.outerCanthal.sd = round(std(outerCanthalArray),1)
                        
                        // console.log(mean(mrd1ODArray))

                        // reset counter
                        window.test = this.recordData
                        this.recordData = []
                        this.sampleCount = 0
                        // console.log(this.recordData)
                    }
                }

                // console.log(FACEMESH_RIGHT_IRIS[3])
                for (const landmarks of results.multiFaceLandmarks) {
                // drawConnectors(canvasCtx, landmarks, FACEMESH_TESSELATION,
                                // {color: '#C0C0C070', lineWidth: 1});
                drawConnectors(canvasCtx, landmarks, FACEMESH_RIGHT_EYE, {color: '#FF0D00', lineWidth:2});
                drawConnectors(canvasCtx, landmarks, FACEMESH_RIGHT_EYEBROW, {color: '#FF0D00', lineWidth:2});
                drawConnectors(canvasCtx, landmarks, FACEMESH_RIGHT_IRIS, {color: '#FF0D00', lineWidth:2});
                drawConnectors(canvasCtx, landmarks, FACEMESH_LEFT_EYE, {color: '#00F2FF', lineWidth:2});
                drawConnectors(canvasCtx, landmarks, FACEMESH_LEFT_EYEBROW, {color: '#00F2FF', lineWidth:2});
                drawConnectors(canvasCtx, landmarks, FACEMESH_LEFT_IRIS, {color: '#00F2FF', lineWidth:2});
                drawConnectors(canvasCtx, landmarks, FACEMESH_FACE_OVAL, {color: '#E0E0E0', lineWidth:2});
                // drawConnectors(canvasCtx, landmarks, FACEMESH_LIPS, {color: '#E0E0E0'});
                }
            }
            canvasCtx.restore();
            }.bind(this)

            const faceMesh = new FaceMesh({locateFile: (file) => {
            return `/models/face_mesh/${file}`;
            }});
            faceMesh.setOptions({
            maxNumFaces: 1,
            refineLandmarks: true,
            minDetectionConfidence: 0.5,
            minTrackingConfidence: 0.5
            });
            faceMesh.onResults(onResults);

            // console.log(this.$route.params.cameraMode)

            // Create Camera
            // console.log('starting camera')
            this.camera.camera = new Camera(videoElement, {
                    onFrame: async () => {
                        await faceMesh.send({image: videoElement});
                    },
                    facingMode: this.$route.params.cameraMode,
                    width: 300,
                    height: 300
                });
            // Start Camera
            this.camera.camera.start();
    },
    async recordResults(nSamples) {
        this.sampleCount = 1
        this.sampleMax = nSamples
        
    },
    gotoPage(pageName) {
      this.$router.push({
        name: pageName,
      });
    },
  },
})
