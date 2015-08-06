#Going Away Cards
It's sad to say goodbye, but we'll treasure the memories of CSSI forever. In order to give everyone a keepsake from the program, we want to give each participant a card with the signatures of all the other participants.

Keeping track of who signed what is hard, and no matter how much we like each other, it's still a pain to sign so many cards. Instead, let's write a Python program to sign the cards for us!

Thankfully, at each CSSI site, we have list of the names of all the participants. You want to write a card for each of the names in the list.

We want to sign everyone's name on each of the cards - but we don't want anyone to sign their own cards. Write a function `everyone_sign()` that takes in an array of names, and returns a dictionary of messages. The message can say anything, but it must also include the other names in the list.

For input:
```python
["See-Mong Tan", "Victoria Kirst", "Matthew Levine", "Eric Breck", "Riccardo Crepaldi"]
```

Return:
```python
{
  "See-Mong Tan":"Thank You! Your friends, Victoria Kirst, Matthew Levine, Eric Breck, Riccardo Crepaldi",
  "Victoria Kirst":"Thank You! Your friends, See-Mong Tan, Matthew Levine, Eric Breck, Riccardo Crepaldi",
  "Matthew Levine":"Thank You! Your friends, See-Mong Tan, Victoria Kirst, Eric Breck, Riccardo Crepaldi",
  "Eric Breck":"Thank You! Your friends, See-Mong Tan, Victoria Kirst, Matthew Levine, Riccardo Crepaldi",
  "Riccardo Crepaldi":"Thank You! Your friends, See-Mong Tan, Victoria Kirst, Matthew Levine, Eric Breck"
}
```

### Bonus Challenges:
- Write a solution that doesn't use nested loops 
- Figure out how to send email with python, and write a program to send the cards to the participants.
- Instead of returning a dictionary of strings, output files of HTML!  Style your cards with CSS and put them online.
- Solve the challenge again, but this time, with Javascript. Can it be done?
