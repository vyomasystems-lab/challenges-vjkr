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

# SEQUENCE DETECTOR Design Verification
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
![image](https://user-images.githubusercontent.com/16399079/181604945-1f3293b7-65a3-4af3-83cc-a7f5ea35360c.png)
The bugs found are
```
AssertionError: Sequence seen is 0 which should be 1
```
The design update should be
```
For the sequence detector, the logic should 
assign seq_seen = next_state == SEQ_1011 ? 1: 0;
     instead of 
assign seq_seen = current_state == SEQ_1011 ? 1: 0;
```
## Verification Strategy
Tried with various await values and rising/falling clocks. logging next_state value helped in finding the bug.
## Is the verification complete ?
Yes
