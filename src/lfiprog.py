from pymtl3 import *
from pymtl3.passes.backends.verilog import *
import lfi
import os

lfi = lfi.Lfi()
lfi.set_metadata(VerilogTranslationPass.enable, True)
lfi.apply(VerilogTranslationPass())

os.system("mv Lfi__nbits_8__pickled.v lfi.v")
























