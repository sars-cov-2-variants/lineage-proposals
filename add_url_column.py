def add_url_column():
    q=open("recombinants.tsv",'r')
    existing_lines=q.readlines()
    q.close()
    existing_names={}
    existing_lines[0]=existing_lines[0]+'\t'+'url'
    for id in range(1,len(existing_lines)):
        
        line=existing_lines[id]
        linsp=line.split()
        #print(linsp)
        if len(linsp)>1:
            existing_names[linsp[0]]=1
        existing_lines[id]=line.replace(' ','\t')
        existing_lines[id]=existing_lines[id].replace('\t\t','\t')
        num=0
        issue_num=linsp[1]
        for ch in existing_lines[id]:
            if ch=='\t':
                num+=1
        while num>3:
            existing_lines[id]=existing_lines[id].replace('\t\t','\t')
            num-=1
        while num<3:
            existing_lines[id]=existing_lines[id]+'\t'
            num+=1
        existing_lines[id]=existing_lines[id]+'\t'+"https://github.com/sars-cov-2-variants/lineage-proposals/issues/"+issue_num[1:]

    f=open("recombinants.tsv",'w')
    for line in existing_lines:
        print(line.replace('\n',''),file=f)
    f.close()
    return 0

w=add_url_column()

