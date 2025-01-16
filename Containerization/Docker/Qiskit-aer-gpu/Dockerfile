# Docker container for qikit_aer 0.15.1 CPU + GPU aarch64


# Use manylinux2014_aarch64 base image for compatibility with the aarch64 architecture
FROM quay.io/pypa/manylinux2014_aarch64

# Label to describe the image
LABEL Description="cuda_12.6_manylinux2014_aarch64"

# Build arguments for the architecture and CUDA versions
ARG ISA="aarch64"
ARG CUDA_VERSION="12-6"

# Install yum-utils for managing yum repositories and other utilities
RUN yum install -y yum-utils
# Extra Packages for Enterprise Linux (EPEL) repository
RUN yum install -y epel-release
# OpenBLAS library for basic linear algebra operations
RUN yum install -y openblas-devel
# NVIDIA CUDA repository for RHEL8 (specific to the aarch64 architecture)
RUN yum-config-manager --add-repo https://developer.download.nvidia.com/compute/cuda/repos/rhel8/sbsa/cuda-rhel8.repo
# CUDA libraries, development tools, and CUDA compiler
RUN yum install -y cuda-libraries-${CUDA_VERSION}.${ISA} \
                   cuda-libraries-devel-${CUDA_VERSION}.${ISA} \
                   cuda-compiler-${CUDA_VERSION}.${ISA}

# Git for cloning repositories
RUN yum install -y git
# Clean up cached files to reduce image size
RUN yum clean all

# Add CUDA library paths to the dynamic linker configuration
RUN echo "/usr/local/cuda/lib64" >> /etc/ld.so.conf.d/999_nvidia_cuda.conf
RUN echo "/usr/local/cuda/lib" >> /etc/ld.so.conf.d/999_nvidia_cuda.conf

# Clone Qiskit Aer repository
RUN git clone https://github.com/Qiskit/qiskit-aer

# Create Python virtual environment
RUN python3.12 -m venv qk_aer
# Activate virtual environment, upgrade pip, setuptools, wheel and install dependencies
RUN source qk_aer/bin/activate && pip install --upgrade pip setuptools wheel && pip install nvidia-cuda-runtime-cu12 nvidia-cublas-cu12 nvidia-cusolver-cu12 nvidia-cusparse-cu12 'cuquantum-cu12<24.11.0' auditwheel && cd /qiskit-aer && git checkout tags/0.15.1 && pip install -r /qiskit-aer/requirements-dev.txt

# Update PATH and LD_LIBRARY_PATH environment variables to include the CUDA binaries
ENV PATH="/usr/local/cuda/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/local/cuda/lib64:${LD_LIBRARY_PATH}"

# Set default command to open a Bash shell
CMD ["/bin/bash"]
