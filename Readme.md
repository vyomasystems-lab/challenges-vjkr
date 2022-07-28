# MUX Design Verification
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
![image](https://user-images.githubusercontent.com/16399079/181467080-eeef2b92-83e4-4c00-98b9-0b3b5827a140.png)
The bug found is
'''
AssertionError: MUX failed, expected vlaue = 0 for select line = 13
'''
The design update should be
'''
For the MUX, the logic should be ``5'b01100: out = inp12;`` instead of ``5'b01101: out = inp12;`` as in the design code.
'''
