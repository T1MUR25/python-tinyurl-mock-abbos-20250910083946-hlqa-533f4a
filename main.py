import hashlib
s='abbosmini'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
