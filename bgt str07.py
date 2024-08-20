
a="""
Tôi chăm học
Tôi chịu khó
Tôi đẹp zai
"""
dem=0
for i in range(len(a)):
    if a[i]=="T" and a[i+1]=="ô" and a[i+2]=="i":
        dem=dem+1
print(dem)