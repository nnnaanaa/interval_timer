# -*- coding:utf-8 -*-

import pygame
import time
import os
import tkinter as tk
import threading
from cmngr import ClassManagerLatr, ClassManagerHptr

def main():
    root = tk.Tk()
    root.title("interval timer")
    root.geometry("100x100")  # ウィンドウサイズを200x300に設定

    label = tk.Label(root, text="training menu", font=("Arial", 10))
    label.pack(pady=0)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=0)

    btn_latr = tk.Button(
        button_frame, text="latr", font=("Arial", 10),
        command=lambda: start_thread(latr)
    )
    btn_latr.pack(side=tk.LEFT)

    btn_hptr = tk.Button(
        button_frame, text="hptr", font=("Arial", 10),
        command=lambda: start_thread(hptr)
    )
    btn_hptr.pack(side=tk.LEFT)

    # 終了ボタン
    btn_exit = tk.Button(root, text="finish", font=("Arial", 10), command=root.destroy)
    btn_exit.pack(pady=0)

    root.mainloop()

# スレッドで関数を実行
def start_thread(target):
    """スレッド処理開始
    """
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()

def latr():
    """下腹トレーニング
    """
    delay_seconds = 20 / 2 # 間隔 
    data_dir = "./data/latr"
    classmanager = ClassManagerLatr()
    classmanager.path_start = os.path.join(data_dir ,"StartProcess.wav")
    classmanager.path_end = os.path.join(data_dir ,"EndProcess.wav")
    classmanager.last_10_seconds = os.path.join(data_dir ,"Last10Seconds.wav")
    classmanager.chapter_1 = os.path.join(data_dir ,"Chapter1.wav")
    classmanager.chapter_2 = os.path.join(data_dir ,"Chapter2.wav")
    classmanager.chapter_3 = os.path.join(data_dir ,"Chapter3.wav")
    classmanager.chapter_4 = os.path.join(data_dir ,"Chapter4.wav")
    classmanager.chapter_5 = os.path.join(data_dir ,"Chapter5.wav")
    classmanager.chapter_6 = os.path.join(data_dir ,"Chapter6.wav")
    classmanager.chapter_7 = os.path.join(data_dir ,"Chapter7.wav")
    classmanager.chapter_8 = os.path.join(data_dir ,"Chapter8.wav")
    classmanager.chapter_9 = os.path.join(data_dir ,"Chapter9.wav")

    # 開始ボイス
    play_sound(classmanager.path_start)

    # Chapter1
    play_sound(classmanager.chapter_1)
    time.sleep(delay_seconds)
    play_sound(classmanager.last_10_seconds)
    time.sleep(delay_seconds)

    # Chapter2
    play_sound(classmanager.chapter_2)
    time.sleep(delay_seconds)
    play_sound(classmanager.last_10_seconds)
    time.sleep(delay_seconds)

    # Chapter3
    play_sound(classmanager.chapter_3)
    time.sleep(delay_seconds)
    play_sound(classmanager.last_10_seconds)
    time.sleep(delay_seconds)

    # Chapter4
    play_sound(classmanager.chapter_4)
    time.sleep(delay_seconds)
    play_sound(classmanager.last_10_seconds)
    time.sleep(delay_seconds)

    # Chapter5
    play_sound(classmanager.chapter_5)
    time.sleep(delay_seconds)
    play_sound(classmanager.last_10_seconds)
    time.sleep(delay_seconds)

    # Chapter6
    play_sound(classmanager.chapter_6)
    time.sleep(delay_seconds)
    play_sound(classmanager.last_10_seconds)
    time.sleep(delay_seconds)

    # Chapter7
    play_sound(classmanager.chapter_7)    
    time.sleep(delay_seconds)
    play_sound(classmanager.last_10_seconds)
    time.sleep(delay_seconds)

    # Chapter8
    play_sound(classmanager.chapter_8)    
    time.sleep(delay_seconds)
    play_sound(classmanager.last_10_seconds)
    time.sleep(delay_seconds)

    # Chapter9
    play_sound(classmanager.chapter_9)    
    time.sleep(delay_seconds)
    play_sound(classmanager.last_10_seconds)
    time.sleep(delay_seconds)

    # 終了ボイス
    play_sound(classmanager.path_end)

def hptr():
    """左右トレーニング
    """
    loop_count = 4 # 試行回数
    delay_seconds = 30 # 間隔 
    data_dir = "./data/hptr"
    classmanager = ClassManagerHptr()
    classmanager.path_start = os.path.join(data_dir, "StartProcess.wav")
    classmanager.path_end = os.path.join(data_dir, "EndProcess.wav")
    classmanager.path_30second = os.path.join(data_dir, "30Second.wav")
    classmanager.path_1minute = os.path.join(data_dir, "1Minute.wav")

    for i in range(loop_count):

        # 開始ボイス
        if i == 0: play_sound(classmanager.path_start)

        # 30秒の休止
        time.sleep(delay_seconds)
        play_sound(classmanager.path_30second)

        # 30秒の休止
        time.sleep(delay_seconds)
        play_sound(classmanager.path_1minute)

    # 終了ボイス
    play_sound(classmanager.path_end)

def play_sound(file_path):
    """指定されたWAVファイルを再生する
    """
    try:
        # Pygameの初期化
        pygame.mixer.init()
        
        # サウンドをロード
        pygame.mixer.music.load(file_path)
        
        # 再生
        pygame.mixer.music.play()
        print(f"Playing: {file_path}")
        
        # 再生が終了するまで待機
        while pygame.mixer.music.get_busy():
            continue
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # 終了処理
        pygame.mixer.quit()

if __name__ == "__main__":
    main()
