// ============================================================
// S23_MIPS_ALU_soln_tb.v
// T. Manikas	2022 Dec 27
//
// testbench for S23_MIPS_ALU_soln
// ============================================================

`timescale 1ns / 1ps

module test_alu;

     parameter finishtime = 100;

	reg [3:0] ALUctl;
	reg [31:0] A, B;
	wire [31:0] ALUOut;
	wire Zero;
	MIPSALU u1(ALUctl, A, B, ALUOut, Zero);

	initial
	begin
	   ALUctl = 4'h0;	// start with AND function
					// A = 0, B = 0
	   A = 32'h0;
	   B = 32'h0;
	end

	initial
	begin
	   #2 A = 32'hC; B = 32'h4;	// C and 4 = 4
	   #2 A = 32'hF; B = 32'h6;	// F and 6 = 6

                  // OR function
	   #2 ALUctl = 4'h1;		      // F or 6 = F
	   #2 A = 32'hC; B = 32'h4;	// C or 4 = C

                  // ADD function
	   #2 ALUctl = 4'h2;            // C + 4 = 0010
	   #2 A = 32'h1;                // 1 + 4 = 5

                  // SUB function
	   #2 ALUctl = 4'h6;		// 1 - 4 = FFFF FFFD
	   #2 A = 32'hF;		// F - 4 = B

                  // set if A<B function
	   #2 ALUctl = 4'h7;		// F < 4? should be false
	   #2 A = 32'h2;		// 2 < 4? should be true

                  // NOR function
	   #2 ALUctl = 4'hC;		// NOR(2,4) = FFFF FFF9
	   #2 A = 32'hFFFF;		// NOR(FFFF,4) = FFFF 0000

                  // XOR function
	   #2 ALUctl = 4'hE;       // XOR(FFFF,4) = 0000 FFFB
	   #2 B = 32'h0000;        // XOR(FFFF,0000) = 0000 FFFF
 
         #finishtime $finish;

	end

	initial $monitor($time, " Zero=%b ALUctl=%d A=%h B=%h ALUOut=%h",
			Zero, ALUctl, A, B, ALUOut);

endmodule

	
