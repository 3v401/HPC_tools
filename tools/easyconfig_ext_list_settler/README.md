When developing a module on HPC systems using EasyBuild, the "exts_lists" parameter plays a crucial role in managing extensions. To find out which external libraries are needed, a Python virtual environment needs to be created as a base for the module. Once the required dependencies are loaded and the virtual environment is activated, the module installation can proceed with a simple "pip install [library]" command, ensuring all required libraries are properly installed within the environment.

#### Example

To test this tool, we use MyQLM module as an example.

1. First, import all the necessary dependencies required for MyQLM.

2. For our HPC infrastructure, running the command "pip install myqlm pulser-myqlm qoqo-myqlm" alone isn't sufficient. We also need to specify certain dependency versions to **avoid conflicts** with other installed modules (e.g., Qiskit, Pulser, DWave...). Additionally, the command should be executed as "pip install ... > output.txt 2>&1" to save both the standard output and error logs into the "output.txt" file for troubleshooting or verification purposes.

3. After the file is created, run the Python script to analyze and identify the external dependencies (exts_list) necessary for developing the module.

4. With the list of required exts_lists generated, you can proceed with developing the easyconfig module. It is highly beneficial to utilize the "interdependency checker" tool at this stage to ensure there are no conflicts or collisions with other modules and other components in our infrastructure.
