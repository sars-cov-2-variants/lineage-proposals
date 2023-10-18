

def add_by_fasta(fasta_name,issue_name,branch=None,add_info=None):
    q=open("recombinants.tsv",'r')
    existing_lines=q.readlines()
    q.close()
    existing_names={}
    for line in existing_lines[1:]:
        linsp=line.split()
        #print(linsp)
        if len(linsp)>1:
            existing_names[linsp[0]]=1
    fasta_file=open("C:/users/xz/Downloads/"+fasta_name+'.fasta','r')
    flines=fasta_file.readlines()
    issue_name='#'+str(issue_name)
    for line in flines:
        if '>'==line[0]:
            linsp=line.split('|')
            name=linsp[0]+'|'+linsp[1]
            name=name.replace('>','').replace('hCoV-19/','')
            lineapp=name+' '+issue_name
            if branch is not None:
                lineapp=lineapp+' '+branch
            if add_info is not None:
                lineapp=lineapp+' '+add_info
            if not(name in existing_names):
                existing_names[name]=1
                existing_lines.append(lineapp)

    f=open("recombinants.tsv",'w')
    for line in existing_lines:
        print(line.replace('\n',''),file=f)
    f.close()
    return 0

import argparse
parser = argparse.ArgumentParser(description='Demo of argparse')
parser.add_argument('--fasta', type=str)
parser.add_argument('--issue', type=int)
parser.add_argument('--branch', type=int,default=None)
parser.add_argument('--add_info', type=str,default=None)

args = parser.parse_args()

w=add_by_fasta(args.fasta,args.issue,args.branch,args.add_info)

