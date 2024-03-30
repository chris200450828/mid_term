import q10_command_stuff as qcf


qcf.day_manager(opt=True)
qcf.advance_link_mode(opt=False, pop=True)
data_list = qcf.get_data()
qcf.advance_file_manager(data_list, opt=False)
