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

export KERNEL_TYPE=private # private, project or other
export KERNEL_SPECS_PREFIX=${HOME}/.local

export KERNEL_SPECS_DIR=${KERNEL_SPECS_PREFIX}/share/jupyter/kernels

if [ -d "${KERNEL_SPECS_DIR}/${KERNEL_NAME}" ]; then
  echo "ERROR: Kernel already exists in ${KERNEL_SPECS_DIR}/${KERNEL_NAME}"
  echo "       Rename kernel name or remove directory."
fi

echo ${KERNEL_SPECS_DIR}/${KERNEL_NAME}

export KERNEL_VENVS_DIR=${PROJECT}/${USER}/jupyter/kernels

mkdir -p ${KERNEL_VENVS_DIR}
if [ "${KERNEL_TYPE}" != "private" ] && [ "${KERNEL_TYPE}" != "other" ]; then
  echo "Please check the permissions and ensure your project partners have read/execute permissions:"
  namei -l ${KERNEL_VENVS_DIR}
fi

echo ${KERNEL_VENVS_DIR}
ls -lt ${KERNEL_VENVS_DIR}

###

if [ -d "${KERNEL_VENVS_DIR}/${KERNEL_NAME}" ]; then
  echo "ERROR: Directory for virtual environment already ${KERNEL_VENVS_DIR}/${KERNEL_NAME}"
  echo "       Rename kernel name or remove directory."
else
  python -m venv --system-site-packages ${KERNEL_VENVS_DIR}/${KERNEL_NAME}
  source ${KERNEL_VENVS_DIR}/${KERNEL_NAME}/bin/activate
  export PYTHONPATH=${VIRTUAL_ENV}/lib/python3.11/site-packages:${PYTHONPATH}
  echo ${VIRTUAL_ENV} # double check
fi

###

which pip
if [ -z "${VIRTUAL_ENV}" ]; then
  echo "ERROR: Virtual environment not successfully initialized."
else
  pip install --ignore-installed ipykernel
  ls ${VIRTUAL_ENV}/lib/python3.11/site-packages/ # double check
fi

#sh
###

python -m ipykernel install --name=${KERNEL_NAME} --prefix ${VIRTUAL_ENV}
export VIRTUAL_ENV_KERNELS=${VIRTUAL_ENV}/share/jupyter/kernels

###

mv ${VIRTUAL_ENV_KERNELS}/${KERNEL_NAME}/kernel.json ${VIRTUAL_ENV_KERNELS}/${KERNEL_NAME}/kernel.json.orig

#json
###

mkdir -p ${KERNEL_SPECS_DIR}
cd ${KERNEL_SPECS_DIR}
ln -s ${VIRTUAL_ENV_KERNELS}/${KERNEL_NAME} .

echo -e "\n\nThe new kernel '${KERNEL_NAME}' was added to your kernels in '${KERNEL_SPECS_DIR}/'\n"
ls ${KERNEL_SPECS_DIR}

###
