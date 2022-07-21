#Shivanshu Raj@caption exctractor
import json

#caption_path='C:/Users/IIISI/Desktop/internship/annotations'
caption_path=input("where are annotation files(just the path..)?:")
caption_file="/captions_train2017.json"
f=open(caption_path+caption_file);
data=json.loads(f.read());
caption_text=open(caption_path+"/caption2017coco.txt","w");
print("opened file...")
count =0;
print("extracting captions...")
for key,value in data.items():
	if(key=="annotations"):
		#print(key)
		#print(value)
		min=-1;


#value is list and v is a dictionary...
		
		lists=value
		d={}
		#list have to be sorted according to dictionary value kept inside it..
		lists=(sorted(lists, key = lambda item: item['image_id']))
		a=1;
		for info in lists:
			s1=info["image_id"]
			s2=info["caption"];
			s3=str(s1)+"   "+s2+"\n"
			#print(s3)
			caption_text.write(s3)
			print(str(int(a/len(lists)*100))+"%")
			a=a+1;
		

print("..done")		
caption_text.close();
print("file closed...bye bye")		
	



