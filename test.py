import random

# single line commnent
'''multi line comment'''
"""multi line comment"""
# x = print

# # x(x)

# # help(print)

# if (True):
#     pass

# while (True):
#     break

# for i in range(5):
#     pass

# for i in [1,2,3]:
#     pass

# print("hfdjgfd")



# print(x)

    def myMain():
    D = random.randint(10,20)
    d = random.randint(0,5)
    print(D,"\t",d)
    if not d == 0 and D % d == 0:
        print(f"to {d} diairei akrivws to {D}")
        print("to {diairetis} diairei akrivws to {Diairetaios}".format(diairetis=d,Diairetaios=D))
        print("to", d,"diairei akrivws to", D)


    


if __name__=="__main__":
    myMain()