import cocotb
from cocotb.triggers import Timer
import random
# import pytest
# @cocotb.test()
# async def test_direct_test(dut):
    
#     # dat_i = random.randint(0, 255)
#     dat_i = 0b00011101
#     # B = 10

#     # input driving
#     dut.dat_i.value = dat_i
#     # dut.b.value = B
#     await Timer(2, units='ns')
#     # print("Modulo 3 operation answer is")
#     # print(dut.reminder.value)
    
#     dut._log.info(f'Data={dat_i} model={int(dat_i % 3)} DUT={int(dut.reminder.value)}')
#     # int around dut.reminder value in above line helps in getting binary to decimal
#     # assert dut.reminder.value == dat_i % 3, f"Adder result is incorrect: {dut.reminder.value} != {dat_i % 3}"
#     assert dut.reminder.value == dat_i % 3, "Randomised test failed with: {A} = {SUM}".format(
#         A=dut.dat_i.value, SUM=dut.reminder.value)

@cocotb.test()
async def test_modulo3_randomised_test(dut):
    
    for i in range(3):

        dat_i = random.randint(0, 3)
        # dat_i = 0b00011101
        # B = 10

        # input driving
        dut.dat_i.value = dat_i
        # dut.b.value = B
        await Timer(2, units='ns')
        # print("Modulo 3 operation answer is")
        # print(dut.reminder.value)
        errors=0
        dut._log.info(f'Data={dat_i} model={int(dat_i % 3)} DUT={int(dut.reminder.value)}')
        # int around dut.reminder value in above line helps in getting binary to decimal
        # assert dut.reminder.value == dat_i % 2, f"Adder result is incorrect: {dut.reminder.value} != {dat_i % 3}"
        # try:
        #     assert dut.reminder.value == dat_i% 3
        # except: 
        #     AssertionError: 
        #     errors=errors+1
        assert dut.reminder.value == dat_i % 3, "Randomised test failed with: input{inpu} = reminder{remi}".format(
            inpu=int(dut.dat_i.value), remi=int(dut.reminder.value))