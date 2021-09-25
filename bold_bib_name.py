
import bibtexparser

def add_bold(input_file, output_file):
    "Bold paper name in the name domain by adding \bold"

    with open(input_file) as bibtex_file:
        bibtex_str = bibtex_file.read()
    bib_database = bibtexparser.loads(bibtex_str)
    for entry in bib_database.entries:
        name = entry['title']
        entry["title"] = "{\\textcolor{purple}{\\textbf{" + name + "}}}"
    
    with open(output_file, 'w') as bibtex_file:
        bibtexparser.dump(bib_database, bibtex_file)
    
    print("Successfully add bold!")

def remove_bold(input_file, output_file):
    "Remove bold in name domain"
    with open(input_file) as bibtex_file:
        bibtex_str = bibtex_file.read()
    bib_database = bibtexparser.loads(bibtex_str)
    for entry in bib_database.entries:
        name = entry['title']
        entry["title"] = name[28:-3]
    
    with open(output_file, 'w') as bibtex_file:
        bibtexparser.dump(bib_database, bibtex_file)
    
    print("Successful remove bold!")


if __name__ == '__main__':
    add_bold("papers.bib", "papers.bib")
    # remove_bold("papers.bib", "papers.bib")

