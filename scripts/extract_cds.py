from Bio import Entrez, SeqIO
from Bio.SeqRecord import SeqRecord
from pathlib import Path

Entrez.email = "srsatt10@gmail.com"

accessions = {
    "Human": "NM_000518.5",
    "Chimpanzee": "XM_508242.5",
    "Cow": "NM_173917.2",
    "Mouse": "NM_001278161.1"
}

output_dir = Path("data")
output_dir.mkdir(exist_ok=True)

cds_records = []

for species, accession in accessions.items():
    print(f"Downloading {species} record...")

    with Entrez.efetch(
        db="nuccore",
        id=accession,
        rettype="gb",
        retmode="text"
    ) as handle:
        record = SeqIO.read(handle, "genbank")

    cds_features = [
        feature for feature in record.features
        if feature.type == "CDS"
    ]

    if not cds_features:
        print(f"No CDS feature found for {species}. Skipping.")
        continue

    cds_feature = cds_features[0]
    cds_sequence = cds_feature.extract(record.seq)

    print("CDS location:", cds_feature.location)
    print("CDS qualifiers:", cds_feature.qualifiers)

    print(f"{species}: CDS length = {len(cds_sequence)} nt")

    cds_records.append(
        SeqRecord(
            cds_sequence,
            id=species,
            description=accession
        )
    )

output_file = output_dir / "hbb_cds.fasta"
SeqIO.write(cds_records, output_file, "fasta")

print(f"\nCDS sequences saved to: {output_file}")