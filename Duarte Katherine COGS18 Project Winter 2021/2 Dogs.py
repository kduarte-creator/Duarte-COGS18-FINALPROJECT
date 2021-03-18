class Dogs():
    
 #Adapted code from Lecture 13 on Classes, I have gone more in depth to include more characteristics under the instance to help identify the dog and added two unique functions that were not included in the lecture's example.


    def __init__(self,name,breed,age,size):
        self.name = name 
        self.breed = breed 
        self.age = age 
        self.size = size
        self.directory
    
    
    
    def add_to_directory(self, dog_info):
        """This function takes the list dog_info which takes a 
        dog's name and their information then adds it to a dictionary.
        
           PARAMETERS: 
           dog_info key takes in the dog's name
           dog_info value takes in the dog's breed, age, and size."""
          
        self.directory[dog_info[0]]= dog_info[1] 
        
   
    
    
    def breed_interations(self):
        """This method determines if a dog, considering their breed, 
        can play freely or if they require supervision when around other dogs.
           
           RETURNS: 
           out(str): The advisement of whether the dog can play with or without supervision. """
       
        carefree_dogs = ['French Bulldog', 'Bulldog', 'Labrador Retriever','Maltese',
                         'Great Dane', 'Greyhound', 'Golden Retriever', 'Collie', 
                         'Charles Spaniel', 'Tibetan Terrier', 'Saint Bernard', 
                         'Newfoundland', 'Mastiff', 'Irish Wolfhound', 'Irish Setter', 
                         'English Toy Spaniel', 'Bichon Frise']
        
        if dog in carefree_dogs:
            out = 'They can play!' 
        else: 
            out = 'Need to play with supervision.'
        return out 

#Functions 

def age_sort(current_roster):
    """The purpose of this function is to sort younger dogs, middle-aged dogs, and older dogs. 
    Given dictionary roster, it will return a list with the category each dog belongs in.
       
       PARAMETERS: 
       current_roster(dict): keys are dog's name and the values are their information.
       
       RETURNS: 
       out(list): List of each age category the dogs in the roster belong to. """

    output_list = []
    young_ages = [0,1,2,3]
    mid_ages = [4,5,6,7,8]
    
    for dog in current_roster: 
        if current_roster.values() in young_ages: 
            output_list.append('young_dog')
        elif current_roster.values() in mid_ages:
            output_list.append('mid_age_dog')
        else: 
            output_list.append('older_dog')
        return output_list 
      
    

def capacity_counter(current_roster):
    """This function loops through the dictionary of dogs 
    to count whether or not the facility is over, under, or at capacity.
       
       PARAMETERS: 
       current_roster(dict): keys are dog's name and the values are their information.
       
       RETURNS: 
       out(str): describing the facility's status of capacity. """
    
    counter = 0
    capacity = 20
    
    for dog in current_roster: 
        counter += 1 
         
        if counter > capacity:
            out = 'Sorry, we can not take more dogs.'
        elif counter == capacity:
            out = 'We are at capacity.'
        else:'We have room for more dogs!'
    
    return out
