palavra = str(input('Digite uma palavra: '))
contra = ''
for i in range(len(palavra) -1, -1, -1):
    contra = contra + palavra[i]
print(contra)