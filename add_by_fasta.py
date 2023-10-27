

def add_by_fasta(fasta_name,issue_name,branch_giv=None,add_info_giv=None):
    q=open("recombinants.tsv",'r')
    existing_lines=q.readlines()
    q.close()
    existing_names={}
    for id in range(1,len(existing_lines)):
        line=existing_lines[id]
        linsp=line.split()
        #print(linsp)
        if len(linsp)>1:
            existing_names[linsp[0]]=1
        name=""
        url=""
        branch=""
        issue=""
        add_info=""

        for item in linsp:
            isb=True
            if "EPI" in item:
                isb=False
                name=item
            if '#' in item:
                isb=False
                issue=item
            if 'usher' in item:
                isb=False
                add_info=item
            if 'http' in item:
                isb=False
                url=item
            if branch=="" and isb:
                branch=item
        existing_lines[id]=name+'\t'+issue+'\t'+branch+'\t'+add_info+'\t'+url

    fasta_file=open("C:/users/xz/Downloads/"+fasta_name+'.fasta','r')
    flines=fasta_file.readlines()
    issue_name='#'+str(issue_name)
    for line in flines:
        if '>'==line[0]:
            linsp=line.split('|')
            name=linsp[0]+'|'+linsp[1]
            name=name.replace('>','').replace('hCoV-19/','')
            lineapp=name+'\t'+issue_name
            if branch_giv is not None:
                lineapp=lineapp+'\t'+str(branch_giv)
            else:
                lineapp=lineapp+'\t'
            if add_info_giv is not None:     
                lineapp=lineapp+'\t'+add_info_giv
            else:
                lineapp=lineapp+'\t'
            lineapp=lineapp+'\t'+"https://github.com/sars-cov-2-variants/lineage-proposals/issues/"+issue_name[1:]
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

w=add_by_fasta(args.fasta,args.issue,branch_giv=args.branch,add_info_giv=args.add_info)

