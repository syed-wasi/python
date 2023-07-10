word = 'banana'
count = 0
for i in word:
    if i=='a':
        count=count+1
print('no of a',count)



text1="Juli.hayes@capgemini.com ct.ase.us Sat Jan 15 09:14:16 2023"
atpos=text1.find('@')
print(atpos)
dotpos=text1.find('.',atpos)
print(dotpos)
host = text1[atpos+1:dotpos]
print(host)


x='From Stephen.marquard@uct.ac.za'
pos= x.find('.')
print(x[pos:pos+3])
print(x[14:17])



numbers=[1,2,3]
for i in range(len(numbers)):
    print("i=",i, "\n" "numbers=",numbers[i], )
    numbers[i] = numbers[i] * 2
    print("numbers multiplied by 2=",numbers[i])


Counts=dict()
fname=input('enter file name')
fh=open(fname)
	Words=line.split()
	For word in words:
		Counts[word]=Counts.get(word,0)+1
Print(Counts)
