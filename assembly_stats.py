import numpy
import screed
import sys


def load_assembly(filename, mincontig):
    d = {}
    for record in screed.open(filename):
        if len(record.sequence) >= mincontig: 
              d[record.name.split()[0]] = len(record.sequence)
    return d

def largest_contigs(d): 
    ncontigs =sorted(d.values(),reverse=True)
    return ncontigs[0]

def total_length(d): 
    total =0
    for key in d: 
        total+= d[key] 
    return total 

def main():
    filename1 =sys.argv[1]
    mincontig =int(sys.argv[2])
    d =load_assembly(filename1, mincontig)
    lc =largest_contigs(d) 
    print 'Largest contigs length is ', lc
    total =total_length(d) 
    print 'Total Length is ', total 

if __name__ == '__main__':
    main()
