from Bio import AlignIO
from pathlib import Path

alignment = AlignIO.read(
    "results/hbb_cds_alignment.aln",
    "clustal"
)

alignment_length = alignment.get_alignment_length()
number_of_sequences = len(alignment)

# Count conserved and variable alignment positions
conserved_positions = 0
variable_positions = 0

for column in range(alignment_length):
    nucleotides = alignment[:, column]

    if len(set(nucleotides)) == 1:
        conserved_positions += 1
    else:
        variable_positions += 1

conserved_percentage = (
    conserved_positions / alignment_length
) * 100

variable_percentage = (
    variable_positions / alignment_length
) * 100

print("CDS ALIGNMENT ANALYSIS")
print("----------------------")
print(f"Number of sequences: {number_of_sequences}")
print(f"Alignment length: {alignment_length} nucleotides")
print(f"Conserved positions: {conserved_positions}")
print(f"Conserved percentage: {conserved_percentage:.2f}%")
print(f"Variable positions: {variable_positions}")
print(f"Variable percentage: {variable_percentage:.2f}%")

print("\nGAP ANALYSIS")
print("------------")

for record in alignment:
    gap_count = record.seq.count("-")
    print(f"{record.id}: {gap_count} gaps")

output_path = Path("results/cds_conservation_results.txt")

with output_path.open("w") as output:
    output.write("CDS ALIGNMENT ANALYSIS\n")
    output.write("----------------------\n")
    output.write(f"Number of sequences: {number_of_sequences}\n")
    output.write(f"Alignment length: {alignment_length}\n")
    output.write(f"Conserved positions: {conserved_positions}\n")
    output.write(f"Conserved percentage: {conserved_percentage:.2f}%\n")
    output.write(f"Variable positions: {variable_positions}\n")
    output.write(f"Variable percentage: {variable_percentage:.2f}%\n")

    output.write("\nGAP ANALYSIS\n")
    output.write("------------\n")

    for record in alignment:
        gap_count = record.seq.count("-")
        output.write(f"{record.id}: {gap_count} gaps\n")

print(f"\nResults saved to: {output_path}")

