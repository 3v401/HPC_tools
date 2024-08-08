import subprocess                                                                                                    
import sys                                                                                                           
import shutil                                                                                                        
                                                                                                                     
###############################################################                                                      
# Input interactive data: (Not finished)                                                                             

modules = input("Introduce the correct names and versions of the modules you want to load, e.g. DWave/6.8.0 \n")
print(f"Modules introduced: {modules}\n")

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

################################################################
# Prepare the slurm jobs (opens the files and adds specific instructions)

def edit_job_file(filename, partition, modules, test_script):
    backup_filename = filename + ".bak"
    # Create a backup of the original file
    shutil.copy2(filename, backup_filename)

    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            if line.startswith("#SBATCH --partition="):
                # Append "dc-devel-gpu" to the partition line
                line = line.strip() + "{}\n".format(partition)

            if line.startswith("module load"):
                line = line.strip() + " Stages/2024 UserInstallations {}\n".format(modules)

            if line.startswith("srun"):
                line = line.strip() + " python3 {}".format(test_script)
                file.write(line)
                break

            else:
                file.write(line)


def restore_original_file(filename):
    backup_filename = filename + ".bak"
    shutil.copy2(backup_filename, filename)

def show_edited_file(filename):
    # Check the contents of the file
    with open(filename, 'r') as file:
        print(file.read())

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

    edit_job_file("./cpu/cpu.job", partitions[0], modules, "./cpu/cpu_script.py")
    print("Edited cpu.job file for {} is: \n".format(partitions[0]))
    show_edited_file("./cpu/cpu.job")
    run_command("sbatch ./cpu/cpu.job") # El outcome del comando no hace prompt, mira como hacerlo
    restore_original_file("./cpu/cpu.job")

    print("Running CPU distributed simulation...\n")

    edit_job_file("./cpu_mpi/cpu_mpi.job", partitions[0], modules, "./cpu_mpi/cpu_mpi_script.py")
    print("Edited cpu_mpi.job file for {} is: \n".format(partitions[0]))
    show_edited_file("./cpu_mpi/cpu_mpi.job")
    run_command("sbatch ./cpu_mpi/cpu_mpi.job")
    restore_original_file("./cpu_mpi/cpu_mpi.job")

    print("Running GPU simulation...\n")
        
    edit_job_file("./gpu/gpu.job", partitions[1], modules, "./gpu/gpu_script.py")
    print("Edited gpu.job file for {} is: \n".format(partitions[1]))
    show_edited_file("./gpu/gpu.job")
    run_command("sbatch ./gpu/gpu.job")
    restore_original_file("./gpu/gpu.job")

    print("Running GPU distributed simulation...\n")
    
    edit_job_file("./gpu_mpi/gpu_mpi.job", partitions[1], modules, "./gpu_mpi/gpu_mpi_script.py")
    print("Edited gpu_mpi.job file for {} is: \n".format(partitions[1]))
    show_edited_file("./gpu_mpi/gpu_mpi.job")
    run_command("sbatch ./gpu_mpi/gpu_mpi.job")
    restore_original_file("./gpu_mpi/gpu_mpi.job")

if __name__ == "__main__":
    main()
