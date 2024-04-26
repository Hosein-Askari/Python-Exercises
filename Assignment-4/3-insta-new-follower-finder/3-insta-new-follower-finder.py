import instaloader
import getpass

#read old followes

f = open("followers.txt","r")
old_followers = []
for line in f:
        old_followers.append(line)
f.close()



#login insta 

insta = instaloader.Instaloader()

username = input("enter usernmae : ")
password = getpass.getpass("enter password : ")

insta.login(username,password)
print("congratulation, succesfully login")

profile = instaloader.Profile.from_username(insta.context,"hosein_askari")


#find new_followers

new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower)



#compare new folloers vs old ones
for follower in new_followers:
       if follower not in old_followers:
              print("new_follower : ",follower)


#update_list_(write)

f = open("followers.txt","w")
for follower in new_followers:
        f.write(follower +" \n")
f.close()

