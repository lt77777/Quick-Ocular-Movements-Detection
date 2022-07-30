<template>
  <ion-page>
    <Header></Header>

    <ion-content overflow-scroll="true">
      <ion-card>
        <video class="input_video"></video>  <!-- for input only, display:none -->
        <canvas class="output_canvas"></canvas> <!-- for display -->
        <ion-card-content> 
            <ion-row>
               <ion-col>
                    <ion-button expand="block" @click="recordResults(60)">
                        <ion-icon :icon="timerOutline" slot="start"></ion-icon><ion-label slot="end">Record 2s</ion-label>
                    </ion-button>
              </ion-col>
              <ion-col>
                    <ion-button expand="block" @click="recordResults(150)">
                        <ion-icon :icon="timerOutline" slot="start"></ion-icon><ion-label slot="end">Record 5s</ion-label>
                    </ion-button>
              </ion-col>
            </ion-row>
            <!-- <ion-row>
                {{ this.$route.params.cameraMode }}
            </ion-row> -->

            <!-- Display sample count while recording -->
            <ion-row v-if="sampleCount" class="ion-text-center">
                <ion-col>
                <ion-text class="ion-text-center">
                    Recording sample {{ sampleCount }} of {{ sampleMax }}
                    </ion-text>
                </ion-col>
            </ion-row>

            <!-- Display results -->
            <!-- OD -->
            <ion-grid class="ion-padding-bottom">
                <ion-row class="ion-align-items-center">
                    <ion-col>
                        <span class='side-title' id='side-title-OD'>OD</span>
                    </ion-col>
                    <ion-col>
                        <strong>Mean</strong>
                    </ion-col>
                    <ion-col>
                        <strong>Median</strong>
                    </ion-col>
                    <ion-col>
                        <strong>SD</strong>
                    </ion-col>
                </ion-row>
                <ion-row>
                    <ion-col>
                        <strong>MRD1</strong>
                    </ion-col>
                    <ion-col>
                        {{ mrd1OD['mean'] }} <span v-if="mrd1OD['mean']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ mrd1OD['median'] }} <span v-if="mrd1OD['median']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ mrd1OD['sd'] }} <span v-if="mrd1OD['sd']">mm</span>
                    </ion-col>
                </ion-row>
                <ion-row>
                    <ion-col>
                        <strong>MRD2</strong>
                    </ion-col>
                    <ion-col>
                        {{ mrd2OD['mean'] }} <span v-if="mrd2OD['mean']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ mrd2OD['median'] }} <span v-if="mrd2OD['median']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ mrd2OD['sd'] }} <span v-if="mrd2OD['sd']">mm</span>
                    </ion-col>
                </ion-row>
                <ion-row>
                    <ion-col>
                        <strong>PF H</strong>
                    </ion-col>
                    <ion-col>
                        {{ pfhOD['mean'] }} <span v-if="pfhOD['mean']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ pfhOD['median'] }} <span v-if="pfhOD['median']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ pfhOD['sd'] }} <span v-if="pfhOD['sd']">mm</span>
                    </ion-col>
                </ion-row>
                <ion-row>
                    <ion-col>
                        <strong>PF W</strong>
                    </ion-col>
                    <ion-col>
                        {{ pfwOD['mean'] }} <span v-if="pfwOD['mean']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ pfwOD['median'] }} <span v-if="pfwOD['median']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ pfwOD['sd'] }} <span v-if="pfwOD['sd']">mm</span>
                    </ion-col>
                </ion-row>
                <ion-row>
                    <ion-col>
                        <strong>PF A</strong>
                    </ion-col>
                    <ion-col>
                        {{ pfaOD['mean'] }} <span v-if="pfaOD['mean']">mm<sup>2</sup></span>
                    </ion-col>
                    <ion-col>
                        {{ pfaOD['median'] }} <span v-if="pfaOD['median']">mm<sup>2</sup></span>
                    </ion-col>
                    <ion-col>
                        {{ pfaOD['sd'] }} <span v-if="pfaOD['sd']">mm<sup>2</sup></span>
                    </ion-col>
                </ion-row>
            </ion-grid>

            <!-- OS -->
            <ion-grid class="ion-padding-bottom">
                <ion-row class="ion-align-items-center">
                    <ion-col>
                        <span class='side-title' id='side-title-OS'>OS</span>
                    </ion-col>
                    <ion-col>
                        <strong>Mean</strong>
                    </ion-col>
                    <ion-col>
                        <strong>Median</strong>
                    </ion-col>
                    <ion-col>
                        <strong>SD</strong>
                    </ion-col>
                </ion-row>
                <ion-row>
                    <ion-col>
                        <strong>MRD1</strong>
                    </ion-col>
                    <ion-col>
                        {{ mrd1OS['mean'] }} <span v-if="mrd1OS['mean']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ mrd1OS['median'] }} <span v-if="mrd1OS['median']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ mrd1OS['sd'] }} <span v-if="mrd1OS['sd']">mm</span>
                    </ion-col>
                </ion-row>
                <ion-row>
                    <ion-col>
                        <strong>MRD2</strong>
                    </ion-col>
                    <ion-col>
                        {{ mrd2OS['mean'] }} <span v-if="mrd2OS['mean']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ mrd2OS['median'] }} <span v-if="mrd2OS['median']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ mrd2OS['sd'] }} <span v-if="mrd2OS['sd']">mm</span>
                    </ion-col>
                </ion-row>
                <ion-row>
                    <ion-col>
                        <strong>PF H</strong>
                    </ion-col>
                    <ion-col>
                        {{ pfhOS['mean'] }} <span v-if="pfhOS['mean']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ pfhOS['median'] }} <span v-if="pfhOS['median']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ pfhOS['sd'] }} <span v-if="pfhOS['sd']">mm</span>
                    </ion-col>
                </ion-row>
                <ion-row>
                    <ion-col>
                        <strong>PF W</strong>
                    </ion-col>
                    <ion-col>
                        {{ pfwOS['mean'] }} <span v-if="pfwOS['mean']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ pfwOS['median'] }} <span v-if="pfwOS['median']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ pfwOS['sd'] }} <span v-if="pfwOS['sd']">mm</span>
                    </ion-col>
                </ion-row>
                <ion-row>
                    <ion-col>
                        <strong>PF A</strong>
                    </ion-col>
                    <ion-col>
                        {{ pfaOS['mean'] }} <span v-if="pfaOS['mean']">mm<sup>2</sup></span>
                    </ion-col>
                    <ion-col>
                        {{ pfaOS['median'] }} <span v-if="pfaOS['median']">mm<sup>2</sup></span>
                    </ion-col>
                    <ion-col>
                        {{ pfaOS['sd'] }} <span v-if="pfaOS['sd']">mm<sup>2</sup></span>
                    </ion-col>
                </ion-row>
            </ion-grid>

            <!-- OU -->
            <ion-grid>
                <ion-row class="ion-align-items-center">
                    <ion-col>
                        <span class='side-title'>OU</span>
                    </ion-col>
                    <ion-col>
                        <strong>Mean</strong>
                    </ion-col>
                    <ion-col>
                        <strong>Median</strong>
                    </ion-col>
                    <ion-col>
                        <strong>SD</strong>
                    </ion-col>
                </ion-row>
                <ion-row class="ion-align-items-center">
                    <ion-col>
                        <strong>ICD</strong>
                    </ion-col>
                    <ion-col>
                        {{ innerCanthal['mean'] }} <span v-if="innerCanthal['mean']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ innerCanthal['median'] }} <span v-if="innerCanthal['median']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ innerCanthal['sd'] }} <span v-if="innerCanthal['sd']">mm</span>
                    </ion-col>
                </ion-row>
                <ion-row class="ion-align-items-center">
                    <ion-col>
                        <strong>OCD</strong>
                    </ion-col>
                    <ion-col>
                        {{ outerCanthal['mean'] }} <span v-if="outerCanthal['mean']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ outerCanthal['median'] }} <span v-if="outerCanthal['median']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ outerCanthal['sd'] }} <span v-if="outerCanthal['sd']">mm</span>
                    </ion-col>
                </ion-row>
                <ion-row class="ion-align-items-center">
                    <ion-col>
                        <strong>IPD</strong>
                    </ion-col>
                    <ion-col>
                        {{ ipd['mean'] }} <span v-if="ipd['mean']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ ipd['median'] }} <span v-if="ipd['median']">mm</span>
                    </ion-col>
                    <ion-col>
                        {{ ipd['sd'] }} <span v-if="ipd['sd']">mm</span>
                    </ion-col>
                </ion-row>
            </ion-grid>


            
        </ion-card-content>
      </ion-card>
      <ion-card>
        <ion-card-header>
            <ion-card-title class='card-title'>Legend</ion-card-title>
        </ion-card-header>
        <ion-card-content>
            <ion-grid>
                <ion-row>
                    <ion-col size='3'>
                        <strong>MRD1</strong>
                    </ion-col>
                    <ion-col size='9'>
                        Margin reflex distance 1
                    </ion-col>
                </ion-row>
                <ion-row>
                    <ion-col size='3'>
                        <strong>MRD2</strong>
                    </ion-col>
                    <ion-col size='9'>
                        Margin reflex distance 2
                    </ion-col>
                </ion-row>
                <ion-row>
                    <ion-col size='3'>
                        <strong>PF H</strong>
                    </ion-col>
                    <ion-col size='9'>
                        Palpebral Fissure Height
                    </ion-col>
                </ion-row>
                <ion-row>
                    <ion-col size='3'>
                        <strong>PF W</strong>
                    </ion-col>
                    <ion-col size='9'>
                        Palpebral Fissure Width
                    </ion-col>
                </ion-row>
                <ion-row>
                    <ion-col size='3'>
                        <strong>PF A</strong>
                    </ion-col>
                    <ion-col size='9'>
                        Palpebral Fissure Area
                    </ion-col>
                </ion-row>
                <ion-row>
                    <ion-col size='3'>
                        <strong>ICD</strong>
                    </ion-col>
                    <ion-col size='9'>
                        Inner Canthal Distance
                    </ion-col>
                </ion-row>
                <ion-row>
                    <ion-col size='3'>
                        <strong>OCD</strong>
                    </ion-col>
                    <ion-col size='9'>
                        Outer Canthal Distance
                    </ion-col>
                </ion-row>
                <ion-row>
                    <ion-col size='3'>
                        <strong>IPD</strong>
                    </ion-col>
                    <ion-col size='9'>
                        Interpupillary distance
                    </ion-col>
                </ion-row>
            </ion-grid>
        </ion-card-content>
      </ion-card>
    </ion-content>
  </ion-page>
</template>

<script lang='js'>
import { defineComponent } from "vue";
import Header from "./Header.vue";
import {IonPage, IonContent} from '@ionic/vue';
import { cameraOutline, folderOpenOutline, timerOutline } from 'ionicons/icons';
import { FaceMesh, FACEMESH_RIGHT_EYE, FACEMESH_RIGHT_EYEBROW, FACEMESH_RIGHT_IRIS, FACEMESH_LEFT_EYE , FACEMESH_LEFT_EYEBROW, FACEMESH_LEFT_IRIS, FACEMESH_FACE_OVAL } from '@mediapipe/face_mesh';
import { drawConnectors } from '@mediapipe/drawing_utils';
import { Camera } from '@mediapipe/camera_utils';
import {
  mean, median, std, round, distance, square, intersect
} from 'mathjs';
const area = require('area-polygon')

export default defineComponent({
  name: "SelectMorphometryVideo",
  components: {
    Header,
    IonPage,
    IonContent
  },
  
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
</script>

<style scoped>
.card-title {
  font-size: 1.5rem;
}
.input_video {
    width: 100%;
    display: none;
}
.output_canvas{
    width: 100%;
}
.side-title {
    font-weight: 800;
    font-size: 1.2rem;
    color: #000000;
}
#side-title-OD {
    color: #FF0D00;
}
#side-title-OS {
    color: #00F2FF;
}
.results-col {
    height: 100%;
    vertical-align: middle;
}
.copyright {
  display: block;
  margin-top: 16px;
  margin-left: auto;
  margin-right: auto;
  width: 90%;
  text-align: center;
  hyphens: none;
  padding-bottom: 20px;
}
</style>