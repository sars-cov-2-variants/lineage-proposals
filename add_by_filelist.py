def add_by_file(file_name,issue_name):
    q=open("recombinants.tsv",'r')
    existing_lines=q.readlines()
    q.close()
    existing_names={}
    for id in range(1,len(existing_lines)):
        line=existing_lines[id]
        linsp=line.split()
        #print(linsp)
        if len(linsp)>1:
            nn=linsp[0].strip()
            if 'EPI_ISL' in nn:
                nnp=nn.split("EPI_ISL_")[1]
                existing_names["EPI_ISL_"+nnp]=1
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
            if 'C_AA' in item:
                isb=False
                name=item
            if branch=="" and isb:
                branch=item
        existing_lines[id]=name+'\t'+issue+'\t'+branch+'\t'+add_info+'\t'+url

    f_file=open(file_name,'r')
    flines=f_file.readlines()
    if issue_name[0]>='0' and issue_name[0]<='9':
        issue_name='#'+issue_name
    for line in flines:
        if len(line)<5:
            continue
        linsp=line.strip().split(' ')
        
        if len(linsp)==1:
            name="EPI_ISL_"+linsp[0]
        else:
            for w in linsp:
                if "EPI_ISL" in w:
                    name=w

        if not(name in existing_names):
            lineapp=name+'\t'+issue_name
                
            lineapp=lineapp+'\t'
        
        
            lineapp=lineapp+'\t'
            if '#' in issue_name:
                lineapp=lineapp+'\t'+"https://github.com/sars-cov-2-variants/lineage-proposals/issues/"+issue_name[1:]
            else:
                lineapp=lineapp+'\t'
            print(name,name in existing_names)
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
parser.add_argument('--file', type=str)
parser.add_argument('--issue', type=str)

args = parser.parse_args()

w=add_by_file(args.file,args.issue)

