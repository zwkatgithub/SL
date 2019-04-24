import docx
from SL.functions.Docx import Docx


def is_space(r):
    if r.underline and r.text.isspace():
        return True
    return False
def readfile(filename):
    return docx.Document(filename)



def ht_space_inspect(doc):
    
    for p in doc.paragraphs:
        flag = True
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
        for seq in seq_underlines:
            for r in seq:
                if not r.text.isspace() and not r.text.strip() == '\\':
                    flag = False
            if flag:
                for r in seq:
                    Docx.markedYellow(r)

    return doc

if __name__ == "__main__":
    doc = readfile('test2.docx')
    ht_space_inspect(doc)
    doc.save('test3.docx')

