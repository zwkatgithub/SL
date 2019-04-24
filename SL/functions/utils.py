import jieba
import os
import numpy as np
yuzhi = 5

with open(os.path.join(os.getcwd(),'SL/functions','stopwords.txt'), 'r', encoding='utf-8') as file:
    stopwords = file.read().split('\n')

def compare(model,s1, s2):
    
    is1 = model.infer_vector(s1)
    is2 = model.infer_vector(s2)
    ns1 = np.array(is1)
    ns2 = np.array(is2)

    return np.dot(ns1,ns2) / (np.linalg.norm(ns1,2)*np.linalg.norm(ns2,2))

def preprocess_sentence(sent):
    s = jieba.cut(''.join(sent.split()))
    #res = [r for r in s if r not in stopwords]
    return list(s)

def preprocess_doc(doc):
    res = []
    for d in doc:
        dt = ''.join(d.split())
        if len(dt) >= yuzhi:
           res.append(''.join([dd for dd in jieba.cut(dt)]))
    return res


