

def remove_by_issue(issue_name,branch=None,mode=None):
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
            try:
                issue_num=int(issue_seq.strip()[1:])
            except:
                issue_num=1000000
            issue_link=linsp[-1]
            if str(issue_name) in issue_seq:
                to_remove=True
                if branch is not None:
                    to_remove=False
                    branch_seq=linsp[2]
                    if str(branch)==branch_seq:
                        to_remove=True
            if mode=='before':
                if issue_num<=issue_name:
                    if 'lineage-proposals' in issue_link:
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
parser.add_argument('--issue', type=int,default=0)
parser.add_argument('--mode', type=str,default=None)
parser.add_argument('--branch', type=int,default=None)

args = parser.parse_args()

w=remove_by_issue(args.issue,args.branch,args.mode)