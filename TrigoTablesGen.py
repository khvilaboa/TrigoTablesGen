import argparse, math, sys

parser = argparse.ArgumentParser(description="Utility to generate parametrized trigonometric tables in a VHDL package ")
parser.add_argument("-o", "--output", type=str, default="trigo.vhd", help="Output file name")
parser.add_argument("-s", "--step", type=int, default=1, help="Step")
parser.add_argument("-p", "--precision", type=int, default=8, help="Number of decimals for the returned values")

args = parser.parse_args()

HEADER = """library IEEE;
use IEEE.STD_LOGIC_1164.all;

library IEEE_PROPOSED;
use IEEE_PROPOSED.FIXED_PKG.ALL;"""

BODY = """package Trigo is
{functions}
end package;"""

FUN_TEMPLATE = """	function {name} (val: INTEGER) return sfixed is
		variable ret : sfixed(11 downto -20);
	begin
		case val is
{cases}
		end case;
		return ret; 
	end {name};"""
	
WHEN_STMT = """			when {case} =>
				ret := to_sfixed({value}, ret);
"""
	
# Decorator
def table_function(func):
	def wrapper(prec = 8, step = 1):
		when_stmts = ""
		name, op = func()
		for i in range(0, 180, step):
			when_stmts += WHEN_STMT.format(case=i, value=round(op(i * math.pi / 180), prec))
		when_stmts += WHEN_STMT.format(case="others", value=0.0)
		return FUN_TEMPLATE.format(name = name, cases = when_stmts[:-1])
	return wrapper
	
@table_function
def gen_sin():
	return "sin", math.sin
	
@table_function
def gen_cos():
	return "cos", math.cos
	
with open(args.output, "w") as f:
	sin_fun = gen_sin(prec = args.precision, step = args.step)
	cos_fun = gen_cos(prec = args.precision, step = args.step)
	funcs = (sin_fun, cos_fun)
	f.write("\n\n".join([HEADER, BODY.format(functions="\n\n".join(funcs))]))
