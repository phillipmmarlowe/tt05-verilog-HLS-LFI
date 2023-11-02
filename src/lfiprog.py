from pymtl3 import *
from pymtl3.passes.backends.verilog import *
import lfi

lfi = lfi.Lfi()
lfi.set_metadata(VerilogTranslationPass.enable, True)
lfi.apply(VerilogTranslationPass())


























