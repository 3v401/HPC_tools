Interdependency checker tutorial and example

When developing modules for the JUNIQ platform, it is essential to ensure that no interdependency collisions exist between the libraries used by different modules. To streamline this process, `interdependency_checker.py` was created, a Python script designed to analyze and compare extension packages across multiple modules. Any number of .txt files can be introduced into the python script identifying version mismatches, common packages between modules, and unique dependencies, helping to maintain a consistent and conflict-free environment.

This tool *drastically reduces work time* required to analyze and resolve interdependency collisions when developing modules. Comparing 8 modules manually, by organizing an Excel file by hand with all their extension names and versions, can take up to 3 days. With interdependency_checker.py, this process is streamlined, reducing the effort to less than 2 minutes *saving up to 99% of the previously consumed time*. This tool enables you to:

1. Look for modules that share the same package name and different version.
2. Look for modules that share same package names and same version.
3. Look for modules that share different package names (that are unique to each module).

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
