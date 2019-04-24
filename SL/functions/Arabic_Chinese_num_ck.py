import argparse
import sys

parser=argparse.ArgumentParser(description="This script aims to judge whether Chinese capitalized numerals matching Arabic numerals.")
args=parser.parse_args()

def change(num):
    strCapital="零壹贰叁肆伍陆柒捌玖" #0-9所对应的汉字
    strCapitalUnit="万仟佰拾亿仟佰拾万仟佰拾元角分" #金额单位所对应的汉字
    strCapitalMoney="" #人民币大写金额形式
    capitalNum="" #数字的汉语读法
    capitalUnit="" #数字位的汉字读法
    countZero=0 #用来计算连续的零值是几个
    temp=0 #从原num值中取出的值
    num=round(abs(num),2) #将num取绝对值并四舍五入取两位小数
    strNum=str(round(num*100)) #将num中的小数点去除，并转换成字符串形式
    #print("%.2f %s"%(num,strNum))
    j=len(strNum) #金额总长度（排除小数点），如101.01的j=5
    if j>15:
        return "溢出" #限制合同金额在万亿以下
    strCapitalUnit=strCapitalUnit[(15-j):] #取出对应位数的所有单位值。如：101.01，j为5，所以strCapitalUnit="佰拾元角分"
    strTempNum="" #用于存放从num值中依次取出的值，进行循环转换
    #循环取出每一位需要转换的值
    for i in range(j):
        strTempNum=strNum[i] #循环取出需转换的每一位的值
        temp=int(strTempNum) #转换为数字
        if i!=(j-3) and i!=(j-7) and i!=(j-11) and i!=(j-15): #当所取位数不为元、万、亿、万亿上的数字时
            if strTempNum=="0":
                capitalNum=""
                capitalUnit=""
                countZero=countZero+1
            else:
                if strTempNum!="0" and countZero!=0:
                    capitalNum="零"+strCapital[temp*1]
                    capitalUnit=strCapitalUnit[i]
                    countZero=0
                else:
                    capitalNum=strCapital[temp*1]
                    capitalUnit=strCapitalUnit[i]
                    countZero=0
        else:#该位是万亿、亿、万、元位等关键位
            if strTempNum!="0" and countZero!=0:
                capitalNum="零"+strCapital[temp*1]
                capitalUnit=strCapitalUnit[i]
                countZero=0
            else:
                if strTempNum!="0" and countZero==0:
                    capitalNum=strCapital[temp*1]
                    capitalUnit=strCapitalUnit[i]
                    countZero=0
                else:
                    if strTempNum=="0" and countZero>=3:
                        capitalNum=""
                        capitalUnit=""
                        countZero=countZero+1
                    else:
                        if j>=11:
                            capitalNum=""
                            countZero=countZero+1
                        else:
                            capitalNum=""
                            capitalUnit=strCapitalUnit[i]
                            countZero=countZero+1
        if i==j-11 or i==j-3: #如果该位是亿位或元位，则必须写上
            capitalUnit=strCapitalUnit[i]
        strCapitalMoney=strCapitalMoney+capitalNum+capitalUnit
        if i==j-1 and strTempNum=="0": #最后一位（分）为0时，加上“整”
            strCapitalMoney=strCapitalMoney+"整"
    if num==0:
        strCapitalMoney="零元整"
    return strCapitalMoney

def check(Arabic_number="1234567.89",Chinese_number="壹佰贰拾叁万肆仟伍佰陆拾柒元捌角玖分"):
    #print("%f %s"%(float(Arabic_number),change(float(Arabic_number))))
    if change(float(Arabic_number)) == Chinese_number:
        #print("检查正确")
        return True
    else:
        #print("检查错误")
        return False

if __name__=='__main__':
    check()