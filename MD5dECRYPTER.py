import hashlib
n = input("Enter your hash")
hash_n=hashlib.md5(n.encode('UTF-8')).hexdigest()
with open("file.txt","r") as f:
    for lines in f:
       hash = hashlib.md5(lines.encode('UTF-8')).hexdigest()
       if hash_n == hash:
         print("[+]hash has been decoded :", lines)
         break
  
