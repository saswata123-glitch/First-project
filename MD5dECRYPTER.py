import hashlib
n = input("Enter your hash")
with open ("file.txt" , "r") as f:
    for lines in f:
       hash = hashlib.md5(lines.encode('UTF-8')).hexdigest()
       if hash == n:
         print("[+]hash has been decoded :", lines)
         break
  
