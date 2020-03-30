//Example: subcomponent.port.connect(port);
[component instance].[port name].connect([port name]);

//Example: export.connect(subcomponent.export);
[export instance].connect([subcomponent.export instance]);

if (!uvm_config_db#([element type])::get(this, "", "[element type]", [element instance]))
 `uvm_fatal("[parent name]","Could not get handle to [element type].")

//Example: comp1.port.connect(comp2.export);
[component instance].[port name].connect([component instance].[export/import name]);
