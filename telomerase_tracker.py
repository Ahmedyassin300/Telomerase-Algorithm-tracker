from Bio import SeqIO, AlignIO
import subprocess
import matplotlib.pyplot as plt

"""Data Collection and load sequences from a FASTA file"""
def load_sequences(file_path):
    sequences = list(SeqIO.parse(file_path, "fasta"))
    return sequences

"""Data Preprocessing"""
def preprocess_sequences(sequences, min_length=10):

# Filter out Sequences shorter than a certain length
    filtered_sequences = [seq for seq in sequences if len(seq.seq) >= min_length]
    return filtered_sequences

"""Sequence Alginment"""

def align_sequence(input_file, output_file):

# Call an external algnment tool like Muscle
    command = f"muscle -in{input_file} - out {output_file}"
    subprocess.run(command, shell=True)

"""Telemere legnth Estimation"""
def estimate_telomere_length(aligned_file, telomere_motif="TTAGGG"):
    alignment = AlignIO.read(aligned_file, "fasta")
    telomere_length = []
    for record in alignment:
        sequence = str(record.seq)
        legnth = sequence.count(telomere_motif) * len(telomere_motif)
        telomere_length.append(legnth)
    return telomere_length

"""Visualization and analysis"""
def plot_telomere_legnths(telomere_legnths):
    plt.hist(telomere_legnths, bins=20, edgecolor='black')
    plt.xlabel('Telomere Length')
    plt.ylabel('Frequency')
    plt.title('Telomere Length Track')
    plt.show()

"""Main the workflow"""
def main(file_path, aligned_output_path, min_sequence_length=10, telomere_motif="TTAGGG"):
    sequences = load_sequences(file_path)
    preprocssed_sequences = preprocess_sequences(sequences, min_sequence_length)

# Save preprocessed sequences to a temporary file
    temp_input_file = "temp_preprocessing_sequences.fasta"
    SeqIO.write(preprocess_sequences, temp_input_file, "fasta")

# Align the preprocessed sequences
    align_sequence(temp_input_file, aligned_output_path)

# Estimate telomere lengths from the aligned sequences
    telomere_length = estimate_telomere_length(aligned_output_path, telomere_motif)

# Plot the telomere length distribution
    plot_telomere_legnths(telomere_length)

"""Example Usage"""

file_path = "test_seuences.fasta"
aligned_output_path = "aligned_sequences.fasta"
main(file_path, aligned_output_path)



























