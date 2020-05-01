# --------------
#Code starts here
# Author- Babrit
#Function to read file
def read_file(path):
    
    #Opening of the file located in the path in 'read' mode
    f=open(path,mode="r")
    #Reading of the first line of the file and storing it in a variable
    sentence=f.readline()
    #Closing of the file
    f.close()
    #Returning the first line of the file
    return sentence
    

#Calling the function to read file
sample_message=read_file(file_path)
#Printing the line of the file
print(sample_message)

message_1=read_file(file_path_1)
message_2=read_file(file_path_2)
#Function to fuse message
def fuse_msg(message_a,message_b):
    
    #Integer division of two numbers
    quotient=int(message_b)//int(message_a)
    #Returning the quotient in string format
    return str(quotient)
    
#Calling the function to read file  

#Calling the function to read file


#Calling the function 'fuse_msg'
secret_msg_1=fuse_msg(message_1,message_2)

#Printing the secret message 

message_3=read_file(file_path_3)
print("Msg 3 ---",message_3)
#Function to substitute the message
def substitute_msg(message_c):
    
    #If-else to compare the contents of the file
    
    if message_c == 'Red':return 'Army General'
    elif message_c == 'Green':return 'Data Scientist'
    elif message_c == 'Blue':return 'Marine Biologist'
    #Returning the substitute of the message
    

#Calling the function to read file


#Calling the function 'substitute_msg'
secret_msg_2=substitute_msg(message_3)

#Printing the secret message
message_4 =read_file(file_path_4)
message_5 =read_file(file_path_5)

#Function to compare message
def compare_msg(message_d,message_e):
    #Splitting the message into a list
    a_list =message_d.split(" ")
    b_list =message_e.split(" ")
    #Splitting the message into a list
    #Comparing the elements from both the lists
    c_list=[x for x in a_list if x not in b_list]
    print(c_list)
    #Combining the words of a list back to a single string sentence
    
    final_msg=" ".join(c_list)

    print("final_msg------ ",final_msg)
    #Returning the sentence
    return final_msg

secret_msg_3=compare_msg(message_4,message_5)

#Printing the secret message
print("#Printing the secret message---- ",secret_msg_3)
ss=read_file(file_path_6)
    #Splitting the message into a list
ls=ss.split(" ")
    
 #Creating the lambda function to identify even length words
new_ls=[a for a in ls if len(a)%2==0]
message_6=" ".join(new_ls)
#Function to filter message
def extract_msg(message_f):
    
    #Splitting the message into a list
    a_list=message_f.split(" ")
    #Combining the words of a list back to a single string sentence
    even_word=lambda x:len(x)%2==0
    b_list=filter(even_word,a_list)
    final_msg=" ".join(b_list)
    #Returning the sentence
    return final_msg 
secret_msg_4=extract_msg(message_6)
#Calling the function to read file

#message_parts=[secret_msg_1,secret_msg_2,secret_msg_3,secret_msg_4]
#Calling the function 'filter_msg'


#Printing the secret message
print("111111",secret_msg_1)
print("222222",secret_msg_2)
print("333333333",secret_msg_3)
print("44444444",secret_msg_4)

#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]

secret_msg=" ".join(message_parts)


# define the path where you 
final_path= user_data_dir + '/secret_message.txt'

#Combine the secret message parts into a single complete secret message


#Function to write inside a file
def write_file(secret_msg,path):
    f=open(path,mode='a+')
    f.write(secret_msg)
    f.close()
       
    #Opening a file named 'secret_message' in 'write' mode


    #Writing to the file


    #Closing the file


#Calling the function to write inside the file    


#Printing the entire secret message


#Code ends here


