import subprocess
import sys

###############################################################
# Input interactive data: (Not finished)


################################################################
# Obtain system hostname and partitions: (Finished)

try:
    # Run the hostname command and capture the output
    result = subprocess.run("hostname", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    hostname = result.stdout.decode().strip()

    # Split the hostname by '.' and get the last part
    suffix = hostname.split('.')[-1]
except subprocess.CalledProcessError as e:
    print(f"Error executing hostname command: {e.stderr.decode()}")
    sys.exit(1)

if suffix:
    print(f"The last part of the hostname is: {suffix}")

partitions=[]
if suffix=="jureca":
    partitions=["dc-cpu-devel","dc-gpu-devel"]
elif suffix=="juwels":
    # This script only counts for juwels-cluster (check how to modify for juwels-booster)
    partitions=["devel","develgpus"]
elif suffix=="jusuf":
    partitions=["batch", "develgpus"]

print(f"The partitions used for {hostname} will be: {partitions}\n")

#################################################################
# Run jobs for those partitions: (Not finished)

def run_command(command):
    try:
        result = subprocess.run(command, shell = True, check = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error executing {command}:\n {e.stderr.decode()}")

def main():
    print("Running CPU simulation...\n")
    run_command("sbatch cpu.job")
    print("Running CPU distributed simulation...\n")
    run_command("sbatch cpu_mpi.job")
    print("Running GPU simulation...\n")
    run_command("sbatch gpu_mpi.job")


if __name__ == "__main__":
    main()
