

def remove_by_issue(issue_name,branch=None):
    q=open("recombinants.tsv",'r')
    existing_lines=q.readlines()
    q.close()
    existing_names={}
    new_lines=[]
    for id in range(len(existing_lines)):
        line=existing_lines[id]
        linsp=line.split()
        #print(linsp)
        to_remove=False
        if len(linsp)<1:
            to_remove=True
        else:
            issue_seq=linsp[1]
            if str(issue_name) in issue_seq:
                to_remove=True
                if branch is not None:
                    to_remove=False
                    branch_seq=linsp[2]
                    if str(branch)==branch_seq:
                        to_remove=True
        if not(to_remove):
            new_lines.append(existing_lines[id])

    f=open("recombinants.tsv",'w')
    for line in new_lines:
        print(line.replace('\n',''),file=f)
    f.close()
    return 0

import argparse
parser = argparse.ArgumentParser(description='Demo of argparse')
parser.add_argument('--issue', type=int)
parser.add_argument('--branch', type=int,default=None)

args = parser.parse_args()

w=remove_by_issue(args.issue,args.branch)