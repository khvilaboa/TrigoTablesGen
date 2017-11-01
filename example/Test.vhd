----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    02:52:52 11/01/2017 
-- Design Name: 
-- Module Name:    Test - Behavioral 
-- Project Name: 
-- Target Devices: 
-- Tool versions: 
-- Description: 
--
-- Dependencies: 
--
-- Revision: 
-- Revision 0.01 - File Created
-- Additional Comments: 
--
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library IEEE_PROPOSED;
use IEEE_PROPOSED.FIXED_PKG.ALL;

use work.Trigo.ALL;

entity Test is
	port(clk: in STD_LOGIC;
	     res: out sfixed(11 downto -20));
end Test;

architecture Behavioral of Test is
	signal count : INTEGER := 0;
	signal readable: REAL;  -- for simulation
begin
	process (clk) is
	begin
		if rising_edge(clk) then
			res <= sin(count);
			readable <= to_real(sin(count));
			count <= count + 1;
		end if;
	end process;

end Behavioral;

