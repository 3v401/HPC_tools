#!/bin/bash
set -x
echo "Creating volume for container"
export ACTUAL_PATH=${PWD}
mkdir $ACTUAL_PATH/jax_volume
echo "Opening shell"
apptainer shell --bind /p/software/jurecadc/lmod:/p/software/jurecadc/lmod \
                --bind /p/software/default/stages:/p/software/default/stages \
                --bind /p/software/default/userinstallations:/p/software/default/userinstallations \
                --bind /usr/bin/lua:/usr/bin/lua \
                --bind /usr/lib64/liblua-5.4.so:/usr/lib64/liblua-5.4.so \
                --bind /usr/lib64/lua:/usr/lib64/lua \
                --bind /usr/share/lua:/usr/share/lua \
                --bind /usr/lib64/libcrypt.so.2:/usr/lib64/libcrypt.so.2 \
                --bind ${ACTUAL_PATH}/jax_volume:/opt/volume \
                jax.sif <<EOF
export LMOD_DIR=/p/software/jurecadc/lmod/8.7.49/libexec
export LMOD_CMD=$LMOD_DIR/lmod
export MODULEPATH=/p/software/default/stages/2025/UI/Toolchains:/p/software/default/stages/2025/UI/Defaults:/p/software/default/stages/2025/UI/Tools:/p/software/default/stages/2025/UI/Compilers:/p/software/default/otherstages:/p/software/default/supercomputer_modules:/p/software/default/productionstages:/p/software/default/userinstallations:/p/software/default/devel
export PATH=$LMOD_DIR:$PATH
export LD_LIBRARY_PATH=/usr/lib64:$LD_LIBRARY_PATH
echo "Deleting previous myenv1 environment (just in case)"
rm -rf ./jax_volume/myenv1
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
module load GCCcore/.13.3.0 poetry/.1.8.3 CMake/3.29.3 maturin/.1.6.0 Rust/1.78.0 Python/3.12.3 SciPy-bundle/2024.05 dill/0.3.9 networkx/3.3 tqdm/4.66.5 matplotlib/3.9.2 IPython/8.27.0 setuptools-rust/.1.9.0 qutip/5.0.4
# To not prompt error while loading jax with python3 -c "import jax":
module load imkl/2024.2.0
# To create environment:
uv venv jax_volume/myenv1
# Activate environment:
source jax_volume/myenv1/bin/activate
# To avoid hardlinking problems (copies everything istead)
export UV_LINK_MODE=copy
# To avoid overwriting numpy and scipy:
uv pip install --link-mode=copy jaxlib jax numpy==1.26.4 scipy==1.13.1
# To check jax version:
echo "Jax version is:"
python -c "import jax; print(jax.__version__)"
echo "Jax module is located at:"
python3 -c "import jax; print(jax.__file__)"
echo "Python version is:"
python --version
echo "Python is located at:"
whereis python
echo "Doing <pip list> we don't get the jax module, uv installations (scipy, numpy, jax...) located in: ./jax_volume/myenv1"
# echo "pip list returns:"
# pip list
echo "showing ./jax_volume/myenv1/lib/python3.12/site-packages/"
ls -la ./jax_volume/myenv1/lib/python3.12/site-packages/
EOF
