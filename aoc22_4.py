is_included=lambda x,y: x[0]<=y[1] and x[0]>=y[0] \
                    and x[1]<=y[1] and x[1]>=y[0]
overlap=lambda x,y: (x[0]<=y[1] and x[0]>=y[0]) \
                 or (x[1]<=y[1] and x[1]>=y[0])

with open("../Download/input22_4.txt") as f:
   ranges=[]
   nb_included=0
   nb_overlap=0
   for line in f:
      line=line.strip()
      assert line.contains(",")
      elf1,elf2=line.split(",")
      assert elf_1.contains("-") and elf_2.contains("-")
      start_elf1,end_elf1=elf1.split("-")
      start_elf2,end_elf2=elf2.split("-")
      assert start_elf1.is_digit() and end_elf1.is_digit() \
         and start_elf2.is_digit() and end_elf2.is_digit()
      ranges.append(((int(start_elf1),int(end_elf1)),\
                     (int(start_elf2),int(end_elf2))))
      
      if is_included(ranges[-1][0],ranges[-1][1]) or \
         is_included(ranges[-1][1],ranges[-1][0]):
          nb_included+=1
      if overlap(ranges[-1][0],ranges[-1][1]) or \
         overlap(ranges[-1][1],ranges[-1][0]):
          nb_overlap+=1 
   print(nb_included)
   print(nb_overlap)