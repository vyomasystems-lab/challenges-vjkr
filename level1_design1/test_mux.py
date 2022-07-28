# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
   
    # input driving
    dut.sel.value = 0
    dut.inp0.value = 0
    # await Timer(2, units='ns') <======== SHOULD NEVER BE COMMENTED, RESULTS IN VALUE ERROR
    await Timer(2, units='ns')
    dut._log.info(f'DUT={dut.sel.value} line checked')
    assert dut.out.value == 0, "MUX failed, expected vlaue = {EXP} for select line = {SEL}".format(EXP=int(dut.out.value), SEL=int(dut.sel.value))
    
    dut.sel.value = 1
    dut.inp1.value = 1
    await Timer(2, units='ns')
    dut._log.info(f'DUT={dut.sel.value} line checked')
    assert dut.out.value == 1, "MUX failed, expected vlaue = {EXP} for select line = {SEL}".format(EXP=int(dut.out.value), SEL=int(dut.sel.value))

    dut.sel.value = 2
    dut.inp2.value = 2
    await Timer(2, units='ns')
    dut._log.info(f'DUT={dut.sel.value} line checked')
    assert dut.out.value == 2, "MUX failed, expected vlaue = {EXP} for select line = {SEL}".format(EXP=int(dut.out.value), SEL=int(dut.sel.value))

    dut.sel.value = 3
    dut.inp3.value = 3
    await Timer(2, units='ns')
    dut._log.info(f'DUT={dut.sel.value} line checked')
    assert dut.out.value == 3, "MUX failed, expected vlaue = {EXP} for select line = {SEL}".format(EXP=int(dut.out.value), SEL=int(dut.sel.value))

    dut.sel.value = 4
    dut.inp4.value = 0
    await Timer(2, units='ns')
    dut._log.info(f'DUT={dut.sel.value} line checked')
    assert dut.out.value == 0, "MUX failed, expected vlaue = {EXP} for select line = {SEL}".format(EXP=int(dut.out.value), SEL=int(dut.sel.value))

    dut.sel.value = 5
    dut.inp5.value = 1
    await Timer(2, units='ns')
    dut._log.info(f'DUT={dut.sel.value} line checked')
    assert dut.out.value == 1, "MUX failed, expected vlaue = {EXP} for select line = {SEL}".format(EXP=int(dut.out.value), SEL=int(dut.sel.value))

    dut.sel.value = 6
    dut.inp6.value = 2
    await Timer(2, units='ns')
    dut._log.info(f'DUT={dut.sel.value} line checked')
    assert dut.out.value == 2, "MUX failed, expected vlaue = {EXP} for select line = {SEL}".format(EXP=int(dut.out.value), SEL=int(dut.sel.value))

    dut.sel.value = 7
    dut.inp7.value = 3
    await Timer(2, units='ns')
    dut._log.info(f'DUT={dut.sel.value} line checked')
    assert dut.out.value == 3, "MUX failed, expected vlaue = {EXP} for select line = {SEL}".format(EXP=int(dut.out.value), SEL=int(dut.sel.value))

    dut.sel.value = 8
    dut.inp8.value = 0
    await Timer(2, units='ns')
    dut._log.info(f'DUT={dut.sel.value} line checked')
    assert dut.out.value == 0, "MUX failed, expected vlaue = {EXP} for select line = {SEL}".format(EXP=int(dut.out.value), SEL=int(dut.sel.value))

    dut.sel.value = 9
    dut.inp9.value = 1
    await Timer(2, units='ns')
    dut._log.info(f'DUT={dut.sel.value} line checked')
    assert dut.out.value == 1, "MUX failed, expected vlaue = {EXP} for select line = {SEL}".format(EXP=int(dut.out.value), SEL=int(dut.sel.value))

    dut.sel.value = 10
    dut.inp10.value = 2
    await Timer(2, units='ns')
    dut._log.info(f'DUT={dut.sel.value} line checked')
    assert dut.out.value == 2, "MUX failed, expected vlaue = {EXP} for select line = {SEL}".format(EXP=int(dut.out.value), SEL=int(dut.sel.value))

    dut.sel.value = 11
    dut.inp11.value = 3
    await Timer(2, units='ns')
    dut._log.info(f'DUT={dut.sel.value} line checked')
    assert dut.out.value == 3, "MUX failed, expected vlaue = {EXP} for select line = {SEL}".format(EXP=int(dut.out.value), SEL=int(dut.sel.value))

    dut.sel.value = 12
    dut.inp12.value = 0
    await Timer(2, units='ns')
    dut._log.info(f'DUT={dut.sel.value} line checked')
    assert dut.out.value == 0, "MUX failed, expected vlaue = {EXP} for select line = {SEL}".format(EXP=int(dut.out.value), SEL=int(dut.sel.value))

    dut.sel.value = 13
    dut.inp13.value = 1
    await Timer(2, units='ns')
    dut._log.info(f'DUT={dut.sel.value} line checked')
    assert dut.out.value == 1, "MUX failed, expected vlaue = {EXP} for select line = {SEL}".format(EXP=int(dut.out.value), SEL=int(dut.sel.value))

    # dut.sel.value = 0
    # dut.inp0.value = 1
    # await Timer(2, units='ns')
    # dut._log.info(f'DUT={dut.sel.value} line checked')
    # assert dut.out.value == 2, "MUX failed, expected vlaue = {EXP} for select line = {SEL}" 
    # .format(EXP=int(dut.out.value), SEL=int(dut.sel.value))

    # dut.sel.value = 0
    # dut.inp0.value = 1
    # await Timer(2, units='ns')
    # dut._log.info(f'DUT={dut.sel.value} line checked')
    # assert dut.out.value == 2, "MUX failed, expected vlaue = {EXP} for select line = {SEL}" 
    # .format(EXP=int(dut.out.value), SEL=int(dut.sel.value))

    # dut.sel.value = 0
    # dut.inp0.value = 1
    # await Timer(2, units='ns')
    # dut._log.info(f'DUT={dut.sel.value} line checked')
    # assert dut.out.value == 2, "MUX failed, expected vlaue = {EXP} for select line = {SEL}" 
    # .format(EXP=int(dut.out.value), SEL=int(dut.sel.value))

    # dut.sel.value = 0
    # dut.inp0.value = 1
    # await Timer(2, units='ns')
    # dut._log.info(f'DUT={dut.sel.value} line checked')
    # assert dut.out.value == 2, "MUX failed, expected vlaue = {EXP} for select line = {SEL}" 
    # .format(EXP=int(dut.out.value), SEL=int(dut.sel.value))

    # dut.sel.value = 0
    # dut.inp0.value = 1
    # await Timer(2, units='ns')
    # dut._log.info(f'DUT={dut.sel.value} line checked')
    # assert dut.out.value == 2, "MUX failed, expected vlaue = {EXP} for select line = {SEL}" 
    # .format(EXP=int(dut.out.value), SEL=int(dut.sel.value))







# @cocotb.test()
# async def mux_randomised_test(dut):
#     """Test for adding 2 random numbers multiple times"""

#     for i in range(31):

#         dut.sel.value = i
#         i=str(i)
#         inputnumbervalue= str("dut.inp"+i+".value")
#         print(inputnumbervalue)
#         # inputnumbervalue=int(inputnumbervalue)
#         # inputnumbervalue = i%3
#         # dut.inp0.value=1
#         # dut.inp1.value=1
#         # dut.inp2.value=1
#         inputnumbervalue=int(inputnumbervalue)
#         inputnumbervalue=1
#         await Timer(4, units='ns')
#         assert dut.out.value == 1, "I failed my Mux, expected vlaue = {EXP}" .format(EXP=int(dut.out.value))
#         # dut._log.info(f'{dut.sel.value}')
 
# @cocotb.test()
# async def mux_randomised_test(dut):
#     """Test for adding 2 random numbers multiple times"""

#     for i in range(31):

#         dut.sel.value = i
#         i=str(i)
#         inputnumbervalue= str("inp"+i)
#         inputnumbervalue=10
#         print(inputnumbervalue)
#         print(type(inputnumbervalue))
#         # inputnumbervalue=int("inputnumbervalue")
#         # print(type(inputnumbervalue))
#         # # inputnumbervalue=int(inputnumbervalue)
#         dut.inputnumbervalue.value=1
#         await Timer(4, units='ns')
#         assert dut.out.value == 1, "I failed my Mux, expected vlaue = {EXP}" .format(EXP=int(dut.out.value))
#         # dut._log.info(f'{dut.sel.value}')