# -----------------------------------------
# Author: Ana Patricia Balbon
# Student number: 0790244
# Email: abalbon@uoguelph.ca
# Assignment 2
# Description: This program reads in a FASTA file of a nucleotide sequence
# and a text file of restriction enzymes, simulates a digest, and prints
# a report.
# Copyright (c) 2021. All rights reserved.
# ------------------------------------------

import sys
import os

# FUNCTIONS --------------------------------------------------------------------

# Digest takes a DNA sequence "seq" and formatted information about the name of
# an enzyme "enzyme" and its cut sequence and returns the name of the enzyme if
# there are no cutting sites in "seq".  Otherwise, it prints the fragments
# of "seq" cut by the enzyme, character by character
# String or Void <- String String

def digest(seq, enzyme):
    temp = enzyme.split(";")
    enzymeName = temp[0]
    cleavageSite = (temp[1]).find("%")
    enzymeSeq = (temp[1]).replace("%", "").rstrip("\n")
    numSites = seq.count(enzymeSeq)
    if (numSites == 0):
        return (enzymeName)
    else:
        print("-" * 65)
        print("There are", numSites, "cutting sites for", enzymeName + ",",
              "cutting at", temp[1], end = "")
        print("There are", numSites + 1, "fragments:")
        spaceCount = 0 # Count up to the next position where there should be a space
        lineBreak  = 0 # Count up to the next position where there should be a newline
        cutStart = 1
        cutStop = seq.find(enzymeSeq) + cleavageSite
        for i in range(0, len(seq)):
            if i == 0 or i == cutStop:
                print("\n", end = "")
                if i == 0:
                    print("length:", cutStop - cutStart + 1, end=" ")
                    print("range:", str(cutStart) + "-" + str(cutStop))
                    cutStart = cutStop + 1
                    cutStop = (seq[i:-1]).find(enzymeSeq) + cleavageSite + i
                elif (seq[i:-1]).find(enzymeSeq) > -1:
                    cutStart = cutStop + 1
                    cutStop = (seq[i:-1]).find(enzymeSeq) + cleavageSite + i
                    print("length:", cutStop - cutStart + 1, end = " ")
                    print("range:", str(cutStart) + "-" + str(cutStop))
                else:
                    cutStart = cutStop + 1
                    cutStop = len(seq)
                    print("length:", cutStop - cutStart + 1, end=" ")
                    print("range:", str(cutStart) + "-" + str(cutStop))
                # Reset counts after meeting a cut site
                spaceCount = 0
                lineBreak = 0
            if spaceCount == 10:
                print(" ", end = "")
                spaceCount = 0 # Reset count
                lineBreak += 1 # Increment to the next newline
            if lineBreak == 6:
                print("\n", end = "")
                # Reset counts after line break
                lineBreak = 0
                spaceCount = 0
            print(seq[i], end = "")
            spaceCount += 1


# READ FILES -------------------------------------------------------------------
# Take arguments from the commandline
commLineArg1 = sys.argv[1]
commLineArg2 = sys.argv[2]

if (os.path.isfile(commLineArg1) & os.path.isfile(commLineArg2)): # Check if files exist

    # Check the file extensions and assign to the correct variable
    if (commLineArg1.endswith(".fas") | commLineArg1.endswith(".fasta")) & commLineArg2.endswith(".txt"):
        fastaFileName = commLineArg1
        enzymeFileName = commLineArg2
    elif (commLineArg2.endswith(".fas") | commLineArg2.endswith(".fasta")) & commLineArg1.endswith(".txt"):
        fastaFileName = commLineArg2
        enzymeFileName = commLineArg1
    else:
        print("Sorry! Please check your filenames and try again")
        exit()
else:
    print("Sorry! Please check your file paths and try again.")
    exit()

# UNPACK FASTA FILE ------------------------------------------------------------
fastaFile = open(fastaFileName, "r")
fastaHeader = fastaFile.readline()[1:-1]
fastaSeq = (fastaFile.read()).replace("\n", "")
fastaFile.close()

# UNPACK ENZYME FILE -----------------------------------------------------------
enzymeFile = open(enzymeFileName, "r")
enzymes = enzymeFile.readlines()
enzymeFile.close()


# REPORT -----------------------------------------------------------------------
print("Restriction enzyme analysis of sequence from file", fastaFileName)
print("Cutting with enzymes found in file", enzymeFileName)
print("-" * 65)

print("Sequence name:", fastaHeader)
print("Sequence is", len(fastaSeq), "bases long.")

noCutEnzymes = []

# Take the list of enzymes read from the file and run the digest function
# on each of them.  If there are no cut sites, store the name of the enzyme in
# the list noCutEnzymes.
for enzyme in enzymes:
    noCutEnzyme = digest(fastaSeq, enzyme)
    if not(noCutEnzyme):
        print("\n")
    else:
        noCutEnzymes.append(noCutEnzyme)

# If the list noCutEnzymes is non-empty, print the names of the enzymes
# which have no cut sites.
if len(noCutEnzymes) > 0:
    print("-" * 65)
    print("There are no sites for", ", ".join(noCutEnzymes) + ". \n")