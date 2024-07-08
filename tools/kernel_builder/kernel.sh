#!/bin/bash

# These loaded modules correspond to HPC systems (center not mentioned) version 2024.
module purge
module load Stages/2024
module load UserInstallations
module load GCCcore/.12.3.0
module load DWave/6.8.0

    
# Activate your Python virtual environment
source ${KERNEL_VENVS_DIR}/${KERNEL_NAME}/bin/activate
    
# Ensure python packages installed in the virtual environment are always prefered
export PYTHONPATH=${VIRTUAL_ENV}/lib/python3.11/site-packages:${PYTHONPATH}
    
exec python -m ipykernel $@
