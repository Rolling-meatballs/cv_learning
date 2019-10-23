

#将图片的数组写入txt文档，方便纠错
def read_pic(lay, name):
    # np.savetxt('data.txt', lay)
    # row = len(lay)
    # log(name)
    file_handle = open(name, mode='w')

    for i in lay:
        # data = str(lay[i])
        # all_data = data + '/n'
        # file_handle.write(all_data)
        i = str(i).strip('[').strip(']').replace(',', '').replace('\'', '') + '\n'
        file_handle.writelines(i)
    file_handle.close()

