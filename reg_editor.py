from winreg import *
import mimetypes

mimetypes.init()

for ext in mimetypes.types_map:
    if mimetypes.types_map[ext].split('/')[0] == 'image':
        keyVal = 'Software\Classes\{}'.format(ext)
        try:
            key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
        except:
            key = CreateKey(HKEY_CURRENT_USER, keyVal)
        SetValueEx(key, "", 0, REG_SZ, "PhotoViewer.FileAssoc.Tiff")
        CloseKey(key)
            
            

                





    

