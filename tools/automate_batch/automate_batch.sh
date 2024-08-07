It takes as input the script to run and tests this script on every machine (jureca, juwels, jusuf, judac)

To use each of them you must be a member of the project:

hdfml: cswmanage (no batch system found)
judac: cswmanage, jqctst01, qlmtst01, cslqip (no batch system found)
jureca: cswmanage (done)
jusuf: cswmanage (done)
juwels: cswmanage (done)
juwels_booster: cswmanage (done)
wsgjsc: wsgjsctst (no batch system found)
juqcs: jqctst01 (no batch system found)

Therefore the systems we will test are: jureca, jusuf, juwels, juwels-booster
User is always: cswmanage

You loggin to each system with ssh -4. Run the .sh script with --user-account = cswmanage

Partitions:
jureca: dc-cpu-devel, dc-gpu-devel
juwels-cluster: devel, develgpus
juwels-booster: develbooster
jusuf: batch, develgpus

The script is run on each system. So it will run:

cpu job
cpu distributed job
gpu job
gpu distributed job

And return the outcomes.
