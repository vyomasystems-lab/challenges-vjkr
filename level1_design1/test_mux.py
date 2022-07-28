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
    assert dut.out.value == 3, "I failed my Mux, expected vlaue = {EXP}" .format(EXP=int(dut.out.value))