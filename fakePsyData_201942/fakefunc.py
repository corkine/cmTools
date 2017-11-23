#!/usr/bin/env python3

# import os,random
# os.chdir("C:/Users/Administrator/Desktop")
# file = open("data.txt",'r')


def Fake_201942(inputfile='data.txt',howmuch=100,data_random='171',sex_random='13',age_random=(20,30)):
    import traceback
    try:
        import os,random
        data={}
        title=[]
        file = open(str(inputfile),'r')
        for title_codeNo in range(30):
            title.append("第%d题"%(title_codeNo+1))


        def readData():
            for user in file:
                try:
                    user_no = int(user.split("\t")[0])
                except:
                    continue
                user_data = user.split("\t")
                data[str(user_data[0])]={}
                data[str(user_data[0])]["user_time"]=user_data[1]
                data[str(user_data[0])]["user_Spend"]=user_data[2]
                data[str(user_data[0])]["user_Ip"]=user_data[3]
                data[str(user_data[0])]["user_Source"]=user_data[4]
                data[str(user_data[0])]["user_Source2"]=user_data[5]
                for small_title in title:
                    data[str(user_data[0])][small_title]=user_data[int(small_title[1])+5]
                data[str(user_data[0])]["user_sex"]=str(user_data[36])
                data[str(user_data[0])]["user_age"]=str(user_data[37])

                            
        readData()

        # print("测试-------------> 第111号被试：\n\n\t",data["111"])

        fake_data={}
        def fakeData():
            for fake_data_No in range(howmuch):
                fake_data[str(fake_data_No)]={}
                fake_data[str(fake_data_No)]["user_time"]="NO_TIME"
                fake_data[str(fake_data_No)]["user_Spend"]="NO_SPEND_TIME"
                fake_data[str(fake_data_No)]["user_Ip"]="0.0.0.0"
                fake_data[str(fake_data_No)]["user_Source"]="NOWHERE"
                fake_data[str(fake_data_No)]["user_Source2"]=random.choice(['1','2'])
                for small_title in title:
                    try:
                        while True:
                            fake_result = int(data[str(random.randint(1,len(data)))][small_title])+int(random.choices([-1,0,1],[int(data_random[0]),int(data_random[1]),int(data_random[2])])[0])
                            if fake_result > 0 and fake_result < 6:break
                    except:
                        pass
                    fake_data[str(fake_data_No)][small_title]= str(fake_result)
                fake_data[str(fake_data_No)]["user_sex"]=random.choices(['1','2'],[int(sex_random[0]),int(sex_random[1])])[0]
                fake_data[str(fake_data_No)]["user_age"]=random.randint(int(age_random[0]),int(age_random[1]))

        fakeData()

        # print("\n测试-------------> FAKE第111号被试：\n\n\t",fake_data["111"])
        # print("\n测试-------------> FAKE第112号被试：\n\n\t",fake_data["112"])


        newfile = open("result.txt",'w')
        for user_no in fake_data.keys():
            fake_user_data_info=''
            for data_item in fake_data[str(user_no)].values():
                fake_user_data_info += str(data_item)+'\t'
            newfile.write(str(str(user_no)+'\t'+fake_user_data_info+'\n'))
            
        newfile.close()


        return True,"完成数据处理，文件保存在此程序同目录下result.txt中"
    except:
        return False,traceback.format_exc()

if __name__=="__main__":
    print(Fake_201942(inputfile='data.txt')[1])
    print("FINISHED")
    