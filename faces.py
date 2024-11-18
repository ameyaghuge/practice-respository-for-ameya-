def main():
    # Prompt the user for input, calls convert on that input
    result = convert(input("Are you having a good day or a bad day?"))
    # Print the result
    print(result)

def convert(emoji):
    # Replace :) with happy face emoji acquired in the input above
    happy = emoji.replace(":)", "\U0001F642")
    # Replace :( with sad face emoji in the variable above, linking both variables
    sad = happy.replace(":(", "\U0001F641")
    # Return the latter variable, the one that links both variables
    return sad

main()
#this is not my code, I used this person's code @luanpires1784 from youtube but I understood why my old code below did not work, it's because 
#I was using the exact same variable for both of the emoji’s which was incorrect, 
# and I didn’t have the unicode in my program, (Instead i had emojis), which meant python treated it as a string (or attempted to so it didn’t work)


#def convert():
    ##getting the user input here as a string
    #face = input("Good Morning how do you feel today?")
        
    #publish = face.replace =(":)","😐") 
    #in the terminal it says that the emoji string is read only 
    #print (publish)
#convert()

#I don't know why there is an issue with main over here 

    #now i need to return this input with any :) and or :( and convert those into actual emoji's
    #there has to be another way      
    # why is this emoji throwing up issues?
    #I put it into a string as well and that did not work, and now it says that it expects and expression 
    #sad.replace = ((":)"), count = 😕)
    #So i am stuck on getting it to convert the emoticons to emoji
        #I saw the .replace code on python's officical documentation

    #I need a method to convert the emojis
