# NatHACKS_Submission

#### Written Summary:

Quick Ocular Movements (QOM) is a python based web-application which tracks and processes eye position and movement to help patients diagnose potential eye conditions. The website essentially has two part photo and video functionality. Both methods allow for a quick real-time calculation of the specific coordinates of their eye structure and eye movement, through which the application will determine potential eye conditions such as: hypotropia, hypertropia, etc. The User is able to access our Javascript frontend design and is given prompts to cover/uncover each eye and result’s json files from the backend are displayed. An environment was created for the backend that installs the dependencies and packages (OpenCV, Mediapipe, Numpy) that can be activated through conda. The main script that is found in the frontend directory calls the backend webcam measurement script that utilizes OpenCV for video capture and MediaPipe for meshing the face and detecting the eyes. The real-time data are in a NormalizedLandmark object which is extracted through the get_measurement helper script into Measurment objects. The measurement object has a hash map attribute which can be collated at 30 per second. All the samples are run through the statistics script that returns it’s sumary statistics as the Measurement’s child class MeasurementStatistics. This is then run through the diagnosis script which uses Cauchy Schwartz Variance for the differences in positions to at 95% confidence if there is a deviation corresponding to each eye condition. 

The website design is created through React which connects to the Python back-end through Node.js, and the aesthetics were created based on wireframes in Figma, and 
the corresponding CSS and HTML styling.

Backend impementation and Full Stack Integrations by Lawrence Tsai
Frontend by Yun Cao

#### Set up the conda environment

You need to [install Anaconda](https://docs.anaconda.com/anaconda/install/index.html) on your system or [install Mamba](https://github.com/mamba-org/mamba) as well, and substitute `conda` with `mamba` in all following commands.

Update Anaconda if needed by running

```
conda update -n base conda
```

To download the dependencies and create the conda environment, inside the NATHACKS_Submission directory, run:

```
conda env create --file environment.yml
```

After, you can activate the new environment with:

```
conda activate NatHACKS
```

If you've already cloned and installed a previous version of the platform, you may need to update the conda environment. To update the conda environment with any new depedencies, do:

```
conda env update --name natHACKS --file environment.yml --prune
```


#### To run the webapp in the development mode

```
npm install
```
```
npm start
```

#### Diagnosis for Cover/Uncover Test:

Hypertropia: Eye twitches up

Hypotropia: Eye twitches down

Expotropia: Eye twitches outwards

Esotropia: Eye twitches inwards

Tolerance: 4 mm at 95% confidence t-test
