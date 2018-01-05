## Write a program in Python

1. Open Python 3 (IDLE) from the Programming menu and click on **File** and **New Window**. This will open a blank file.
1. Click on **File** and **Save As** and name the file `whoopee.py`
1. Type the following code into your file:

   ``` python
   import os
   import random
   from time import sleep
   from gpiozero import Button
   ```

   This part of the code pulls in all the libraries that you are going to use to write your program.

1. Then, you'll need to use the Button class in your code. You'll have to tell it that the button is on pin 2. To do this, write the following code in your new file:

   ``` python
   button = Button(2)
   ```

1. Now create a list of all your sound effects and store them inside a variable that you can call later on in your code:

   ``` python
   trumps = ['ben-fart.wav', 'ca-fart.wav', 'marc-fart.wav']
   ```

   In Python, square brackets are used to create a list. Each item in the list is separated by a comma.

1. Once all the setup needed in the code is complete, you can move on to writing the part of the program that will make something happen when the button is pressed. Begin by creating a loop using `while True:`.
1. Then, add `button.wait_for_press()` inside the loop by indenting by four spaces. Each time around the loop, the computer waits for the button to be pressed.
1. On the next line, use the `random.choice` function to select a sound at random from the list you created earlier. That selected sound needs to be stored inside another variable which you can call parp! Type `parp = random.choice(trumps)`.
1. The next line will play the sound selected at random using `aplay`, which you used earlier to test your sounds. Type `os.system("aplay {0}".format(parp))`.
1. Finally, add `sleep(2)` to pause the program before it starts the loop again.
1. Your code should look like this:

   ``` python
   while True:
     button.wait_for_press()
     parp = random.choice(trumps)
     os.system("aplay {0}".format(parp))
     sleep(2)
   ```

1. Save the file by clicking on **File** and **Save**.

1. Test that your code works by clicking on **Run** and **Run Module**. Use your hand to push the top plate of your Whoopi cushion down to make a connection between the tinfoil sheets and you should hear a fun sound. If it does not work first time, do not worry. Check your code through. Have you typed your code out **exactly** as you see it here?
