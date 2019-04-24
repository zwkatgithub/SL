import docx
import re
from SL.functions.Docx import Docx
from SL.functions.Arabic_Chinese_num_ck import check
from SL.functions.pay_conditions import get_seq

def num_case_inspect(doc):
    patstr = '￥[\s]*[\d+(，|,)]*[0-9]+[.[0-9]+]?[\s]*元（(?:大写|大写金额)：\s*\S*）'
    Arabic_Number = '\d+|[.\d+]'
    Chinese1_Number = '(?<=（大写：).+?(?=）)'
    Chinese2_Number = '(?<=（大写金额：).+?(?=）)'
    patCapital='零?壹?贰?叁?肆?伍?陆?柒?捌?玖?万?亿?仟?佰?拾?元?角?分?'

    for p in doc.paragraphs:
        match=re.findall(patstr,p.text)
        if(len(match)!=0):
            num_str=''
            ch_str=''
            for s in match:
                for n in re.findall(Arabic_Number,s):
                    num_str+=n
                num_str.strip()
                if re.findall(Chinese1_Number, s):
                    ch_str += re.findall(Chinese1_Number, s)[0].strip()
                else:
                    ch_str += re.findall(Chinese2_Number, s)[0].strip()
                # print('结果是：',num_str,ch_str)
                if not check(num_str,ch_str):
                    seq_ = get_seq(p)
                    for idx, se in enumerate(seq_):
                        t = ''.join([s.text for s in se])
                        try:
                            a = float(t.replace(',','').replace('，',''))
                            for r in seq_[idx]:
                                Docx.markedYellow(r)
                            for r in seq_[idx+1]:
                                Docx.markedYellow(r)
                        except:
                            continue
                    #for r in p.runs:
                    #    if len(re.findall(patCapital,r.text))!=0:
                    #        Docx.markedYellow(r)
    return doc