import docx

def pay_conditions_inspect(doc_, clauses):
    #print(doc_, clauses)
    res = [idx for idx, n in enumerate(doc_.split('-')) if str(n) != clauses[idx]]
    return res
def get_seq(p):
    seq_underlines = []
    i = 0
    while i < len(p.runs):
        if p.runs[i].underline:
            s = []
            while i < len(p.runs) and p.runs[i].underline:
                s.append(p.runs[i])
                i += 1
            seq_underlines.append(s)
        i += 1
    return seq_underlines
    
def get_abc(seq_):
    a, b, c = [''.join([s.text for s in seq]).replace(' ', "") for seq in seq_]
    b = b.replace("，", "")
    b = b.replace(",", "")
    return a,b,c
    
def check(total, a,b):

    print(a*0.01*total,' -- ' ,b)

    if a*0.01*total == b:
        return True
    return False
def check_sum(total, bs):
    return sum(bs) == total
def pay_inspect(clauses, doc):
    '''	
        clauses : 2-5-2-1
    '''
    clauses_ = []
    seq_clauses = []
    total = None
    bs = []
    for para in doc.paragraphs:
        seq_ = get_seq(para)
        if len(seq_) != 3:
            continue
        a,b,c = get_abc(seq_)
        if a.find(",") == -1 and a.find("，") == -1:
            try:
                clauses_.append(str(int(a) // 10))
                seq_clauses.append(seq_[0])
            except:
                continue
            if total is None:
                raise ValueError("total is None")
            bs.append(float(b))
            if not check(total, float(a), float(b)):
                for seq in seq_:
                    for r in seq:
                        r.font.highlight_color = docx.enum.text.WD_COLOR_INDEX.YELLOW
        else:
            total = float(a.replace(',',"").replace('，',""))
            total_ = seq_[0]
    if not check_sum(total, bs):
        for se in total_:
            se.font.highlight_color = docx.enum.text.WD_COLOR_INDEX.YELLOW
    res = pay_conditions_inspect(clauses, clauses_)
    if len(res)!=0:
        for idx in res:
            seq = seq_clauses[idx]
            for r in seq:
                r.font.highlight_color = docx.enum.text.WD_COLOR_INDEX.YELLOW
    return doc

if __name__ == "__main__":
    file_path = r'C:\Users\51334\Desktop\jishu.docx'
    doc = docx.Document(file_path)
    clauses = '2-4-2-1'
    doc_ = pay_inspect(clauses, doc)
    doc_.save(r'C:\Users\51334\Desktop\test2.docx')
