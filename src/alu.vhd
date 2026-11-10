library IEE
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL

entity ALU is
    Port (
        A           :in STD_LOGIC_VECTOR(31 downto 0); -- 32bits wide 
        B           :in STD_LOGIC_VECTOR(31 downto 0); -- input is also 32 bits wide
        ALUControl  :in STD_LOGIC_VECTOR(1 downto 0); -- tells which instruction to execute
        Result      :out STD_LOGIC_VECTOR(31 downto 0); -- result of the operation which is also 32 bits wide
        Zero        :out STD_LOGIC
    )
end ALU;

architecture Behavioral of ALU is
    signal ALURESULT : STD_LOGIC_VECTOR(31 downto 0);
begin 

    process(A, B, ALUControl)
    begin
        case ALUControl is

            --addition
            when "00" =>
                ALURESULT <=STD_LOGIC_VECTOR(UNSIGNED(A)+UNSIGNED(B));
            --Substraction 

            when "01"=>
                ALURESULT <= STD_LOGIC_VECTOR(UNSIGNED(A)-UNSIGNED(B));
            ---BITWISE OR 

            when"10"=>
                ALURESULT <= STD_LOGIC_VECTOR( A OR B);
            ---BITWISE NAND 

            when"11" =>
                ALURESULT <= STD_LOGIC_VECTOR(A NAND B);

            when others =>
                ALURESULT <= ('others'<= '0');
            end case 
    end process

    Result <= ALURESULT;

    -- IS THE ALU RESULT ZERO ? 
    zero <= '1' when ALURESULT <= x"00000000" else '0';
