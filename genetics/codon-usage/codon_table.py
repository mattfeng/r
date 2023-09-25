import click

@click.command()
@click.argument("codon_usage_file")
def generate_codon_table(codon_usage_file):
	usage = []
	with open(codon_usage_file) as f:
		f.readline()

		for line in f:
			line = line.strip()

			aa, codon, _, per1000, _ = line.split()
			per1000 = float(per1000)

			if aa == "End":
				aa = "_STOP"

			usage.append((aa, codon, per1000))

	usage = sorted(usage, key=lambda x: (x[0], x[1], x[2]))

	print("Amino Acid,Codon,Usage")
	for entry in usage:
		print(",".join(map(str,entry)))


if __name__ == "__main__":
	generate_codon_table()