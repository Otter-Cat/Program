import random
import time
import msvcrt
import os
import base64
from os import system as cmd

cmd("title 加解密小程序")
print("加解密小程序，Made By.OtterCat \n ver. 1.0.0 請勿隨意修改程序碼")
print("3秒後即將開始！")
time.sleep(3)
cmd("cls")

#加密用
baseOT = {
    "1": "OTKv79",
    "2": "OTrT70",
    "3": "OTLw07",
    "4": "OTgb57",
    "5": "OTFS63",
    "6": "OTyw43",
    "7": "OTdI59",
    "8": "OTjV94",
    "9": "OTDF79",
    "0": "OTDA46",
    "Q": "OTIP80",
    "W": "OTHm98",
    "E": "OTIk61",
    "R": "OTCK10",
    "T": "OTXw40",
    "Y": "OTgS24",
    "U": "OTRI23",
    "I": "OTPf52",
    "O": "OTRg79",
    "P": "OTsT82",
    "A": "OTEr20",
    "S": "OTgF51",
    "D": "OTEc23",
    "F": "OTCj42",
    "G": "OTqI51",
    "H": "OTsp75",
    "J": "OTiV36",
    "K": "OTAR80",
    "L": "OTGK62",
    "Z": "OTXE97",
    "X": "OTOn47",
    "C": "OTHp98",
    "V": "OTgQ04",
    "B": "OTDC57",
    "N": "OTzW90",
    "M": "OTQP58",
    "q": "OTeT52",
    "w": "OTMy21",
    "e": "OTzB64",
    "r": "OTFN72",
    "t": "OTnH14",
    "y": "OTte67",
    "u": "OTRb90",
    "i": "OTUD53",
    "o": "OTyw60",
    "p": "OTtG52",
    "a": "OTTY29",
    "s": "OTKc46",
    "d": "OTlM46",
    "f": "OTeo51",
    "g": "OTag79",
    "h": "OTba26",
    "j": "OTft76",
    "k": "OTtS79",
    "l": "OTZT85",
    "z": "OTHA15",
    "x": "OTnh80",
    "c": "OTKc15",
    "v": "OThw12",
    "b": "OTwQ57",
    "n": "OTGx63",
    "m": "OTUm27"
}
caser = {
    '1': '4',
    '2': '5',
    '3': '6',
    '4': '7',
    '5': '8',
    '6': '9',
    '7': '0',
    '8': '1',
    '9': '2',
    '0': '3',
    'Q': 'T',
    'W': 'Z',
    'E': 'H',
    'R': 'U',
    'T': 'W',
    'Y': 'B',
    'U': 'X',
    'I': 'L',
    'O': 'R',
    'P': 'S',
    'A': 'D',
    'S': 'V',
    'D': 'G',
    'F': 'I',
    'G': 'K',
    'H': 'M',
    'J': 'N',
    'K': 'O',
    'L': 'C',
    'Z': 'Y',
    'X': 'E',
    'C': 'F',
    'V': 'K',
    'B': 'o',
    'N': 't',
    'M': 'h',
    'q': 'u',
    'w': 'x',
    'e': '1',
    'r': 'l',
    't': 'v',
    'y': 'i',
    'u': 'm',
    'i': 'p',
    'o': 'b',
    'p': 'g',
    'a': 'm',
    's': 'o',
    'd': 'q',
    'f': 'r',
    'g': 'v',
    'h': 'c',
    'j': 'w',
    'k': 'f',
    'l': 'd',
    'z': 'y',
    'x': 'e',
    'c': 'j',
    'v': 'p',
    'b': 'k',
    'n': 'o',
    'm': 'q'
}
morse = {
    '1': '· - - - -',
    '2': '· · - - -',
    '3': '· · · - -',
    '4': '· · · · -',
    '5': '· · · · ·',
    '6': '- · · · ·',
    '7': '- - · · ·',
    '8': '- - - · ·',
    '9': '- - - - ·',
    '0': '- - - - -',
    'Q': '- - · - ·',
    'W': '· - -',
    'E': '·',
    'R': '· - ·',
    'T': '-',
    'Y': '- · - -',
    'U': '· · -',
    'I': '· ·',
    'O': '- - -',
    'P': '· - - ·',
    'A': '· -',
    'S': '· · ·',
    'D': '- · ·',
    'F': '· · - ·',
    'G': '- - ·',
    'H': '· · · ·',
    'J': '· - - -',
    'K': '- · -',
    'L': '· - · ·',
    'Z': '- - · ·',
    'X': '- · · -',
    'C': '- · - ·',
    'V': '· · · -',
    'B': '- · · ·',
    'N': '- ·',
    'M': '- -',
    'q': '- - · - ·',
    'w': '· - -',
    'e': '·',
    'r': '· - ·',
    't': '-',
    'y': '- · - -',
    'u': '· · -',
    'i': '· ·',
    'o': '- - -',
    'p': '· - - ·',
    'a': '· -',
    's': '· · ·',
    'd': '- · ·',
    'f': '· · - ·',
    'g': '- - ·',
    'h': '· · · ·',
    'j': '· - - -',
    'k': '- · -',
    'l': '· - · ·',
    'z': '- - · ·',
    'x': '- · · -',
    'c': '- · - ·',
    'v': '· · · -',
    'b': '- · · ·',
    'n': '- ·',
    'm': '- -'
}
#解密用
baseOT_Raw ={
    "OTKv79": "1",
    "OTrT70": "2",
    "OTLw07": "3",
    "OTgb57": "4",
    "OTFS63": "5",
    "OTyw43": "6",
    "OTdI59": "7",
    "OTjV94": "8",
    "OTDF79": "9",
    "OTDA46": "0",
    "OTIP80": "Q",
    "OTHm98": "W",
    "OTIk61": "E",
    "OTCK10": "R",
    "OTXw40": "T",
    "OTgS24": "Y",
    "OTRI23": "U",
    "OTPf52": "I",
    "OTRg79": "O",
    "OTsT82": "P",
    "OTEr20": "A",
    "OTgF51": "S",
    "OTEc23": "D",
    "OTCj42": "F",
    "OTqI51": "G",
    "OTsp75": "H",
    "OTiV36": "J",
    "OTAR80": "K",
    "OTGK62": "L",
    "OTXE97": "Z",
    "OTOn47": "X",
    "OTHp98": "C",
    "OTgQ04": "V",
    "OTDC57": "B",
    "OTzW90": "N",
    "OTQP58": "M",
    "OTeT52": "q",
    "OTMy21": "w",
    "OTzB64": "e",
    "OTFN72": "r",
    "OTnH14": "t",
    "OTte67": "y",
    "OTRb90": "u",
    "OTUD53": "i",
    "OTyw60": "o",
    "OTtG52": "p",
    "OTTY29": "a",
    "OTKc46": "s",
    "OTlM46": "d",
    "OTeo51": "f",
    "OTag79": "g",
    "OTba26": "h",
    "OTft76": "j",
    "OTtS79": "k",
    "OTZT85": "l",
    "OTHA15": "z",
    "OTnh80": "x",
    "OTKc15": "c",
    "OThw12": "v",
    "OTwQ57": "b",
    "OTGx63": "n",
    "OTUm27": "m"
}
caser_Raw ={
    '4': '1',
    '5': '2',
    '6': '3',
    '7': '4',
    '8': '5',
    '9': '6',
    '0': '7',
    '1': '8',
    '2': '9',
    '3': '0',
    'T': 'Q',
    'Z': 'W',
    'H': 'E',
    'U': 'R',
    'W': 'T',
    'B': 'Y',
    'X': 'U',
    'L': 'I',
    'R': 'O',
    'S': 'P',
    'D': 'A',
    'V': 'S',
    'G': 'D',
    'I': 'F',
    'K': 'G',
    'M': 'H',
    'N': 'J',
    'O': 'K',
    'C': 'L',
    'Y': 'Z',
    'E': 'X',
    'F': 'C',
    'K': 'V',
    'o': 'B',
    't': 'N',
    'h': 'M',
    'u': 'q',
    'x': 'w',
    '1': 'e',
    'l': 'r',
    'v': 't',
    'i': 'y',
    'm': 'u',
    'p': 'i',
    'b': 'o',
    'g': 'p',
    'm': 'a',
    'o': 's',
    'q': 'd',
    'r': 'f',
    'v': 'g',
    'c': 'h',
    'w': 'j',
    'f': 'k',
    'd': 'l',
    'y': 'z',
    'e': 'x',
    'j': 'c',
    'p': 'v',
    'k': 'b',
    'o': 'n',
    'q': 'm'
}
morse_Raw = {
    '· - - - -': '1',
    '· · - - -': '2',
    '· · · - -': '3',
    '· · · · -': '4',
    '· · · · ·': '5',
    '- · · · ·': '6',
    '- - · · ·': '7',
    '- - - · ·': '8',
    '- - - - ·': '9',
    '- - - - -': '0',
    '- - · - ·': 'Q',
    '· - -': 'W',
    '·': 'E',
    '· - ·': 'R',
    '-': 'T',
    '- · - -': 'Y',
    '· · -': 'U',
    '· ·': 'I',
    '- - -': 'O',
    '· - - ·': 'P',
    '· -': 'A',
    '· · ·': 'S',
    '- · ·': 'D',
    '· · - ·': 'F',
    '- - ·': 'G',
    '· · · ·': 'H',
    '· - - -': 'J',
    '- · -': 'K',
    '· - · ·': 'L',
    '- - · ·': 'Z',
    '- · · -': 'X',
    '- · - ·': 'C',
    '· · · -': 'V',
    '- · · ·': 'B',
    '- ·': 'N',
    '- -': 'M',
    '- - · - ·': 'q',
    '· - -': 'w',
    '·': 'e',
    '· - ·': 'r',
    '-': 't',
    '- · - -': 'y',
    '· · -': 'u',
    '· ·': 'i',
    '- - -': 'o',
    '· - - ·': 'p',
    '· -': 'a',
    '· · ·': 's',
    '- · ·': 'd',
    '· · - ·': 'f',
    '- - ·': 'g',
    '· · · ·': 'h',
    '· - - -': 'j',
    '- · -': 'k',
    '· - · ·': 'l',
    '- - · ·': 'z',
    '- · · -': 'x',
    '- · - ·': 'c',
    '· · · -': 'v',
    '- · · ·': 'b',
    '- ·': 'n',
    '- -': 'm'
}
while True:
    while True:
        print("目前支持的加密方式:\n base64 \n baseOT--只支持英文及數字 \n 凱薩加密--只支持英文及數字 \n 摩斯密碼--只支持英文及數字 \n\n")#(base64 , baseOT, caesar cipher, morse code)
        Uinput = input("請選擇你要加密(E)還是解密(D):\n > > > ")
        if Uinput == "E":
            print("(若程序崩潰表輸入內容無法成功編碼，請刪除空格或其他字元，並重新啟動程序。)")
            text = input("請輸入你要編碼的文字:\n > > > ")
            print("\n\n編碼中")
            time.sleep(3)
            text_A = text.encode('UTF-8')
            answer_A = base64.b64encode(text_A)
            answer_A = answer_A.decode('UTF-8').replace("b", "").replace("'", "").replace("=", "")
            text_B = list(text)
            answer_B = ""
            fountion = 0
            for char in text:
                if char in baseOT:
                    first = text_B[fountion]
                    answer_vir = baseOT[first]
                    answer_B += answer_vir
                    fountion += 1
                else:
                    answer_B = "ERROR 無法加密，請確認是否有錯誤的字元或空格。"
            text_C = list(text)
            answer_C = ""            
            fountion = 0
            for char in text:
                if char in caser:
                    first = text_C[fountion]
                    answer_vir = caser[first]
                    answer_C += answer_vir
                    fountion += 1
                else:
                    answer_C = "ERROR 無法加密，請確認是否有錯誤的字元或空格。"
            text_D = list(text)
            answer_D = ""
            fountion = 0
            for char in text:
                if char in morse:
                    first = text_D[fountion]
                    answer_vir = morse[first]
                    answer_D += answer_vir
                    answer_D += "/"
                    fountion += 1
                else:
                    answer_D = "ERROR 無法加密，請確認是否有錯誤的字元或空格。"
            cmd("cls")
            print(text, "為原文\n\n")
            print("Base64\n", answer_A)
            print("baseOT\n", answer_B)
            print("凱薩加密\n",answer_C)
            print("摩斯密碼\n",answer_D)
            break

        elif Uinput == "D":
            print("(若程序崩潰表輸入內容無法解碼，請確認輸入內容開頭沒有包含空格，並重新啟動程序。)")
            text = input("請輸入你要解碼的亂碼: \n > > > ")
            BOJI = input('請輸入解碼方式"base64(B), baseOT(O), 凱薩加密(C), 摩斯密碼(M)":\n > > > ')
            print("\n\n解碼中")
            time.sleep(3)
            if BOJI == "B":
                text_A = text.encode('UTF-8')
                answer_A = base64.b64decode(text_A)
                answer_A = answer_A.decode('UTF-8').replace("b", "").replace("'", "").replace("=", "")
                cmd("cls")
                print(text, "為原文\n\n")
                print(answer_A)
            elif BOJI == "P":
                text_B_Raw = text
                six = 6
                text_B = []
                for i in range(0, len(text_B_Raw), six):
                    chunk = text_B_Raw[i:i + six]
                    text_B.append(chunk)
                fountion = 0
                answer_B_Raw = []
                for char in text_B:
                    if char in baseOT_Raw:
                        first = text_B[fountion]
                        answer_vir = baseOT_Raw[first]
                        answer_B_Raw += answer_vir
                        fountion += 1
                    else:
                        answer_B_Raw = "ERROR 無法解密，請確認是否有錯誤的字元或空格。"
                answer_B = "".join(answer_B_Raw)
                cmd("cls")
                print(text, "為原文\n\n")
                print(answer_B)
            elif BOJI == "C":
                text_C = list(text)
                answer_C = ""            
                fountion = 0
                for char in text:
                    if char in caser_Raw:
                        first = text_C[fountion]
                        answer_vir = caser_Raw[first]
                        answer_C += answer_vir
                        fountion += 1
                    else:
                        answer_C = "ERROR 無法解密，請確認是否有錯誤的字元或空格。"
                cmd("cls")
                print(text, "為原文\n\n")
                print(answer_C)
            elif BOJI == "M":
                text_D = text.split("/")
                if text_D[-1] == "":
                    text_D.pop()
                fountion = 0
                answer_D = ""
                for char in text_D:
                    if char in morse_Raw:
                        first = text_D[fountion]
                        answer_vir = morse_Raw[first]
                        answer_D += answer_vir
                        fountion += 1
                    else:
                        answer_D = "ERROR 無法解密，請確認是否有錯誤的字元或空格。"
                cmd("cls")
                print(text, "為原文\n\n")     
                print(answer_D)
            break
        elif Uinput == "stop":
            print()
        else:
            print("請確認輸入的內容。")
            time.sleep(3)
            cmd("cls")
            continue
    
    while True:
        print()
        Uinput = input("是否重新開始加密或解密?(Y/N)")
        if Uinput == "Y":
            print("請稍後")
            time.sleep(3)
            break
        elif Uinput == "N":
            print("請稍後")
            time.sleep(3)
            break
        else:
            print("請檢查輸入的內容。")
            time.sleep(3)
            continue
    if Uinput == "Y":
        print()
        cmd("cls")
        continue
    elif Uinput == "N":
        print()
        cmd("cls")
        break
        
print(text, "為原文\n\n")
print("Base64:\n", answer_A)
print("baseOT:\n", answer_B)
print("凱薩加密:\n",answer_C)
print("摩斯密碼:\n",answer_D)

print("\n\n\n加解密小程序，Made By.OtterCat \n ver. 1.0.0 請勿隨意修改程序碼")
print("\n\n\n按下任意鍵離開或關閉程序")
msvcrt.getch()
