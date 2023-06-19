import os
from datetime import datetime
from pathlib import Path

class Util:
    def __init__(self):
        self.YEAR = datetime.now().year
        self.MONTH = '%02d' % datetime.now().month
        self.DAY = '%02d' % datetime.now().day
        self.YEAR, self.MONTH, self.DAY = list(map(str, [self.YEAR, self.MONTH, self.DAY]))

    def create_folder(self, ip) -> None:
        try:
            if not os.path.exists(self.get_path() + '\\' + str(ip)):
                os.makedirs(self.get_path() + '\\' + str(ip))
        except OSError:
            print('Error : Creating directory')

    def get_save_path(self, ip):
        media_root = os.path.abspath(os.path.join(self.get_project_root(), 'media'))
        return os.path.join(media_root, self.YEAR, self.MONTH, self.DAY, str(ip))
    

    def get_path(self):
        media_root = os.path.abspath(os.path.join(self.get_project_root(), 'media'))
        return os.path.join(media_root, self.YEAR, self.MONTH, self.DAY)
    
    def get_project_root(self):
        # 이 부분을 Django 프로젝트의 루트 경로로 수정해야 합니다.
        return Path(__file__).resolve().parent.parent
    
    