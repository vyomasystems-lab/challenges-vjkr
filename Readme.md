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

# BITMANIP Processor Design Verification
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
![image](https://user-images.githubusercontent.com/16399079/181800108-90fad127-f8e5-4d4b-8614-f6cb5d300edd.png)
The bugs found are for AND, OR and XOR operations
```
AssertionError: Value mismatch DUT = 0x1fffffffe does not match MODEL = 0x1
```
The design update should be
```
model_bitmanip.py didnot have IF cases for AND, OR and XOR operations
appending valid bit was not possible
```
## Verification Strategy
verification took time because, model.py file was assumed to be perfect. 
After finding the bugs in model.py, manual results and results from model.py match. But DUT results are not matching.
Also could not work through providing valdation bit on the results.
## Is the verification complete ?
NO

# Mod 3 Calculator Design Verification
![image](https://user-images.githubusercontent.com/16399079/181872182-fd49f6c6-383c-464c-b0a7-5e8f126e4b65.png)
The bug inserted and found is
```
AssertionError: Randomised test failed with: input82 = reminder0
AssertionError: Randomised test failed with: input201 = reminder1
AssertionError: Randomised test failed with: input113 = reminder0
AssertionError: Randomised test failed with: input97 = reminder2
AssertionError: Randomised test failed with: input1 = reminder2 <--------- This error is helpful in verification strategy
```
The design update should be
```
type_conv TC0(
     .plus_one(dat_i[1]), ---------> .plus_one(dat_i[0]),
     .minus_one(dat_i[0]), ----------> .minus_one(dat_i[1]),
```
## Verification Strategy
Fourth error is obtained for small number, hence manual tracing of operations on last 2 bits helps find the error!
The observed pattern is when input number has last bits 01 or 10, error is seen. No error if 00 or 11

## Is the verification complete ?
YES


:thumbsup:
