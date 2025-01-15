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

#### Install whl file locally in a virtual environment

#### Install whl file in JEDI and JURECA

#### Test module

###### JEDI

###### JURECA
