# NatHACKS_Submission

Currently diagnosing Strabismus (eye misalignment) through the eye cover/uncover test

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

#### Diagnosis for Cover/Uncover Test:

Hypertropia: Eye twitches up
Hypotrophia: Eye twitches down
Expotropia: Eye twitches outwards
Esotrophia: Eye twitches inwards

Tolerance: 4 mm