# -*- coding:utf-8 -*-

class ClassManagerLatr:
    def __init__(self):
        self._path_start =""
        self._path_end = ""
        self._last_10_seconds = ""
        self._chapter_1 = ""
        self._chapter_2 = ""
        self._chapter_3 = ""
        self._chapter_4 = ""
        self._chapter_5 = ""
        self._chapter_6 = ""
        self._chapter_7 = ""
        self._chapter_8 = ""
        self._chapter_9 = ""

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
    def last_10_seconds(self):
        return self._last_10_seconds
    
    @last_10_seconds.setter
    def last_10_seconds(self, value):
        """Setter: last_10_seconds の値を設定"""
        if not isinstance(value, str):
            raise ValueError("last_10_seconds must be a string")
        self._last_10_seconds = value

    @property
    def chapter_1(self):
        return self._chapter_1
    
    @chapter_1.setter
    def chapter_1(self, value):
        """Setter: chapter_1 の値を設定"""
        if not isinstance(value, str):
            raise ValueError("chapter_1 must be a string")
        self._chapter_1 = value

    @property
    def chapter_2(self):
        return self._chapter_2
    
    @chapter_2.setter
    def chapter_2(self, value):
        """Setter: chapter_2 の値を設定"""
        if not isinstance(value, str):
            raise ValueError("chapter_2 must be a string")
        self._chapter_2 = value

    @property
    def chapter_3(self):
        return self._chapter_3
    
    @chapter_3.setter
    def chapter_3(self, value):
        """Setter: chapter_3 の値を設定"""
        if not isinstance(value, str):
            raise ValueError("chapter_3 must be a string")
        self._chapter_3 = value

    @property
    def chapter_4(self):
        return self._chapter_4
    
    @chapter_4.setter
    def chapter_4(self, value):
        """Setter: chapter_4 の値を設定"""
        if not isinstance(value, str):
            raise ValueError("chapter_4 must be a string")
        self._chapter_4 = value

    @property
    def chapter_5(self):
        return self._chapter_5
    
    @chapter_5.setter
    def chapter_5(self, value):
        """Setter: chapter_5 の値を設定"""
        if not isinstance(value, str):
            raise ValueError("chapter_5 must be a string")
        self._chapter_5 = value

    @property
    def chapter_6(self):
        return self._chapter_6
    
    @chapter_6.setter
    def chapter_6(self, value):
        """Setter: chapter_6 の値を設定"""
        if not isinstance(value, str):
            raise ValueError("chapter_6 must be a string")
        self._chapter_6 = value

    @property
    def chapter_7(self):
        return self._chapter_7
    
    @chapter_7.setter
    def chapter_7(self, value):
        """Setter: chapter_7 の値を設定"""
        if not isinstance(value, str):
            raise ValueError("chapter_7 must be a string")
        self._chapter_7 = value

    @property
    def chapter_8(self):
        return self._chapter_8
    
    @chapter_8.setter
    def chapter_8(self, value):
        """Setter: chapter_8 の値を設定"""
        if not isinstance(value, str):
            raise ValueError("chapter_8 must be a string")
        self._chapter_8 = value

    @property
    def chapter_9(self):
        return self._chapter_9
    
    @chapter_9.setter
    def chapter_9(self, value):
        """Setter: chapter_9 の値を設定"""
        if not isinstance(value, str):
            raise ValueError("chapter_9 must be a string")
        self._chapter_9 = value

class ClassManagerHptr:
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