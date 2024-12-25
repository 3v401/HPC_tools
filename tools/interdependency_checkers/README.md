## Interdependency checker tutorial and example

When developing modules for the JUNIQ platform, it is essential to ensure that no interdependency collisions exist between the libraries used by different modules. To streamline this process, `interdependency_checker.py` was created, a Python script designed to analyze and compare extension packages across multiple modules. Any number of .txt files can be introduced into the python script identifying version mismatches, common packages between modules, and unique dependencies, helping to maintain a consistent and conflict-free environment.

This tool *drastically reduces work time* required to analyze and resolve interdependency collisions when developing modules. Comparing 8 modules manually, by organizing an Excel file by hand with all their extension names and versions, can take up to 3 days. With interdependency_checker.py, this process is streamlined, reducing the effort to less than 2 minutes *saving up to 99% of the previously consumed time*. This tool enables you to:

1. Look for modules that share the same package name and different version.
2. Look for modules that share same package names and same version.
3. Look for modules that share different package names (that are unique to each module).

### Example

Let's run an example with interdependency_checker.py. Let's compare three modules: PyQuil, Pulser, and DWave. This example will showcase how the tool identifies interdependency collisions, unique extensions, and common package names + versions.

To further validate its effectiveness, we will intentionally edit the pip list output for DWave at the end to create a version mismatch for numpy package (1.25.1 --> 1.26.1) with the other modules. By running this script, we will observe how it accurately detects and flags differing versions for the same package name (numpy).

Run the following commands:

```
module load Stages/2024 UserInstallations GCCcore/.12.3.0 PyQuil/4.8.0
pip list > pyquil.txt 2>&1
ml --force purge
module load Stages/2024 UserInstallations GCCcore/.12.3.0 pulser/0.18.0
pip list > pulser.txt 2>&1
ml --force purge
module load Stages/2024 UserInstallations GCCcore/.12.3.0 DWave/6.8.0
pip list > dwave.txt 2>&1
```

This code:

1. Loads the required modules.
2. Generates the pip list output and saves it into <module_name>.txt file.
3. Unloads the previously loaded modules (cleans environment).
4. Repeats from step 1.

Now execute:

```
python3 interdependency_checker.py
```

and follow the commands described in the images:

pic1

As it can be observed, no interdependency collisions were found.

pic2

It can be observed with instruction `2` the modules that share the same package with same version.

pic3

It can be observed with instruction `3` the modules that share different package name.

#### Finding interdependency collision

Open the dwave.txt file by `vim dwave.txt` and edit the numpy version (1.25.1 --> 1.26.1). Save and exit. Run the `python3 interdependency_checker.py`, choose the three .txt files and run instruction 1:

pic4

As expected, there is an interdependency collision in numpy package! 😃👍
