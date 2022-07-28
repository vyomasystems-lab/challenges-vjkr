# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.triggers import Timer
@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    
    cocotb.log.info('#### CTB: Develop your test here! ######')
    # testing if clock works without triggering. It does!
    # await Timer(9, units='us')
    # print(dut.clk.value)
    
    # waitning 10 us so as to allow clocking
    # await Timer(10, units='us')
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await Timer(2, units='us')
    print('current state', dut.current_state.value)
    print('next state', dut.next_state.value)
    print("seq_seen=",dut.seq_seen.value)
    assert dut.seq_seen.value==0, f"Sequence seen is {dut.seq_seen.value} which should be 0 "
    # print("reset value=")
    # print(dut.reset.value)
    
    await FallingEdge(dut.clk)
    # await Timer(10, units='us')
    dut.inp_bit.value=0
    await Timer(2, units='us')
    print('current state', dut.current_state.value)
    print('next state', dut.next_state.value)
    print("seq_seen=",dut.seq_seen.value)
    assert dut.seq_seen.value==0, f"Sequence seen is {dut.seq_seen.value} which should be 0 "
    
    await FallingEdge(dut.clk)
    # await Timer(10, units='us')
    dut.inp_bit.value=1
    await Timer(2, units='us')
    print('current state', dut.current_state.value)
    print('next state', dut.next_state.value)
    print("seq_seen=",dut.seq_seen.value)
    assert dut.seq_seen.value==0, f"Sequence seen is {dut.seq_seen.value} which should be 0 "
      
    await FallingEdge(dut.clk)
    # await Timer(10, units='us')    
    dut.inp_bit.value=1
    await Timer(2, units='us')
    print('current state', dut.current_state.value)
    print('next state', dut.next_state.value)
    print("seq_seen=",dut.seq_seen.value)
    assert dut.seq_seen.value==1, f"Sequence seen is {dut.seq_seen.value} which should be 1"
    
