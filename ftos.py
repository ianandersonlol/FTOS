import os
import re

# Regular expression to find the motif. Using '.' to match any character (amino acid) in place of 'X'
motif_regex = re.compile(r'DD..D')

def find_motif_positions(fasta_file):
    """Find and print positions of the motif DDXXD in a given FASTA file."""
    with open(fasta_file, 'r') as file:
        sequence = ""
        for line in file:
            # Skip header lines
            if line.startswith('>'):
                # If there's a sequence accumulated and a new header is found,
                # search the accumulated sequence for motifs before moving on
                if sequence:
                    for match in motif_regex.finditer(sequence):
                        print(f"Motif found in {os.path.basename(fasta_file)} at position {match.start() + 1}")
                    sequence = ""  # Reset sequence for the next record
                continue
            sequence += line.strip()

        # Check for the motif in the last sequence of the file
        if sequence:
            for match in motif_regex.finditer(sequence):
                print(f"Motif found in {os.path.basename(fasta_file)} at position {match.start() + 1}")

# Iterate over each file in the current working directory
for file_name in os.listdir('.'):
    if file_name.endswith('.fasta') or file_name.endswith('.fa'):
        find_motif_positions(file_name)

