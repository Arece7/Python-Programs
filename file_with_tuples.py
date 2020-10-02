# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for
# each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting
# the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=[]
lst2=[]
count=dict()
for line in handle:
    if line.startswith("From "):
        line=line.split()
        hour=line[5]
        lst.append(hour)
       
for hours in lst:
    hours=hours.split(':')
    partHour=hours[0]
    lst2.append(partHour)
    lst2.sort()
for hh in lst2:
    count[hh]=count.get(hh,0)+1
for hourExact,counter in count.items():
    print(hourExact,counter)
    
