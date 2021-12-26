from PIL import Image
import os
import glob

path1 = os.getcwd()
comp1 = path1+'\\compression'
print(path1)
try:
    os.mkdir(comp1)
except:
    pass

print('將JPG壓縮請輸入:1')
print('將PNG壓縮請輸入:2')
print('混合壓縮請輸入 :3')
def compression(name):
    jpgphoto = path1+"/*."+str(name)    
    size = (1920,1080)   # 定義要調整成爲的尺寸（PIL會自動根據原始圖片的長寬比來縮放適應設置的尺寸）
    for infile in glob.glob(jpgphoto, recursive=True):     # glob.glob()用來進行模糊查詢，增加參數recursive=True後可以使用**/來匹配所有子目錄
        f,ext = os.path.splitext(infile)       # 分離文件名和後綴
        print(f)
        print(ext)
        k,c = os.path.split(f)        
        img = Image.open(infile)        # 打開圖片文件
        if (name=='png'):
            img = img.convert("RGB")
        img.thumbnail(size, Image.ANTIALIAS)        # 使用抗鋸齒模式生成縮略圖（壓縮圖片）
        img.save(comp1+"\\"+c+".jpg", "JPEG",quality=40) 
    
num = input()
try:
    if (num =='1'):
        compression('jpg')
    if (num =='2'):
        compression('png')
    if(num =='3'):
        compression('jpg')
        compression('png')
except Exception as e:
    print(e)
print('ok')
os.system("pause")

