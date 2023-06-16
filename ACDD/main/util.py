import os
from datetime import datetime
from django.conf import settings

class Util:
    def __init__(self):
        self.__path = os.getcwd()
        self.YEAR = datetime.now().year
        self.MONTH = '%02d' % datetime.now().month
        self.DAY = '%02d' % datetime.now().day
        self.YEAR, self.MONTH, self.DAY = list(map(str, [self.YEAR, self.MONTH, self.DAY]))

    def create_folder(self, ip) -> None:
        try:
            if not os.path.exists(os.path(settings.MEDIA_ROOT) + '\\' + str(ip)):
                os.makedirs(os.path(settings.MEDIA_ROOT) + '\\' + str(ip))
        except OSError:
            print('Error : Creating directory')

    def get_save_path(self, ip):
        return os.path(settings.MEDIA_ROOT) + '\\' + self.YEAR + '\\' + self.MONTH + '\\' + self.DAY + '\\' + str(ip)
    
    def get_path(self):
        return os.path(settings.MEDIA_ROOT)  + '\\' + self.YEAR + '\\' + self.MONTH + '\\' + self.DAY
    
    def get_pwd_path(self):
        return self.__path
    
    