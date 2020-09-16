import json
import os

f = open("fonts.json")
jsondata = json.load(f)
f.close()
#print(jsondata)


# f = open("imagelist.json")

arr = os.listdir("fonts")
for x in range(0, len(arr)):
	fontFamily = arr[x].split(".")[0]
	filename = arr[x]
	print(fontFamily)
	print(filename)
	newobj = {"fontFamily": fontFamily, "filename": filename}
	if newobj not in jsondata["items"]:
	   jsondata["items"].append(newobj)
	print(jsondata)
# for x in arr:
   # isdirectory = os.path.isdir(x)
   # if isdirectory:
      # if x not in jsondata:
       # jsondata[x] = []
      # files = os.listdir(x)
      # for file in files:
          # url = 'https://gesab001.github.io/assets/egw/images/' + x + "/" + file
          # if url in jsondata[x]:
             # print(x + ": exists")
          # else:
             # print("not exists")
             # url = 'https://gesab001.github.io/assets/egw/images/' + x + "/" + file
             # jsondata[x].append(url)


#newimage = input("url : " )
#folder = input("folder: " )
#if newimage not in jsondata[folder]:
#   jsondata[folder].append(newimage)

with open("fonts.json", "w") as outfile:
     json.dump(jsondata, outfile, indent=4)
