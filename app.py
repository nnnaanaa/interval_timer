# -*- coding:utf-8 -*-

import pygame
import time
import os
import asyncio
from cmngr import ClassManagerLatr, ClassManagerHptr

async def latr():
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
    await play_sound(classmanager.path_start)

    # Chapter1
    await play_sound(classmanager.chapter_1)
    time.sleep(delay_seconds)
    await play_sound(classmanager.last_10_seconds)
    time.sleep(delay_seconds)

    # Chapter2
    await play_sound(classmanager.chapter_2)
    time.sleep(delay_seconds)
    await play_sound(classmanager.last_10_seconds)
    time.sleep(delay_seconds)

    # Chapter3
    await play_sound(classmanager.chapter_3)
    time.sleep(delay_seconds)
    await play_sound(classmanager.last_10_seconds)
    time.sleep(delay_seconds)

    # Chapter4
    await play_sound(classmanager.chapter_4)
    time.sleep(delay_seconds)
    await play_sound(classmanager.last_10_seconds)
    time.sleep(delay_seconds)

    # Chapter5
    await play_sound(classmanager.chapter_5)
    time.sleep(delay_seconds)
    await play_sound(classmanager.last_10_seconds)
    time.sleep(delay_seconds)

    # Chapter6
    await play_sound(classmanager.chapter_6)
    time.sleep(delay_seconds)
    await play_sound(classmanager.last_10_seconds)
    time.sleep(delay_seconds)

    # Chapter7
    await play_sound(classmanager.chapter_7)    
    time.sleep(delay_seconds)
    await play_sound(classmanager.last_10_seconds)
    time.sleep(delay_seconds)

    # Chapter8
    await play_sound(classmanager.chapter_8)    
    time.sleep(delay_seconds)
    await play_sound(classmanager.last_10_seconds)
    time.sleep(delay_seconds)

    # Chapter9
    await play_sound(classmanager.chapter_9)    
    time.sleep(delay_seconds)
    await play_sound(classmanager.last_10_seconds)
    time.sleep(delay_seconds)

    # 終了ボイス
    await play_sound(classmanager.path_end)

async def hptr():
    """左右トレーニング
    """
    loop_count = 4 # 試行回数
    delay_seconds = 30 # 間隔 
    data_dir = "./data/hptr"
    classmanager = ClassManagerHptr()
    classmanager.path_start = "./data/hptr/StartProcess.wav"
    classmanager.path_end = "./data/hptr/EndProcess.wav"
    classmanager.path_30second = "./data/hptr/30Second.wav"
    classmanager.path_1minute = "./data/hptr/1Minute.wav"

    for i in range(loop_count):

        # 開始ボイス
        if i == 0: await play_sound(classmanager.path_start)

        # 30秒の休止
        time.sleep(delay_seconds)
        await play_sound(classmanager.path_30second)

        # 30秒の休止
        time.sleep(delay_seconds)
        await play_sound(classmanager.path_1minute)

    # 終了ボイス
    await play_sound(classmanager.path_end)

async def play_sound(file_path):
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
    asyncio.run(latr())
    # asyncio.run(hptr())
