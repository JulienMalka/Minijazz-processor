source = utils.mj multiplexers.mj add_sub.mj comparator.mj logic_unit.mj main.mj

processor.mj: $(source)
	cat $(source) > processor.mj
	./mjc.byte processor.mj