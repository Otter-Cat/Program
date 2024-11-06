import os
import random
import msvcrt
import time
from random import choice
from os import system as cmd

cmd("title 隨機分組小程序")
cmd("cls")
print("隨機分組小程式，Made By.PGpenguin72 \n ver. 1.0.1 請勿隨意修改程序碼 \n\n\n")
print("(3秒後即將開始分組！)")
time.sleep(3)
cmd("cls")

while True:
    input_players = ""
    while not input_players.strip():
        input_players = input("請輸入所有成員名單，並以「, 」隔開每個成員的名字(或輸入stop來結束分組)。\n(例如:小明, 小紅, 小黃) \n > > >")
    if input_players == "stop":
        break
    else:
        input_players = input_players.split(', ')

    input_team = ""
    while not input_team.strip():
        input_team = input("請輸入要分的組別名稱,並以「, 」隔開(最多26個組)。\n (企鵝隊, 螃蟹隊, 北極熊隊) \n > > > ")
    input_team = input_team.split(", ")

    team_Raw = input_team
    player_raw = input_players

    while True:

        input_team = team_Raw
        input_players = player_raw

        teams = {}

        function = 1 

        for t in input_team:
            key = f'team_{function}'
            teams[key] = t
            function += 1

        T_function = function -1 #隊伍總數

        players = {}
        function = 1

        for p in input_players:
            player = f'player_{function}'
            players[player] = p
            function += 1

        P_list = list(players.values())
        T_list = [[] for _ in range(T_function)]

        function -= 1
        P_function = function
        function = 1

        while len(P_list) > 0:
            for i in range(T_function):
                if P_list:
                    player = choice(P_list)
                    T_list[i].append(player)
                    P_list.remove(player)

        print()
        cmd("cls")
        for index, team_key in enumerate(teams.keys()):
            if index < len(T_list):
                print(f'{teams[team_key]} 成員: {", ".join(T_list[index])}')
                time.sleep(0.3)

        while True:
            ans = input("請問是否重新隨機分組?(Y/N) \n > > >")
            if ans == "Y":
                print("正在準備重新分組中")
                cmd("cls")
                break
            elif ans == "N":
                print()
                while True:
                    ans_2 = input("那是否要重新開始(R)或統整數據(C) \n (註: 重新開始會刪除所有數據，統整數據會只保留結果於終端機。) \n > > > ")
                    if ans_2 == "R":
                        print()
                        break
                    elif ans_2 == "C":
                        print()
                        break
                    else:
                        print("請確認字母大小寫或是否有輸入錯誤")
                        continue
                if ans_2 == "R":
                    print()
                    break
                elif ans_2 == "C":
                    print()
                    break
            elif ans == "":
                continue
            else:
                print("請確認字母大小寫或是否有輸入錯誤")
                continue                       

            if ans_2 == "R":
                print("正在清除檔案")        
                time.sleep(3)
                break  
            elif ans_2 == "C":
                print("正在記錄數據")
                time.sleep(2)
                break 
        
        if ans == "Y":
            continue
        elif ans_2 == "R":
            cmd("cls")
            break
        elif ans_2 == "C":
            print()
            break
    if ans_2 == "R":
        cmd("cls")
        continue
    elif ans_2 == "C":
        print()
        break                 

if input_players == "stop":
    cmd("cls")
    print("隨機分組小程式，Made By.PGpenguin72 \n ver. 1.0.1 請勿隨意修改程序碼")
    print("\n\n\n按下任意鍵離開或關閉程序")
    msvcrt.getch()
else:
    print()
    cmd("cls")
    for index, team_key in enumerate(teams.keys()):
        if index < len(T_list):
            print(f'{teams[team_key]} 成員: {", ".join(T_list[index])}')
            time.sleep(0.2)

    print("\n\n")
    print("隨機分組小程式，Made By.PGpenguin72 \n ver. 1.0.1 請勿隨意修改程序碼")
    print("\n\n\n按下任意鍵離開或關閉程序")
    msvcrt.getch()