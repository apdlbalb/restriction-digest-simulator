# restriction-digest-simulator
This program takes a fasta file with a single sequence and a list of restriction enzymes with their recognition sites and returns cut DNA accordingly.
## Usage
Please run in command line as follows:
```
simulateDigest.py enzymes.txt sequence.fa
```
where `enzymes.txt` looks like:
```
EcoRI;G%AATTC
BamHI;G%GATCC
```
and where `sequence.fa` contains a single sequence in FASTA format.
