from skeleton import *
skeleton1 = skeleton_1()
skeleton2 = skeleton_2()
skeleton3 = skeleton_3()

def distribute_key():
    if skeleton1.key_holder == 1:
        skeleton2.Is_key_holder(x=0)
        skeleton3.Is_key_holder(x=0)
    elif skeleton2.key_holder == 1:
        skeleton1.Is_key_holder(x=0)
        skeleton3.Is_key_holder(x=0)
    elif skeleton3.key_holder == 1:
        skeleton1.Is_key_holder(x=0)
        skeleton2.Is_key_holder(x=0)
    elif skeleton1.key_holder == 0 and skeleton2.key_holder == 0 and skeleton3.key_holder == 0:
        skeleton2.Is_key_holder(x=1)

