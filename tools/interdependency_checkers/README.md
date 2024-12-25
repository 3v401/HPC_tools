Interdependency checker tutorial and example


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
