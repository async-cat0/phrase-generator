import random
from constant.constants import RESET,YELLOW
from constant.constants import DCT,DCT2,DCT3



def generate():
    space = ' '
    print(f"{random.choice(DCT) + space + random.choice(DCT2) + space + random.choice(DCT3)}")
    print(f"{YELLOW} by async-cat0{RESET}")
generate()