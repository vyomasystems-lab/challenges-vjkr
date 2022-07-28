# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
   
    # input driving
    dut.sel.value = 5
    dut.inp5.value = 3
    
    # await Timer(2, units='ns') <======== SHOULD NEVER BE COMMENTED, RESULTS IN VALUE ERROR
    await Timer(2, units='ns')
    assert dut.out.value == 7, "I failed my Mux, expected vlaue = {EXP}" .format(EXP=int(dut.out.value))
    
    # assert dut.sum.value == A+B, "Adder result is incorrect: {A} + {B} != {SUM}, expected value={EXP}".format(
    #         A=int(dut.a.value), B=int(dut.b.value), SUM=int(dut.sum.value), EXP=A+B)
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
   
    # input driving
    dut.sel.value = 5
    dut.inp5.value = 3
    
    # await Timer(2, units='ns') <======== SHOULD NEVER BE COMMENTED, RESULTS IN VALUE ERROR
    await Timer(2, units='ns')
    assert dut.out.value == 1, "Mux failed, expected vlaue = {EXP}" .format(EXP=int(dut.out.value))

    # # input driving
    # dut.sel.value = 10
    # dut.inp10.value = 2
    # await Timer(2, units='ns')
    # assert dut.out.value == 2, "Mux failed, expected vlaue = {EXP}" .format(EXP=int(dut.out.value))