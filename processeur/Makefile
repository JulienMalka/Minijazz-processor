
source = utils.mj multiplexers.mj add_sub.mj comparator.mj logic_unit.mj registers.mj controller.mj shift_unit.mj ALU.mj PC.mj extend.mj CPU.mj decoder.mj ROM.mj RAM.mj main.mj

processor.mj: $(source)
	cat $(source) > processor.mj
	./mjc.byte processor.mj


clean:
	rm processor.mj
