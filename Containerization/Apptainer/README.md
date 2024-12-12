In this example we are going to develop a jax container and set the configuration options compatible with our HPC system JURECA.

# What is Containerization?

Containerization is a form of virtualization that packages an application with all its dependencies into a single unit (the container).
Unline Virtual Machines (VMs), containers share the host system's kernel (in this case, JURECA) and hence being these much faster to start, smaller in size and more efficient in resource usage.

Containers encapsulate everything an application needs to run (libraries, tools...).

Containerization is used for software development, deployment, microservices architecture, high-performance computing, data sciente, machine learning...
### Benefits:
  1. Portability: You can run containers consistently accross different platforms (local, cloud or on-premises)
  2. Efficiency: Containers use fewer resources than VMs because they share the host system's OS kernel.
  3. Scalability: Containers can easily be scaled horizontally using orchestration tools like Kubernetes.

### Cons:
  1. Limited isolation: As they share the host OS kernel, security risk are higher compared to VMs.
  2. Complex Networking: Configuring and managing container networks can be challenging
  3. Storage management: Persistent storage for containers require additional setup.

## Most used container technologies

Docker, Kubernetes, Podman and Singularity (now Apptainer) are the most used container technologies. Docker is the most populat containerization platform. Singularity is specifically designed for scientific and HPC environments. It emphasizes reproducibility and security.

## Singularity (Now Apptainer)

Singularity/Apptainer is designed to address unique challenges faced in HPC such as security, preformance and integration with shared resources. It easily integrates with container technologies like Docker, enabling users to convert Docker images to a Singularity-compatible format. Supports integrations with schedulers like Slurm.

### JAX container

To get the jax container we need to access the site [Link](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/jax/tags) and get the latest tag image path: `nvcr.io/nvidia/jax:24.10-maxtext-py3`

  1. First, let's move to the folder $SCRATCH
  2. Create a folder where we will save our container `jureca_containers`
  3. Run the following command:
`TMPDIR=$SCRATCH/jureca_containers apptainer pull $SCRATCH/jureca_containers/jax.sif docker://nvcr.io/nvidia/jax:24.10-maxtext-py3`

The container will start ... (explain the process).

Once downloaded, move to `cd $SCRATCH/jureca_containers` and activate a shell by doing:
`apptainer shell jax.sif`. You will get a terminal like the following. You will see that you have the container active.
(pic1)
