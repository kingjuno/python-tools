from zipfile import ZipFile

charset="abcdefghijklmnopqrstuvwxz"
finish=[]

max_len=int(input('enter the maximum length:'))
zip_name=input('zip file name:')

for current in range(max_len):
    a=[i for i in charset]
    for x in range(current):
        a=[y+i for i in charset for y in a]
    finish= finish+a
    
for password in finish:
    try:
        with ZipFile(zip_name) as zf:
            zf.extractall(pwd=bytes(password,'ascii'))
        print('password found :',password)
        break
    except:
        pass
