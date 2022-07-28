# MUX Design Verification
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
![image](https://user-images.githubusercontent.com/16399079/181467080-eeef2b92-83e4-4c00-98b9-0b3b5827a140.png)
The bugs found are
```
AssertionError: MUX failed, expected vlaue = 0 for select line = 13
AssertionError: MUX failed, expected vlaue = 1 for select line = 30
AssertionError: MUX failed, expected vlaue = 2 for select line = 31
```
The design update should be
```
For the MUX, the logic should be ``5'b01100: out = inp12;`` instead of ``5'b01101: out = inp12;`` as in the design code.
Insert case for 5'b11110 : out = inp30;
Insert case for 5'b11111 : out = inp31;
```
## Verification Strategy
Directed test cases for individual test scenarios i.e 32. Very tedious but works.
## Is the verification complete ?
Yes
