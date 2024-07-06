import numpy as np
# 算法核心
def selectKeys(dataList, k):
    # 计算矩阵行
    row = len(dataList)
    # 计算矩阵列
    col = most_elements(dataList)
    keyList = []
    valueList = []
    for item in dataList:
        try:
            # 获取每个字典的键
            keys = list(item.keys())
            # 获取每个字典的值
            values = list(item.values())
            for index in range(col):
                keyList.append(keys[index])
                valueList.append(values[index])
        except Exception as e:
            # 这里try-except的作用是对键列表有多少缺的补None，对值列表有缺补可以确定的最小值
            iter = col - len(keys)
            for i in range(iter):
                keyList.append(None)
                valueList.append(-999)

    # 创建numpy数组
    npKeys = np.array(keyList)
    npValues = np.array(valueList)

    # 转row x col大小矩阵
    matKeys = np.reshape(npKeys, (row, col))
    matValues = np.reshape(npValues, (row, col))

    # 矩阵转置
    matkeyT = np.transpose(matKeys)
    matValueT = np.transpose(matValues)

    # 行排序，并且将键数组根据索引重新排列
    matValueSorted, index = rowSort(matValueT)
    matKeys = matRearrange(matkeyT, index)

    # 键矩阵转回数组， 并获取前k个值
    keyArr = np.reshape(matKeys, (1, row * col))
    result = keyArr[keyArr != None]
    result = result[:k]
    return result

# 计算元素最多的字典的元素数量
def most_elements(dicts):
    return len(max(dicts, key=len))
# 矩阵行降序排序，并打出索引
def rowSort(arr):
    indices = []
    for i in range(arr.shape[0]):
        arr[i] = np.sort(arr[i])[::-1]
        indices.append(np.argsort(arr[i]))
    return arr,indices

def matRearrange(matKeys, indices):
    for i in range(len(matKeys)):
        matKeys[i] = np.take(matKeys[i], indices[i])
    return matKeys

if __name__ == '__main__':
    dataList = [
        {
            'a': 3,
            'b': 2,
            'c': 1
        },
        {
            'e': 4,
            'd': 3
        },
        {
            'f': 6,
            'g': 5,
            'm': 1,
            'h': 9
        }
    ]
    print(selectKeys(dataList, 5))