"""
What is a set?
Set is also a collection of similar or different types of elements.
How to create a set?
1.We can create a set using curly braces{}
2.We can also create set with keyword set 
3.It is also mutable object
4.Set does not allow duplicate elements.
5.Set also does not follow any order.
"""
s1 = set({10,20})
print("s1:\t",s1)
s2 = {10,20,30,30,40,40,50,70}
print("s2:\t",s2)
print("Address OF Set:\t",id(s2))
s2.remove(70)
print("Set2 after removing:\t",s2)
s2.pop()
print("set after popping:\t",s2)
l1 = [10,20,30]
l1.pop(0)
print(l1)
s2.discard(50)
print("set after discarding:\t",s2)
#both discard() and remove() methods are used to delete elements...........
s2.clear()
print("set after clearing:\t",s2)
s2 = {10,20,30,40}
s3 = s2.copy()
print("my set:\t",s2)
print("copy set:\t",s3)
s1 = {10,20,30,40,50}
s2 = {10,30,50,70,90}
s3 = s1.difference(s2)
s4 = s2.difference(s1)
print("s1:\t",s1)
print("s2:\t",s2)
print("s3:\t",s3)
print("s4:\t",s4)
s1.difference_update(s2)
print("s1:\t",s1)
print("s2:\t",s2)
s5={"vijji","naga","lakshmi","jyothi"}
s6={"sai","devika","vijji","naga"}
s7 = s5.intersection(s6)
print("s5:\t",s5)
print("s6:\t",s6)
print("s7:\t",s7)
s5={"vijji","naga","lakshmi","jyothi"}
s6={"sai","devika","vijji","naga"}
s6.intersection_update(s5)
print("s5:\t",s6)
s5={"vijji","naga","lakshmi","jyothi"}
s6={"sai","devika","vijji","naga"}
s8 = s5.union(s6)
print("UNION SET S8:\t",s8)
s5={"vijji","naga","lakshmi","jyothi"}
s6={"sai","devika","vijji","naga"}
s5.update(s6)
print("Set after updating s5:\t",s5)
s5={"vijji","naga","lakshmi","jyothi"}
s6={"sai","devika","vijji","naga"}
print("s5.isdisjoint(s6):\t",s5.isdisjoint(s6))
s5={"vijji","naga","lakshmi","jyothi"}
s6={"sai","devika"}
print("s5.isdisjoint(s6):\t",s5.isdisjoint(s6))
s7={"vijji","naga","lakshmi","jyothi"}
s8={"sai","devika"}
print("s7.issubset(s8):\t",s7.issubset(s8))
s9 = {1,2,3,4,5}
s10 = {1,2,3,4,5,6,7,8,9}
s11 = s10.issuperset(s9)
print("s11:\t",s11)
s1 = {1,2,3,4,5}
s2 = {1,3,7}
s3 =s2.symmetric_difference(s1)
s1.symmetric_difference_update(s2)
print("s3:\t",s3)
print("s1:\t",s1)