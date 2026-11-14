library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity Register_File is 
    port(
        clk         : in STD_LOGIC;
        reset       : in STD_LOGIC;
        --THE READ PORTS 

        ReadReg1    : in STD_LOGIC(4 down to 0);
        ReadReg2    : in STD_LOGIC(4 down to 0);

        ReadData1   : in STD_LOGIC(31 down to 0);
        ReadData2   : in STD_LOGIC(31 down to 0);

        --the Write ports 

        WriteReg   : in STD_LOGIC(4 down to 0);
        WriteData   : in STD_LOGIC(31 down to 0);
        RegWrite   : in STD_LOGIC
    );
end Register_File;

architecture Behaviorial of Register_File is

    -- 32 registers and each of them is 32 bits wide

    type resgister_array is array(0 to 32)
        of STD_LOGIC_VECTOR( 31 down to 0);

    signal registers: resgister_array:=
        (others => (others => '0));
begin
    