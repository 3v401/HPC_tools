#!/bin/bash

# These loaded modules correspond to HPC systems (center not mentioned) version 2024.

# export PROJECT=Type_your_project # Project you are working with

ml --force purge
jutil env activate -p $PROJECT
cd $PROJECT
export USERINSTALLATIONS=${PROJECT}/${USER}
cd ${PROJECT}/${USER}
ml --force purge
ml Stages/2024 UserInstallations
module load GCCcore/.12.3.0
module load DWave/6.8.0

    
# Activate your Python virtual environment
source ${KERNEL_VENVS_DIR}/${KERNEL_NAME}/bin/activate
    
# Ensure python packages installed in the virtual environment are always prefered
export PYTHONPATH=${VIRTUAL_ENV}/lib/python3.11/site-packages:${PYTHONPATH}
    
exec python -m ipykernel $@
