import numpy as np
import scipy.io as scio
from random import shuffle

def normalize(data):
    '''(0,1)normalization
    :param data : the object which is a 1*2048 vector to be normalized
    '''
    s= (data-min(data)) / (max(data)-min(data))

    return  s


def cut_samples(org_signals):
    ''' get original signals to 10*120*2048 samples, meanwhile normalize these samples
    :param org_signals :a 10* 121048 matrix of ten original signals
    '''

    results=np.zeros(shape=(10,120,2048))
    temporary_s=np.zeros(shape=(120,2048))

    for i in range(10):
        s=org_signals[i]
        for x in range(120):
            temporary_s[x]=s[1000*x:2048+1000*x]
            temporary_s[x]=normalize(temporary_s[x])     #顺道对每个样本归一化
        results[i]=temporary_s

    return results


def make_datasets(org_samples):
    '''输入10*120*2048的原始样本，输出带标签的训练集(占80%)和测试集(占20%)'''

    train_x=np.zeros(shape=(10,96,2048))
    train_y=np.zeros(shape=(10,96,10))
    test_x=np.zeros(shape=(10,24,2048))
    test_y=np.zeros(shape=(10,24,10))
    for i in range(10):
        s=org_samples[i]
        # 打乱顺序
        index_s = [a for a in range(len(s))]
        shuffle(index_s)
        s=s[index_s]
        # 对每种类型都划分训练集和测试集
        train_x[i]=s[:96]
        test_x[i]=s[96:120]
        # 填写标签
        label = np.zeros(shape=(10,))
        label[i] = 1
        train_y[i, :] = label
        test_y[i, :] = label

    #将十种类型的训练集和测试集分别合并并打乱
    x1 = train_x[0]
    y1 = train_y[0]
    x2 = test_x[0]
    y2 = test_y[0]
    for i in range(9):
        x1 = np.row_stack((x1, train_x[i + 1]))
        x2 = np.row_stack((x2, test_x[i + 1]))
        y1 = np.row_stack((y1, train_y[i + 1]))
        y2 = np.row_stack((y2, test_y[i + 1]))

    index_x1= [i for i in range(len(x1))]
    index_x2= [i for i in range(len(x2))]
    shuffle(index_x1)
    shuffle(index_x2)
    x1=x1[index_x1]
    y1=y1[index_x1]
    x2=x2[index_x2]
    y2=y2[index_x2]

    return x1, y1, x2, y2    #分别代表：训练集样本，训练集标签，测试集样本，测试集标签

def get_timesteps(samples):
    ''' get timesteps of train_x and test_X to 10*120*31*128
    :param samples : a matrix need cut to 31*128
    '''

    s1 = np.zeros(shape=(31, 128))
    s2 = np.zeros(shape=(len(samples), 31, 128))
    for i in range(len(samples)):
        sample = samples[i]
        for a in range(31):
            s1[a]= sample[64*a:128+64*a]
        s2[i]=s1

    return s2


# 读取原始数据，处理后保存
dataFile= r'D:\py\zhihu\c10signals.mat'
data=scio.loadmat(dataFile)
org_signals=data['signals']
org_samples=cut_samples(org_signals)
train_x, train_y, test_x, test_y=make_datasets(org_samples)
train_x= get_timesteps(train_x)
test_x= get_timesteps(test_x)

saveFile = r'D:\py\zhihu\dataset.mat'
scio.savemat(saveFile, {'train_x':train_x, 'train_y':train_y, 'test_x':test_x, 'test_y':test_y})
