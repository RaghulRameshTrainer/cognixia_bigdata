'''
r (read) -> File will be opened with read mode. File must be there otherwise we will
            get FileNotFoundError
w (write) -> Open the file to write into it. if the exists already then it wil cleanup
            the existing content and start writing as a new file OR if the file is not
            there then it will create a file and write into it.
a (append) -> File will be opened for appending the data. If the will is already exists
            with some content, it will not remove those content , it will start appending
            new lines into it.If the file is not there then it will create a file and start
            writing into it
r+ ( read and write) -> File will be opened for both read and write purpose. * we must
                read the existing content first and start writing into it.
w+ (write and read) -> Will be opened for write and read. If the file exists the content
                of the file will be removed and starting as a new file.and we can read
                whatever has been written into it
rb (read binary) -> used for reading image/audio/video files.
wb (write binary) -> used for writing image/audio/video files

READ:
    readline()
    readlines()
    read()
'''
'''
with open('days.txt','r') as fh:
    # print(fh.readline(),end='')
    # print(fh.readline())
    # for day in fh.readlines()[1:6]:
    #     print(day[:3])
    print(fh.read())


with open("tech.txt",'w') as wfo:
    wfo.write('SPARK\n')
    wfo.writelines(['Spark\n','Hadoop\n','Python\n','Tableau\n','DWH'])

with open('tech.txt','a') as fh:
    fh.writelines(['\nHDFS\n','YARN\n','Sqoop\n','Hive\n','Kafka\n','Airflow'])


with open('tech.txt','r+') as venu:
    print(venu.read())
    venu.write('\n ------------END OF THE FILE----------------')


with open('tech.txt','w+') as fo:
    fo.writelines(['Chennai\n','Bangalore\n','Hyderabad\n','Pune\n','Gurgoan'])
    fo.seek(0,0)
    print(fo.read())
'''

with open(r'C:\Users\RaghulRamesh\OneDrive\Pictures\puppy.jpg','rb') as fh:
    with open(r'D:\TPERSONAL\pythonProject\pythonProject\dog.jpg','wb') as wfh:
        wfh.write(fh.read())

