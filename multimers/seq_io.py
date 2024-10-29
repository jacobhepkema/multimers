import argparse
from Bio import SeqIO
import matplotlib.pyplot as plt

def parse_arguments():
    parser = argparse.ArgumentParser(description="Process a FASTQ file from ONT whole plasmid sequencing and plot read lengths.")
    parser.add_argument("fastq_path", help="Path to the FASTQ file from ONT whole plasmid sequencing.")
    parser.add_argument("-o", "--output", default="read_lengths.png", help="Output file name for the plot (optional).")
    parser.add_argument("-p", "--plasmid_len", type=int, help="Plasmid length (optional).")
    return parser.parse_args()

def main():
    args = parse_arguments()
    fastq_path = args.fastq_path
    output = args.output
    plasmid_len = args.plasmid_len

    all_lens = []
    for record in SeqIO.parse(fastq_path, 'fastq'):
        read_len = len(record.seq)
        if plasmid_len:
            read_len /= plasmid_len  # Normalize by plasmid length if provided
        all_lens.append(read_len)

    plt.hist(all_lens, bins=30, color="skyblue", edgecolor="black")
    xlabel = "Multiplicity" if plasmid_len else "Read Length"
    plt.xlabel(xlabel)
    plt.ylabel("Frequency")
    plt.title("Distribution of Read Lengths" if not plasmid_len else "Distribution of Read Multiplicities")
    plt.savefig(output)

if __name__ == '__main__':
    main()

