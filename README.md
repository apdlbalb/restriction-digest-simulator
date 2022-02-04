# restriction-digest-simulator
This program takes a fasta file with a single sequence and a list of restriction enzymes with their recognition sites and returns cut DNA accordingly.
## Dependencies
- Written with Python 3
## Usage
Assuming all are in the same directory, please run in command line as follows:
```
./simulateDigest.py enzymes.txt sequence.fas
```
where `enzymes.txt` looks like:
```
EcoRI;G%AATTC
BamHI;G%GATCC
```
and where `sequence.fas` contains a single sequence in FASTA format.

## Sample output
```
Restriction enzyme analysis of sequence from file sequence.fa
Cutting with enzymes found in file enzymes.txt
-----------------------------------------------------------------
Sequence name: TESTSEQ
Sequence is 107 bases long.
-----------------------------------------------------------------
There are 2 cutting sites for EcoRI, cutting at G%AATTC
There are 3 fragments:

length: 27 range: 1-27
ATTATAAAAT TAAAATTATA TCCAATG
length: 23 range: 28-50
AATTCAATTA AATTAAATTA AAG
length: 57 range: 51-107
AATTCAATAA TATACCCCGG GGGGATCCAA TTAAAAGCTA AAAAAAAAAA AAAAAAA
```
