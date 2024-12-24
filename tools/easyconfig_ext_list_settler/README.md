When developing a module on HPC systems using EasyBuild, the "exts_lists" parameter plays a crucial role in managing extensions. To find out which external libraries are needed, a Python virtual environment needs to be created as a base for the module. Once the required dependencies are loaded and the virtual environment is activated, the module installation can proceed with a simple "pip install [library]" command, ensuring all required libraries are properly installed within the environment.

#### Example

To test this tool, we use MyQLM module as an example.

1. First, import all the necessary dependencies required for MyQLM.

2. For our HPC infrastructure, running the command "pip install myqlm pulser-myqlm qoqo-myqlm" alone isn't sufficient. We also need to specify certain dependency versions to **avoid conflicts** with other installed modules (e.g., Qiskit, Pulser, DWave...). Additionally, the command should be executed as "pip install ... > output.txt 2>&1" to save both the standard output and error logs into the "output.txt" file for troubleshooting or verification purposes.

3. After the file is created, run the Python script to analyze and identify the external dependencies (exts_list) necessary for developing the module.

4. With the list of required exts_lists generated, you can proceed with developing the easyconfig module. It is highly beneficial to utilize the "interdependency checker" tool at this stage to ensure there are no conflicts or collisions with other modules and other components in our infrastructure.

##### Extension libraries for myqlm 1.10.6

1. Load the module dependencies for Stages/2025 running:
```
module load GCCcore/.13.3.0 poetry/.1.8.3 CMake/3.29.3 maturin/.1.6.0 Rust/1.78.0 Python/3.12.3 SciPy-bundle/2024.05 dill/0.3.9 networkx/3.3 tqdm/4.66.5 matplotlib/3.9.2 IPython/8.27.0 setuptools-rust/.1.9.0
python3 -m venv venv
source venv/bin/activate
pip install myqlm
```
You will get the necessary prompt saved into `output.txt` file.
(pic1)
Send this txt as parameter to `exts_lists_settler.py`
(pic2)
You will get the extension libraries required for myqlm sorted with its dependency name and version for a faster development.
