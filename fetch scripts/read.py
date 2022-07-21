f=open("C:\\Users\\IIISI\\Desktop\\internship\\fetch scripts\\COCOclasses.txt","r");
if "#CLASS" in f.readline():
	while True:
		klass=f.readline();

		if "#END" in klass:
			break;
		else:
			print("%s %d"%(klass.strip(),len(klass.strip())))
			#input();
f.close()
input();