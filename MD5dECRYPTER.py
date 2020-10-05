import hashlib
n = input("Enter your hash")
with open ("file text" , "r") as f:
    for lines in f:
       hash = hashlib.md5(lines).hexdigest()
       if hash == n:
         print("[+]hash has been decoded :", lines)
         break
   f.close()
