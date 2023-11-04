from pymtl3 import *

class Lfi(Component):
  def construct( s, nbits = 8 ):
    #Inputs
    s.clk_i = InPort()
    s.rst_n = InPort()
    s.current_i = InPort(nbits)
    #Outputs
    s.spike_o = OutPort()
    s.nu_o = OutPort(nbits)
    #Wires
    s.threshold_w = Wire(nbits)
    s.u_w = Wire(nbits)

    @update_ff
    def countblk():
      if (~s.rst_n):
        s.u_w <<= 0
        s.threshold_w <<= 127
      else:
        s.u_w <<= s.nu_o

    @update
    def updateblk():
      #if (~(s.spike_o)):
        #s.nu_o @= s.current_i + (s.u_w >> 1)
      #else:
        #s.nu_o @= 0
      s.nu_o @= s.current_i + (s.u_w >> 1) if ~(s.spike_o) else 0
      s.spike_o @= (s.u_w >= s.threshold_w)

