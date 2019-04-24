import os
from gensim.models.doc2vec import Doc2Vec
from SL.functions.utils import preprocess_sentence
from SL.functions.utils import preprocess_doc
from SL.functions.utils import compare
import re
import jieba
from collections import defaultdict

model = Doc2Vec.load(os.path.join(os.getcwd(), 'SL/functions','model_hts.model'))

def clause_inspect(clauses, doc):
    clauses = clauses.split("\n")
    
    docs = preprocess_doc([t.text for t in doc.paragraphs])
    #all_ = '\n'.join(docs)
    #docs = [list(jieba.cut(d)) for d in docs]
    res = {}
    for idx, clause in enumerate(clauses):
        s = defaultdict(lambda : 0)
        c = re.compile("".join(["("+r+")?" for r in clause.strip()]))
        for row in docs:
            row_res = re.findall(c,row)
            for r in row_res:
                if len([rr for rr in r if len(rr)!=0]) > 1:
                    s[row] += len([rr for rr in r if len(rr)!=0])
        s = sorted(s.items(), key= lambda i : -i[1])
        #cla = list(jieba.cut(clause.strip()))
        #res[idx] = [(''.join(d),compare(model, cla, list(jieba.cut(d)))) for d in s] 
        #res[idx].sort(key= lambda x : -x[1])
        res[idx] = s
    return res
