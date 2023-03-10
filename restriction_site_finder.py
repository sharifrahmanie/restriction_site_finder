import re
def restriction_site_finder(pattern, sequence):
    sequence = sequence.upper()
    pattern = pattern.upper()
    match = re.findall(pattern, sequence)
    site = re.finditer(pattern, sequence)
    p = [s.start() for s in site]
    if len(match) == 0:
        print("No match found.")
    else:
        for i in range(0, len(match)):
            print("Restriction site for ",match[i], " found at ",p[i])
        
EcoR1 = "GAATTC"
sequence = "AGCTAGCTGCTAGCGAATTCTAGCTAGCTAGCTAAGCTAGCTCTAGAATTCGCTAGCTAGCTAGCTAGCTAGCT"
restriction_site_finder(EcoR1, sequence)
# @sharifrahmanie
