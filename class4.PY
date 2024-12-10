Tree1= 96
Tree2= 64
Tree3= 92
Tree4= 98
Tree5= 100
sum=(Tree1+Tree2+Tree3+Tree4+Tree5)
print("the sum of trees height is ", sum)
average= sum/5
print("the average of the tree height is ",average)
#task2
amount= int(input("enter a amount of money"))
note1=(amount//100)
note2=(amount%100)//50
note3= (amount%100%50)//10
print("number of notes in hundreds=", note1)
print("number of notes in fity",note2)
print("number of notes in ten",note3)