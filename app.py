from flask import Flask, render_template, request, redirect, url_for, flash,session
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio import SeqIO, Entrez

app = Flask(__name__)
app.secret_key = 'your_secret_key'
Entrez.email = "sameer22439@iiitd.ac.in"

# Function to download gene sequence from NCBI
def download_gene_sequence(output_file, accession_number, start_pos, end_pos, reverse_complement=False):
    
    handle = Entrez.efetch(db="nucleotide", id=accession_number, rettype="fasta", seq_start=start_pos, seq_stop=end_pos)

    gene_record = SeqIO.read(handle, "fasta")

    handle.close()

    if reverse_complement: 
        gene_record.seq = gene_record.seq.reverse_complement()

    with open(output_file, "w") as file:
        SeqIO.write(gene_record, file, "fasta")

    return gene_record

# INS 1 requires reverse complement 
accession_number_INS1 = "NC_000011.10" # Accession number of INS1 gene
start_position_INS1 = 2159779 # Start position of INS1 gene
end_position_INS1 = 2161209 # End position of INS1 gene

print("Downloading INS1 gene sequence")
gene_record_INS1 = download_gene_sequence("INS1.fsa", accession_number_INS1, start_position_INS1, end_position_INS1, True)
print("Downloaded INS1 gene sequence successfully")

# INS 2 requires reverse complement
accession_number_INS2 = "NC_060935.1" # Accession number of INS2 gene
start_position_INS2 = 2247427 # Start position of INS2 gene
end_position_INS2 = 2248857 # End position of INS2 gene

print("Downloading INS2 gene sequence")
gene_record_INS2 = download_gene_sequence("INS2.fsa", accession_number_INS2, start_position_INS2, end_position_INS2, True)
print("Downloaded INS2 gene sequence successfully")



def find_and_write_snps(sequence1, sequence2, output_file):
    sequence1 = sequence1.replace("\n", "")
    sequence1 = sequence1.strip()
    sequence2 = sequence2.replace("\n", "")
    sequence2 = sequence2.strip()
    # Perform pairwise alignment
   
    alignments = pairwise2.align.globalxx(sequence1, sequence2)

    # Find SNPs
    snps = []
    for i in range(len(sequence1)):
        if sequence1[i] != sequence2[i]:
            snps.append((i+1, sequence1[i], sequence2[i]))

    # Write SNPs to file
    with open(output_file, 'w') as file:
        for position, base1, base2 in snps:
            file.write(f"{base1}{position}{base2}")
            file.write("\n")

    
   

    # Print SNPs
    print("SNPs:")
    for position, base1, base2 in snps:
        print(f"Position {position}: {base1} -> {base2}")

sequence1 = "AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACCCCAGGCCCCAGCTCTGCAGCAGGGAGGACGTGGCTGGGCTCGTGAAGCATGTGGGGGTGAGCCCAGGGGCCCCAAGGCAGGGCACCTGGCCTTCAGCCTGCCTCAGCCCTGCCTGTCTCCCAGATCACTGTCCTTCTGCCATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCTGCAGGGTGAGCCAACTGCCCATTGCTGCCCCTGGCCGCCCCCAGCCACCCCCTGCTCCTGGCGCTCCCACCCAGCATGGGCAGAAGGGGGCAGGAGGCTGCCACCCAGCAGGGGGTCAGGTGCACTTTTTTAAAAAGAAGTTCTCTTGGTCACGTCCTAAAAGTGACCAGCTCCCTGTGGCCCAGTCAGAATCTCAGCCTGAGGACGGTGTTGGCTTCGGCAGCCCCGAGATACATCAGAGGGTGGGCACGCTCCTCCCTCCACTCGCCCCTCAAACAAATGCCCCGCAGCCCATTTCTCCACCCTCATTTGATGACCGCAGATTCAAGTGTTTTGTTAAGTAAAGTCCTGGGTGACCTGGGGTCACAGGGTGCCCCACGCTGCCTGCCTCTGGGCGAACACCCCATCACGCCCGGAGGAGGGCGTGGCTGCCTGCCTGAGTGGGCCAGACCCCTGTCGCCAGGCCTCACGGCAGCTCCATAGTCAGGAGATGGGGAAGATGCTGGGGACAGGCCCTGGGGAGAAGTACTGGGATCACCTGTTCAGGCTCCCACTGTGACGCTGCCCCGGGGCGGGGGAAGGAGGTGGGACATGTGGGCGTTGGGGCCTGTAGGTCCACACCCAGTGTGGGTGACCCTCCCTCTAACCTGGGTCCAGCCCGGCTGGAGATGGGTGGGAGTGCGACCTAGGGCTGGCGGGCAGGCGGGCACTGTGTCTCCCTGACTGTGTCCTCCTGTGTCCCTCTGCCTCGCCGCTGTTCCGGAACCTGCTCTGCGCGGCACGTCCTGGCAGTGGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGCCCTTGGCCCTGGAGGGGTCCCTGCAGAAGCGTGGCATTGTGGAACAATGCTGTACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGCAACTAGACGCAGCCCGCAGGCAGCCCCACACCCGCCGCCTCCTGCACCGAGAGAGATGGAATAAAGCCCTTGAACCAGC"

l=['G326T', 'A323G', 'T322G', 'C302G', 'G293T', 'A289C', 'T286C', 'G284A', 'G266C', 'G266T', 'C163T', 'C155G', 'T147C', 'T143G', 'T143C', 'C136T', 'T127G', 'C115T', 'T104A', 'C103A', 'C103G', 'A101C', 'G95T', 'C71T', 'C71A', 'C26G', 'C16T', 'A1G']


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/search', methods=['POST'])
def process_gene_sequence():
    if request.method == 'POST':
        gene_sequence = request.form['insGeneSequence']
        if len(gene_sequence)!=len(sequence1):
            flash("Enter Correct INS Gene Sequence !",'danger')
            return redirect(url_for('homepage'))
        find_and_write_snps(sequence1, gene_sequence, "snpsList.txt")

        # Save selected symptoms to session
        selected_symptoms = request.form.getlist('symptom')  # Retrieve selected symptoms as a list
        session['selected_symptoms'] = selected_symptoms
        
        flash('Gene Sequence Processing Complete', 'success')
        return redirect(url_for('result')) 

@app.route('/result')
def result():
    flag = False
    with open("snpsList.txt", "r") as f:
        
        for i in f:
            i = i.strip()  
            i = i.replace("\n", "")  
            
    
           
            if i in l:  
                flag = True
                break        
    if flag:
        return render_template('p.html', selected_symptoms=session.get('selected_symptoms', []))
    else:
        return render_template('resultnegative.html', selected_symptoms=session.get('selected_symptoms', []))


if __name__ == "__main__":
    app.run(debug=True)



