import pickle
import pandas as pd
from image_struct import ImageStruct

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

filepath = 'data/cifar-10-batches-py/data_batch_1'
output_excel = 'data/cifar-10-batches-py/data_batch_1.xlsx'

# 加载数据
data_dict = unpickle(filepath)
data = data_dict[b'data']
labels = data_dict[b'labels']

# 将数据转换为DataFrame
df = pd.DataFrame(data)
df['Label'] = labels
label_list = df['Label'].tolist()

# 只保留前1000条数据
df = df.head(1000)
label_list = label_list[:1000]

# data normalization label not normalized
df = df.apply(lambda x: x / 255)
# reput the label to the dataframe
df['Label'] = label_list



# 初始化image_list
image_list = []

# 将数据分成RGB通道
df_r = df.iloc[:, :1024]
df_g = df.iloc[:, 1024:2048]
df_b = df.iloc[:, 2048:3072]

# put the data into image struct
for index, row in df.iterrows():
    # 创建一个新的ImageStruct对象
    image = ImageStruct(None, r=[], g=[], b=[])
    image.label = row['Label']
    for i in range(1024):
        # 将每个通道的像素值添加到对应的列表中
        image.r.append(df_r.iloc[index, i])
        image.g.append(df_g.iloc[index, i])
        image.b.append(df_b.iloc[index, i])
    # save the image to a list
    image_list.append(image)
    print(index,'image:', image.label, 'r:', image.r[0], 'g:', image.g[0], 'b:', image.b[0])

print('label:',image_list[0].label, 'r:', image_list[0].r[0], 'g:', image_list[0].g[0], 'b:', image_list[0].b[0])
