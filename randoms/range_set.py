# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way t

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))


# def set_range(x,y,z):
#     # Your code here
#     big = biggest(x,y,z)
#     # small find things small =?
#     if big == x:
#         small = bigger(y,z)
#         if small == y:
#             return x - y
#         else:
#             return x - z
#     if big == y:
#         small = bigger(x,z)
#         if small == z:
#             return y - z
#         else:
#             return y - x #redunda
#     if big == z:
#         small = bigger(x,y)
#         if small == x:
#             return z - x #redundant
#         else:
#             return z - y #redundant


def set_range(p, q, r):
    if p == biggest (p, q, r):
        if q == bigger (q, r):
            return p - r
        else: 
            return p - q
    else:
        if q == bigger (q, r):
            if p == bigger (p, r):
                return q - r
            else:
                return q - p
        else:
                if p == bigger (p, q):
                    return r - q
                else:
                    return r - p


print(set_range(10, 4, 7))
#>>> 6  # since 10 - 4 = 6

print(set_range(1.1, 7.4, 18.7))
#>>> 17.6 # since 18.7 - 1.1 = 17.6
