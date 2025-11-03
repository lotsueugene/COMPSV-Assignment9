class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    def __init__(self,name):
        self.name=name
        self.friends=[]

    def add_friend(self,friend):
        if friend not in self.friends:
            self.friends.append(friend)
        else:
            return f'{friend.name} is already friends with {self.name}'


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
    def __init__(self):
        self.people={}
    
    def add_person(self,name)->None:
        if name not in  self.people:
            self.people[name]=Person(name)
        else:
            return f'{name} exists in network!'

    def add_friendship(self,person1_name:str,person2_name:str)->None:
       #Handing friends that are not in network
       missing=[]
       if person1_name not  in self.people:
           missing.append(person1_name)
       if person2_name not in self.people:
           missing.append(person2_name)
       if missing:
           if len(missing)==1:
                print(f'Friendship not created. {missing[0]} does not exist in network')
           elif len(missing)==2:
               print(f'Friendship not created. {missing[0]} and {missing[1]} does not exist in network')
           return
       
       person1=self.people[person1_name]
       person2=self.people[person2_name]
       person1.add_friend(person2)
       person2.add_friend(person1)
           
    def print_network(self)->None:
        for name, person in self.people.items():

            friend_names=[]
            for f  in person.friends:
                 friend_names.append(f.name)

            
            
            s='' #Temporary string that will hold names of friends
            for i in range(len(friend_names)):
                s=s+ friend_names[i]
                if i<len(friend_names)-1:
                    s=s+ ", "
            
            print(f'{name} is friends with: {s}')


#         #Testing Person Class
# person_=Person('Eugene')
# new_friend=Person('Derrick')

# print(person_.name)
# person_.add_friend(new_friend)

# print(person_.friends[0].name)


        #Testing
if __name__=='__main__':
    network = SocialNetwork()

    network.add_person("Alex")
    network.add_person("Jordan")
    # print(network.people)
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")




    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Jordan", "Johnny") # "Friendship not created. Johnny doesn't exist!"
    network.add_friendship("Eugene", "Johnny") #Eugene and Johnny does not exist in network
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    network.print_network()

#A graph is the best structure to reepresent a social network  because it naturally shows connections between people. In graph, each person can be seen as a node, and each friendship can be
#represented as an edge linking two nodes(Each person is represented as a node and they are connected via edges). A simple lost will not work as well because it stores data in a single straight
# line and does not have the ability to show the connections between them. A tree would also fail because trees have a hierachical structure with one root with  branches flowing downward, no connection to others.
#When building the program, I noticed that adding friends required updating both people's lists to keep the network accurate. This makes the process clear. Also, printing takes more time as more peoplee and friendships are formed.