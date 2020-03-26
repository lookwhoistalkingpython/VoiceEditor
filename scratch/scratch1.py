class iic_agent extends uvm_agent;
 `uvm_component_utils(iic_agent)

 string m_name;

 [config name] m_config;
 virtual [interface name] m_vif;

 [sequencer name] m_sequencer;
 [driver name] m_driver;

 uvm_analysis_port #([type]) m_ap;

 extern function new(string name = "iic_agent", uvm_component parent = null);
 extern function void build_phase(uvm_phase phase);
 extern function void connect_phase(uvm_phase phase);

endclass

function iic_agent::new(string name = "iic_agent", uvm_component parent = null);
 super.new(name,parent);
 m_name = name;
endfunction

function void iic_agent::build_phase(uvm_phase phase);
 super.build_phase(phase);

 // Agent configuration
 if (!uvm_config_db#([config name])::get(this, "", "config", m_config))
  `uvm_fatal([m_name], "Unable to get handle to [config name].")
 m_vif=m_config.m_vif;

 //Create sub components.
 m_driver = [driver name]::type_id::create("m_driver",this);
 m_driver.m_vif = m_vif;
 m_sequencer = iic_type_id::create("m_sequencer", this);

endfunction

function void iic_agent::connect_phase(uvm_phase phase);
 super.connect_phase(phase);
 m_driver.seq_item_port.connect(m_sequencer.seq_item_export);
 m_ap = m_sequencer.m_ap;
endfunction





