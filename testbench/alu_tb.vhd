library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity ALU_TB is
end ALU_TB;

architecture Behavioral of ALU_TB is

    -- Inputs to the ALU
    signal A : STD_LOGIC_VECTOR(31 downto 0);
    signal B : STD_LOGIC_VECTOR(31 downto 0);

    signal ALUControl : STD_LOGIC_VECTOR(1 downto 0);

    -- Outputs from the ALU
    signal Result : STD_LOGIC_VECTOR(31 downto 0);
    signal Zero : STD_LOGIC;

begin

    -- Connect the ALU to the testbench
    DUT: entity work.ALU
        port map (
            A => A,
            B => B,
            ALUControl => ALUControl,
            Result => Result,
            Zero => Zero
        );

    -- Apply test cases
    process
    begin

        -- TEST 1: ADD (5 + 3 = 8)
        A <= x"00000005";
        B <= x"00000003";
        ALUControl <= "00";

        wait for 10 ns;

        assert Result = x"00000008"
            report "ADD TEST FAILED"
            severity error;

        assert Zero = '0'
            report "ADD ZERO FLAG FAILED"
            severity error;

        report "ADD TEST PASSED";

        -- TEST 2: SUB (5 - 3 = 2)
        A <= x"00000005";
        B <= x"00000003";
        ALUControl <= "01";

        wait for 10 ns;

        assert Result = x"00000002"
            report "SUB TEST FAILED"
            severity error;

        report "SUB TEST PASSED";

        -- TEST 3: OR (5 OR 3 = 7)
        A <= x"00000005";
        B <= x"00000003";
        ALUControl <= "10";

        wait for 10 ns;

        assert Result = x"00000007"
            report "OR TEST FAILED"
            severity error;

        report "OR TEST PASSED";

        -- TEST 4: NAND
        A <= x"00000005";
        B <= x"00000003";
        ALUControl <= "11";

        wait for 10 ns;

        assert Result = x"FFFFFFFE"
            report "NAND TEST FAILED"
            severity error;

        report "NAND TEST PASSED";

        -- TEST 5: ZERO FLAG
        A <= x"00000005";
        B <= x"00000005";
        ALUControl <= "01";

        wait for 10 ns;

        assert Result = x"00000000"
            report "ZERO RESULT TEST FAILED"
            severity error;

        assert Zero = '1'
            report "ZERO FLAG TEST FAILED"
            severity error;

        report "ZERO FLAG TEST PASSED";

        report "ALL ALU TESTS COMPLETED SUCCESSFULLY!";

        wait;

    end process;

end Behavioral;