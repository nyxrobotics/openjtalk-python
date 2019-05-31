#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding: UTF-8
import subprocess
import re
import sys
from datetime import datetime
 
def jtalk(t):
    echo = 'echo'+' '+t+'|'
    open_jtalk = '~/lib/openjtalk_libs/open_jtalk-1.11/bin/open_jtalk'+ ' '
    dic ='-x' + ' ' + '~/lib/openjtalk_libs/open_jtalk_dic_utf_8-1.11' + ' '
    htsvoice ='-m' + ' ' + '~/lib/openjtalk_libs/MMDAgent_Example-1.8/Voice/mei/mei_happy.htsvoice' + ' '
    speed='-r' + ' ' +'1.0 '
    outwav='-ow' + ' ' +'/dev/stdout | aplay --quiet'
    cmd=echo+open_jtalk+dic+htsvoice+speed+outwav
    # print(cmd)
    proc = subprocess.run(cmd,shell  = True)

def jtalk_quick(t):
    echo = 'echo'+' '+t+'|'
    open_jtalk = '~/lib/openjtalk_libs/open_jtalk-1.11/bin/open_jtalk'+ ' '
    dic ='-x' + ' ' + '~/lib/openjtalk_libs/open_jtalk_dic_utf_8-1.11' + ' '
    htsvoice ='-m' + ' ' + '~/lib/openjtalk_libs/MMDAgent_Example-1.8/Voice/mei/mei_happy.htsvoice' + ' '
    speed='-r' + ' ' +'1.0 '
    outwav='-ow' + ' ' +'/dev/stdout | aplay --quiet'
    cmd=echo+open_jtalk+dic+htsvoice+speed+outwav
    proc = subprocess.Popen(cmd,stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True)
    # proc.wait()

def jtalk_wait(t):
    echo = 'echo'+' '+t+'|'
    open_jtalk = '~/lib/openjtalk_libs/open_jtalk-1.11/bin/open_jtalk'+ ' '
    dic ='-x' + ' ' + '~/lib/openjtalk_libs/open_jtalk_dic_utf_8-1.11' + ' '
    htsvoice ='-m' + ' ' + '~/lib/openjtalk_libs/MMDAgent_Example-1.8/Voice/mei/mei_happy.htsvoice' + ' '
    speed='-r' + ' ' +'1.0 '
    outwav='-ow' + ' ' +'/dev/stdout | aplay --quiet --device=default'
    cmd=echo+open_jtalk+dic+htsvoice+speed+outwav
    # proc = subprocess.Popen(cmd,stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True)
    # proc.wait()
    proc = subprocess.call(cmd,shell=True)

def say_datetime():
    d = datetime.now()
    text = '%s月%s日、%s時%s分%s秒' % (d.month, d.day, d.hour, d.minute, d.second)
    jtalk('只今の時刻は' + text + 'です。')

def say_longtext(longtext_in):
    longtext = longtext_in

    longtext=re.sub(r' ', "、", longtext)#半角スペース
    longtext=re.sub(r'　', "、", longtext)#全角スペース
    longtext=re.sub(r'\n', "。", longtext)#改行
    longtext=re.sub(r'ゝ', "ー、", longtext)#繰り返し記号
    longtext=re.sub(r'」', "、", longtext)#かぎかっこ
    longtext=re.sub(r'「', "、", longtext)#かぎかっこ
    longtext=re.sub(r'！', "っ。", longtext)#びっくり
    longtext=re.sub(r'!', "っ。", longtext)#びっくり
    longtext=re.sub(r'。、', "。", longtext)#その他
    longtext=re.sub(r'。。', "。", longtext)#その他
    longtext=re.sub(r'。 ', "。", longtext)#その他
    longtext=re.sub(r'。　', "。", longtext)#その他
    longtext=re.sub(r'―', "", longtext)#その他
    longtext=re.sub(r'\.', "。", longtext)#句読点
    longtext=re.sub(r'．', "。", longtext)#句読点
    longtext=re.sub(r',', "、", longtext)#句読点
    longtext=re.sub(r'，', "、", longtext)#句読点
    longtext=re.sub(r'。\\1', "。",longtext)#複数連続

    list1 = longtext.split('。')
    for num1 in range(len(list1)):
        text = list1[num1]
        text=re.sub(r'[!-/:-@[-`{-~]', "、", text)#半角記号,数字,英字
        text=re.sub(r'[︰-＠]', "、", text)#全角記号
        text=re.sub(r'、\\1', "、", text)#複数連続

        if len(text) > 50:#文字数が多すぎるときは読点でも分割
            list2 = text.split('、')
            for num2 in range(len(list2)):
                text = list2[num2]
                if len(text) < 50 and text != "":#それでも多かったら無視
                    jtalk_wait(text + "、")
        else:
            if text != "":
                jtalk_wait(text + "〜っ、。")#語尾を適当に調整
                # print(text)

def main():
    # text = 'こんにちは、テストです。文章区切りの検証をします。'
    # say_longtext(text)
    # say_datetime()
    print("文字を入力してください。(Ctrl + d で入力完了)")
    # text=input()
    text=sys.stdin.read().decode("UTF-8")
    say_longtext(text)
    # jtalk_wait(text)



if __name__ == '__main__':
    main()
