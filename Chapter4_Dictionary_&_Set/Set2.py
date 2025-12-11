"""Figure out a way to store 9 & 9.0 as separate values in the set. 
(You can take help of built-in data types) """

st = {9, "9.0"}
# or
st1 = {"9", 0.9}
# or
st2 = {("int", 9), ("float", 9.0)}  # insert tuples inside set , because tuples are also immutable