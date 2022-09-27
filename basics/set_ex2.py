A ={1,2,3,4,5}
B={4,5,6,7,8}

#use/operater
print(A|B)

#use union function
A.union(B)
{1,2,3,4,5,6,7,8}

#use union function on B
B.union(A)
{1,2,3,4,5,6,7,8}


A ={1,2,3,4,5}
B ={4,5,6,7,8}

#use & operator
print(A&B)

A. intersection(B)


A ={1,2,3,4,5}
B ={4,5,5,6,7,8}

#use-operator an A
print(A-B)

#use difference function on A
A.difference(B)

#use -operator
B-A
print(B-A)


#use^operator
print(A^B)

#use symmetric_difference function on A
A.symmetric_difference(B)
{1,2,3,6,7,8}
