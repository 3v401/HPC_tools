# Kernel

The kernel is the core component of an operating system (OS). It acts as a bridge between the hardware of a computer and the software applications that run on it. The kernel is responsible for managing system resources such as CPU, memory and I/O devices. Building a custom Jupyter kernel allows for tailored computational environments that can meet specific needs. In the context of Jupyter Notebooks, a kernel is the computational engine that executes the code contained in the notebook cells. Different kernels can support different programming languages (e.g., Python, R, Julia). In our case we will use Python.

A kernel bridged to a Jupyter Notebook connected to an HPC system allows the notebook to use the computational resources of the HPC environment with a Jupyter Notebook interface instead of using a Linux/UNIX terminal.

### Steps:

1. Create Python Environment: To ensure a clean environment free from conflicts with other Python environments on the system.
2. Create a launch script (`kernel.sh`) for the Jupyter kernel: Used to start the kernel with the necessary environment variables and configurations. It includes paths to the virtual environment, environment settings and other initialization commands. By creating this `.sh` we will ensure that the kernel starts with the correct settings and environment every time.
3. Create Jupyter kernel configuration (`kernel.json`) script: This file will allow Jupyter to recognize and launch the custom kernel

In this repository we will develop a basic Jupyter Notebook kernel for an HPC (High-Performance Computing) system.

### Example

#### Load a kernel for DWave

![alt text](URL)
Resource Management:

1. Handle job submissions and monitoring on the HPC cluster (using Slurm).
2. 
