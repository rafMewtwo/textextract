import os

frend = open('./a/test.pdf')

final_path = './b'
inicial_path = './a'
os.listdir(inicial_path)

for line in frend:
    if('lulu' in line):
        frend.close()
        os.rename(f"a/test.pdf", f"b/test.pdf")
        print('transferido')
        break
    else:
        print('nao transferido')





