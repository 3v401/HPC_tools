# Create a unique kernel name using the username of the current user, ensuring easy identification.
KERNEL_NAME=${USER}_kernel

# Standardize the kernel name to lowercase to avoid case sensitivity issues:
export KERNEL_NAME=$(echo "${KERNEL_NAME}" | awk '{print tolower($0)}')
echo ${KERNEL_NAME}

# Search paths for Jupyter kernel directories:
# Check if the JUPYTER_PATH environment variable is empty. 1: Print the default Jupyter search path. 0: Print each path on a new line.
if [ -z $JUPYTER_PATH ]; then
  echo "$HOME/.local/share/jupyter"
else
  tr ':' '\n' <<< "$JUPYTER_PATH"
fi

# Set kernel type and path:
export KERNEL_TYPE=private # private, project or other
export KERNEL_SPECS_PREFIX=${HOME}/.local

# Set the appropriate directory path based on the selected kernel type and verify that the directory exists:
if [ "${KERNEL_TYPE}" == "project" ]; then
  export KERNEL_SPECS_PREFIX=${PROJECT}/.local
  echo "project kernel"
elif [ "${KERNEL_TYPE}" == "private" ]; then
  export KERNEL_SPECS_PREFIX=${HOME}/.local
  echo "private kernel"
else
  if [ ! -d "$KERNEL_SPECS_PREFIX" ]; then
    echo "ERROR: please create directory $KERNEL_SPECS_PREFIX"
  fi
  echo "other kernel"
fi

export KERNEL_SPECS_DIR=${KERNEL_SPECS_PREFIX}/share/jupyter/kernels

# Ensure that the kernel name is unique to avoid conflicts with existing kernels:
if [ -d "${KERNEL_SPECS_DIR}/${KERNEL_NAME}" ]; then
  echo "ERROR: Kernel already exists in ${KERNEL_SPECS_DIR}/${KERNEL_NAME}"
  echo "       Rename kernel name or remove directory."
fi
export KERNEL_SPECS_DIR=${KERNEL_SPECS_PREFIX}/share/jupyter/kernels

if [ -d "${KERNEL_SPECS_DIR}/${KERNEL_NAME}" ]; then
  echo "ERROR: Kernel already exists in ${KERNEL_SPECS_DIR}/${KERNEL_NAME}"
  echo "       Rename kernel name or remove directory."
fi

# Confirm the final path where the kernel will be installed:
echo ${KERNEL_SPECS_DIR}/${KERNEL_NAME}

# Define a specific directory path for storing the virtual environments of the kernels
export KERNEL_VENVS_DIR=${PROJECT}/${USER}/jupyter/kernels

# Create directory. The -p option creates the directory and any necessary parent directories if they do not already exist:
mkdir -p ${KERNEL_VENVS_DIR}

# Check the directory's permissions to ensure that project partners have the necessary read and execute permissions:
if [ "${KERNEL_TYPE}" != "private" ] && [ "${KERNEL_TYPE}" != "other" ]; then
  echo "Please check the permissions and ensure your project partners have read/execute permissions:"
  namei -l ${KERNEL_VENVS_DIR}
fi

# Output directory path. List its contents to verify the directory was created and is accessible.
echo ${KERNEL_VENVS_DIR}
ls -lt ${KERNEL_VENVS_DIR}

# Load the required modules for your kernel
module purge
# 'cslqip' is my project, use yours.
jutil env activate -p cslqip
cd $PROJECT
export USERINSTALLATIONS=${PROJECT}/${USER}
cd ${PROJECT}/${USER}
ml --force purge
ml Stages/2024 UserInstallations
module load GCCcore/.12.3.0
module load DWave/6.8.0

# Check if the directory for the virtual environment already exists to prevent overwriting or conflicts.
if [ -d "${KERNEL_VENVS_DIR}/${KERNEL_NAME}" ]; then
  echo "ERROR: Directory for virtual environment already ${KERNEL_VENVS_DIR}/${KERNEL_NAME}"
  echo "       Rename kernel name or remove directory."
else
  python -m venv --system-site-packages ${KERNEL_VENVS_DIR}/${KERNEL_NAME}
  source ${KERNEL_VENVS_DIR}/${KERNEL_NAME}/bin/activate
  # Set PYTHONPATH to prioritize packages installed in this virtual environment.
  export PYTHONPATH=${VIRTUAL_ENV}/lib/python3.11/site-packages:${PYTHONPATH}
  # output the path of VIRTUAL_ENV for verification (this variable is defined after the creation and activation of the environment)
  echo ${VIRTUAL_ENV}
fi

# Check location of pip (it must be in your activated environment)
which pip
if [ -z "${VIRTUAL_ENV}" ]; then
  echo "ERROR: Virtual environment not successfully initialized."
else
  # If environment activated install ipykernel package for communication between Python environment and Jupyter
  pip install --ignore-installed ipykernel
  # List packages installed to verify instllation
  ls ${VIRTUAL_ENV}/lib/python3.11/site-packages/
fi

# Any additional library you may need for your kernel:
# pip install <python-package you need>

##################################################################################################################
#                                             Create Jupyter kernel .sh
##################################################################################################################

# This script sets up the environment necessary to run the Jupyter kernel
# Ensure all modules and environment variables are loaded to replicate the environment in previous steps
# Execute ipykernel to start the kernel process with the provided arguments ('$@')
# "$@" is a powerful shell construct that allows scripts and functions to handle and pass on multiple arguments dynamically
# Save the script and make it executable. Output the contents to verify the script


echo '#!/bin/bash'"

module purge
# 'cslqip' is my project, use yours.
jutil env activate -p cslqip
cd $PROJECT
export USERINSTALLATIONS=${PROJECT}/${USER}
cd ${PROJECT}/${USER}
ml --force purge
ml Stages/2024 UserInstallations
module load GCCcore/.12.3.0
module load DWave/6.8.0

# Load extra modules you need for your kernel (as you did in step 1.2)
#module load <module you need>

# Activate your Python virtual environment
source ${KERNEL_VENVS_DIR}/${KERNEL_NAME}/bin/activate

# Ensure python packages installed in the virtual environment are always prefered
export PYTHONPATH=${VIRTUAL_ENV}/lib/python3.11/site-packages:"'${PYTHONPATH}'"

exec python -m ipykernel "'$@' > ${VIRTUAL_ENV}/kernel.sh
chmod +x ${VIRTUAL_ENV}/kernel.sh

# Check if the script has been correctly scripted:
cat ${VIRTUAL_ENV}/kernel.sh


##################################################################################################################
#                                             Create Jupyter kernel .json
##################################################################################################################

# Create Jupyter Kernel Configuration Directory and Files
# This is done to register the kernel with Jupyter so that it appears as an option when creating new notebooks.

# Install kernel for Jupyter:
python -m ipykernel install --name=${KERNEL_NAME} --prefix ${VIRTUAL_ENV}
#  VIRTUAL_ENV_KERNELS is where Jupyter looks for kernel configurations and specifications:
export VIRTUAL_ENV_KERNELS=${VIRTUAL_ENV}/share/jupyter/kernels

###
# Backup to ensure if any modification made to the kernel.json file in subsequent steps
# affects the performance and there's a need to revert these changes:
mv ${VIRTUAL_ENV_KERNELS}/${KERNEL_NAME}/kernel.json ${VIRTUAL_ENV_KERNELS}/${KERNEL_NAME}/kernel.json.orig

echo '{
  "argv": [
    "'${KERNEL_VENVS_DIR}/${KERNEL_NAME}/kernel.sh'",
    "-m",
    "ipykernel_launcher",
    "-f",
    "{connection_file}"
  ],
  "display_name": "'${KERNEL_NAME}'",
  "language": "python"
}' > ${VIRTUAL_ENV_KERNELS}/${KERNEL_NAME}/kernel.json

cat ${VIRTUAL_ENV_KERNELS}/${KERNEL_NAME}/kernel.json

# Directory where Jupyter looks for kernel specifications 
mkdir -p ${KERNEL_SPECS_DIR}
cd ${KERNEL_SPECS_DIR}
# Creates symbolic link. This link allows Jupyter to locate and use the kernel configuration stored:
ln -s ${VIRTUAL_ENV_KERNELS}/${KERNEL_NAME} .

echo -e "\n\nThe new kernel '${KERNEL_NAME}' was added to your kernels in '${KERNEL_SPECS_DIR}/'\n"
# List the contents to verify the symbolic link
ls ${KERNEL_SPECS_DIR}
