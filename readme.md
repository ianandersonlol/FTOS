# FTOS Documentation

This document provides information on how to use the `ftos` script to find and report the positions of a specific motif in FASTA files. The motif in question is `DDXXD`, where `X` can be any amino acid.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Example](#example)
5. [Notes](#notes)

## Introduction

The `ftos` script is designed to scan through FASTA files in the current directory and identify positions of a specific motif, `DDXXD`, in sequences. The script outputs the position of each motif occurrence for every FASTA file it processes.

## Installation

No special installation is required for the `ftos` script. It is a standalone Python script. Make sure you have Python installed on your system to run it.

## Usage

To use the `ftos` script, follow these steps:

1. **Place your FASTA files in the same directory as the script**: Ensure that your target FASTA files, with extensions `.fasta` or `.fa`, are located in the same directory as the `ftos` script.

2. **Run the script**: Execute the script using Python. Open a terminal, navigate to the directory containing the script and your FASTA files, and run the following command:

   ```bash
   python ftos.py
   ```

3. **Review the output**: The script will print the filename and the position of each motif occurrence to the console.

## Example

Here's an example of how the script works:

Assume you have a FASTA file named `example.fasta` in the same directory as `ftos.py` with the following content:

```
>sequence_1
MDDXXDAAADDXXD
>sequence_2
DDXXDMMDDXXD
```

When you run the script, the output will be:

```
Motif found in example.fasta at position 2
Motif found in example.fasta at position 10
Motif found in example.fasta at position 1
Motif found in example.fasta at position 7
```

This indicates that the motif `DDXXD` was found at these positions in `example.fasta`.

## Notes

- **File Extensions**: The script only processes files with `.fasta` or `.fa` extensions.
- **Sequence Headers**: Lines starting with `>` are considered headers and are not processed for motif searching.
- **Directory**: The script scans the current working directory. Ensure your FASTA files are in that directory when running the script.
- **Output**: The script outputs directly to the console. If you need to save the output, consider redirecting the output to a file.

This script is a simple utility for motif searching in bioinformatics, making it useful for researchers and students working with protein sequences.