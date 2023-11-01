from pymtl3 import *

class lfi(Component):
	def construct( s ):
def construct( s, nbits = 8 ):
	s.clk_i = InPort()
	s.rst_n = InPort()
    s.current_i = InPort(nbits)
    s.spike_o = OutPort()
    s.nu_o = OutPort(nbits)
	
	s.threshold_w = Wire(nbits)
	s.u_w = Wire(nbits)

	@update
	def updateblk():
	    s.nu_o @= s.current_i + (s.u_w >> 1)
		s.spike @= (s.u_w >= s.threshold)
	
	
	@update_ff
    # YOUR CODE HERE
    # Use <<= for sequential assignment
    def countblk():
    	if (!s.rst_n):
    		s.u_w <<= 0
    		# s.threshold_w <= 0
    	else:
    		s.u_w <<= s.nu_o






















