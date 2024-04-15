// ============================================================
// S23_MIPS_ALU_soln.v
// T. Manikas	2022 Dec 27
//
//
// modified ALU (Arithmetic-Logic Unit) for MIPS processor
// ============================================================

`timescale 1ns / 1ps

module MIPSALU (ALUctl, A, B, ALUOut, Zero);
	input [3:0] ALUctl;		// ALU control signals
	input [31:0] A, B;		// ALU input values (operands)
	output [31:0] ALUOut;		// result of ALU operation
	reg [31:0] ALUOut;	
	output Zero;			// ZERO flag

		// ZERO flag set if ALU result is 0

	assign Zero = (ALUOut==0);

		// do if any change in ALUctl, A, B

	always @(ALUctl or A or B)
	begin
	   case (ALUctl)
	     0:  ALUOut <= A & B;		     // bitwise AND
	     1:  ALUOut <= A | B;		     // bitwise OR
	     2:  ALUOut <= A + B;		     // ADD
	     6:  ALUOut <= A - B;		     // SUB
	     7:  ALUOut <= A < B ? 1 : 0;	// set if A < B
	     12: ALUOut <= ~(A | B);		// NOR
	     14: ALUOut <= A ^ B;            // bitwise XOR
	     default:  ALUOut <= 0;
	   endcase
	end
endmodule

