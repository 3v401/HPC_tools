## Post under development

Containerization example Docker for Qiskit-aer-gpu.
When developing the Qiskit/1.2.4 module for JUNIQ Stages/2025 we found out that extension library [qiskit-aer-gpu](https://pypi.org/project/qiskit-aer-gpu/#files) was not released for aarch64 architecture (JEDI). To avoid requesting a whl release, we use a Docker container built from scratch to create a whl file that contains qiskit-aer CPU and GPU capabilities.
We will test it locally and insert it into our easyconfig and test it from our HPC system JEDI (aarch64) and JURECA (x86_64)

#### Docker container

1. Check if Docker is running: `sudo systemctl status docker`
2. If it is not running, start it: `sudo systemctl start docker`
3. To allow your current user have permissions to interact with the Docker daemon run: `sudo usermod -aG docker $USER`
4. Restart your sheel or reboot your laptop: `reboot`
5. Test docker access: `docker run hello-world`

After installing and setting up Docker, it is necessary to abilitate the capability of simulate other architectures. Our current Docker engine uses `amd64` architecture (our laptop) and the intended whl file is for `aarch64` (JEDI). Docker cannot run `aarch64` binaries on `amd64` systems unless emulation is explicitly enabled. For that run the following:

1. Install qwmu-user-static: `sudo apt install -y qemu-user-static`
2. Enable multi-architecture support in Docker: `docker run --rm --privileged multiarch/qemu-user-static --reset -p yes`
3. Specify the platform for building: `docker build --platform linux/arm64 -t aerbuilder .`
4. Run the Docker container: `docker run --platform linux/arm64 --rm -it aerbuilder /bin/bash`
5. You will get the following terminal:

(pic1)

##### Production of whl file

After setting up the multi-architecture aarch64 container with Docker on my amd64 laptop, the steps can be followed by the container. Follow the commands:

1. Activate the environment: `source qk_aer/bin/activate`
2. Move to: `cd qiskit-aer`
3. Run the build command tailoring it to `aarch64` GPU CUDA from JEDI. JURECA uses NVIDIA GH200 GPU and JEDI USES NVIDIA GH200, both use CUDA architecture `7.5`. It can be observed [here](https://developer.nvidia.com/cuda-gpus): `python ./setup.py bdist_wheel -- -DAER_THRUST_BACKEND=CUDA -DAER_CUDA_ARCH="7.5" -DAER_PYTHON_CUDA_ROOT=/qk_aer`. This command will create the .whl file in the `dist/` directory.
4. Repair the whl file to make it manylinux-compatible. To ensure it works on the HPC system, run auditwheel with the specified exclusions: `auditwheel repair --exclude libcudart.so.12 --exclude libcustatevec.so.1 --exclude libcutensornet.so.2 --exclude libcutensor.so.1 --exclude libcutensorMg.so.1 --exclude libcusolver.so.11 --exclude libcusolverMg.so.11 --exclude libcusolver.so.12 --exclude libcusolverMg.so.12 --exclude libcusparse.so.12 --exclude libcublas.so.12 --exclude libcublasLt.so.12 --exclude libnvJitLink.so.12 -w dist/ dist/qiskit_aer-0.15.1-cp312-cp312-linux_aarch64.whl`

#### Install whl file locally in a virtual environment

1. Identify the container ID: `docker ps`
2. Copy the wheel into your host system (laptop): `docker cp <CONTAINER_ID>:/qiskit-aer/dist/qiskit_aer-0.15.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl ~/qiskit_aer-0.15.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl`

#### Install whl file in JEDI and JURECA

Connect to JEDI and run the following commands:
1. Load basic modules: `module load Stages/2025 UserInstallations GCC/13.3.0 Python/3.12.3`
2. Create Python environment: `python -m venv venv_jedi`
3. Load environment: `source venv_jedi/bin/activate`
4. Load modules required to install Qiskit (dependencies and builddependencies): ``

#### Test module

###### JEDI

###### JURECA
