import os
import sys
import argparse
import re

def makeEventDict(fname, d):
    fs = open(fname, 'r')
    lc = 0
    evt = False
    rs = re.compile(r'VEVENT')
    for l in fs:
        l = l.split(':')
        m = rs.search(l[1]) 
        if (l[1][0:6] == 'VEVENT') & (l[0] == 'BEGIN'):
            lc = lc+1
            d[lc] = dict()
            evt = True
            print('New event found: %s' % lc)
        
        if (l[1][1:6] == 'VEVENT') & (l[0] == 'END'):
            evt = False
        
        if evt:
            e = d.get(lc)
            key = l[0]
            if e.get(key) == None:
                 e[key] = l[1]
                 print("%s is %s" % (key, l[1]))           
                
            
        
    

def main():
    parser = argparse.ArgumentParser(description='Convert ICS files to csv files')

    parser.add_argument('-v', '--verbose', action='store_true', help='verbose output')
    parser.add_argument('file', type=argparse.FileType('r'),  help='Input file')
    parser.add_argument('outfile', nargs='?', help='Name of the output file')
    parser.add_argument('-V','--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()
    
    global verbose
    if args.verbose:
        verbose = args.verbose
    else:
        verbose = args.verbose

    if args.file:
        fn = os.path.basename(args.file.name)
        wd = os.path.dirname(args.file.name)
        np = fn.split('.')
        fout = os.path.join(wd, np[0] + '.ics')
        
            
        if args.outfile:
            fout = os.path.join(wd, args.outfile)

    
    d = dict()  #Event dictionary
    d = makeEventDict(args.file.name, d)
    
    if verbose:
        print('Convert file: ' + os.path.abspath(args.file.name))          

#Main function call to start the program
if __name__ == "__main__":
    main()