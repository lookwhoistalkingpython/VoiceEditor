module top;
 import uvm_pkg::*;

 ////Interface Instantiations
 //Example: iicIf iicIf1();

 //Wire Declarations
 //Example: wire scl, sda;

 initial begin
  ////Put config's into database
  //Example: uvm_config_db//(virtual iicIf)::set(null,"*","iicIf1", iicIf1);
 end

 ////Test bench component instantiations
 //Example: pullup(scl);

 ////Device Under Test instantiation
 //Example: i2c_master_top dut(
 //Example:  .wb_clk_i(wbIf.clk),
 //Example:);


 ////Initial Block
 initial begin
  //Example: wbIf.rst   <= 1'b1;
 end

 initial run_test();

endmodule
