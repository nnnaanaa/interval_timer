import pygame
import time

class ClassManager:
    def __init__(self):
        self._path_start =""
        self._path_end = ""
        self._path_30second = ""
        self._path_1minute = ""

    @property
    def path_start(self):
        return self._path_start
    
    @path_start.setter
    def path_start(self, value):
        """Setter: path_start の値を設定"""
        if not isinstance(value, str):
            raise ValueError("path_start must be a string")
        self._path_start = value

    @property
    def path_end(self):
        return self._path_end
    
    @path_end.setter
    def path_end(self, value):
        """Setter: path_end の値を設定"""
        if not isinstance(value, str):
            raise ValueError("path_end must be a string")
        self._path_end = value

    @property
    def path_30second(self):
        return self._path_30second
    
    @path_30second.setter
    def path_30second(self, value):
        """Setter: path_30second の値を設定"""
        if not isinstance(value, str):
            raise ValueError("path_30second must be a string")
        self._path_30second = value

    @property
    def path_1minute(self):
        return self._path_1minute
    
    @path_1minute.setter
    def path_1minute(self, value):
        """Setter: path_1minute の値を設定"""
        if not isinstance(value, str):
            raise ValueError("path_1minute must be a string")
        self._path_1minute = value              

def main():
    classmanager = ClassManager()
    classmanager.path_start = "./data/StartProcess.wav"
    classmanager.path_end = "./data/EndProcess.wav"
    classmanager.path_30second = "./data/30Second.wav"
    classmanager.path_1minute = "./data/1Minute.wav"
    loop_count = 4
    delay_seconds = 30

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
    """
    指定されたWAVファイルを再生する関数
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
