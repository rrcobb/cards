# Going Away Cards
It's sad to say goodbye, but we'll treasure the memories of CSSI forever. In order to give everyone a keepsake from the program, we want to give each participant a card with the signatures of all the other participants.

Keeping track of who signed what is hard, and no matter how much we like each other, it's still a pain to sign so many cards. Instead, let's write a Python program to sign the cards for us!

Thankfully, at each CSSI site, we have list of the names of all the participants in a file called names.txt. Your first task is to read the list of names in from that file and store them in a Python array. Check out the python documentation for files to see how it's done, and ask for help if you are stuck.

Once you have the names in Python, you want to write a card for each of the names in the list. First, figure out how to create and write to a new file. In the documentation, you'll find

f = open('file_name', 'mode')

The mode defines whether you can read, write, or append to the file, or a combination. Read more about python files.

Now that you can create a new file and write to it, the next step is to create a new file for each of the names in your array of names. Loop through your array, creating a new file for each participant, and write "Hello, " plus the name of the participant in each of those files. Once you have that working, go ahead and change the "Hello, " + name message to something that expresses how you really feel.

Finally, we want to sign everyone's name on each of the cards - but we don't want anyone to sign their own cards. It's up to you to figure out how to use loops and conditional statements to personalize the messages to each recipient.

Bonus Challenges:
 - Figure out how to send email with python, and write a program to send the cards to the participants.
- Write HTML to the output, and style your cards with some CSS. Maybe use templates and throw the project up on AppEngine. Go nuts.
- Solve the challenge again, but this time, with Javascript. Can it be done?
