import backpack
import file_load

tmpa=file_load.data_load("plecak.txt")
tmpd=file_load.get_data(tmpa,separator=",")

backpack= backpack.Backpack.create_Backpack(tmpd)
backpack.start()
