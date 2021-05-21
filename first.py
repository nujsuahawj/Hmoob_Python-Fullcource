x=99
if x>=80:
    print('grade A')
elif x>=70:
    print('grade B')
else:
    print('grade F')
for i in range(3):
    if i % 3 == 0:
         continue
    print(i)
def get_box_are( width, lenght,height):
    if width<0 or lenght<0 or height<0:
        return 0
    box_area=width * lenght * height
    return box_area
box1 = get_box_are(2,4,2)    
box2 = get_box_are(width=1,lenght=1,height=1)
print(box1)