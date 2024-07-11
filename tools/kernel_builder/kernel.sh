echo '#!/bin/bash'"

# Note: My outcome after creating kernel.sh won't be shared because of privacy/security reasons. 


module purge
# cslqip is my project, use yours.
jutil env activate -p $PROJECT_NAME
cd $PROJECT
export USERINSTALLATIONS=${PROJECT}/${USER}
cd ${PROJECT}/${USER}
ml --force purge
ml Stages/2024 UserInstallations
module load ${MODULE_LIST}

# Activate your Python virtual environment
source ${KERNEL_VENVS_DIR}/${KERNEL_NAME}/bin/activate

# Ensure python packages installed in the virtual environment are always prefered
export PYTHONPATH=${VIRTUAL_ENV}/lib/python3.11/site-packages:"'${PYTHONPATH}'"

exec python -m ipykernel "'$@' > ${VIRTUAL_ENV}/kernel.sh
chmod +x ${VIRTUAL_ENV}/kernel.sh
