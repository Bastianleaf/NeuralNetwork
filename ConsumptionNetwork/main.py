import Network
import dataset

data = dataset.DataHandler("../dataset/data_normalizada.data")
data.read_line()
print(data.line)
print(data.line_output())