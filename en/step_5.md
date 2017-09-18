## Step 3: Test the sound
That’s the hardware complete. Now for the software! We are going to use Python. Don’t worry if you haven't used it before: just follow the instructions and you will pick it up.
You will be using the command line to enter commands. To do this you will need to open a terminal window by clicking on the **terminal** icon: it looks like a computer screen, and is found three icons along from the menu button on your desktop.

1. Connect the speaker to the Raspberry Pi using the sound jack port.
1. Create a new folder called `whoopee` by typing the following command in the terminal and pressing **enter** on the keyboard:

   ``` bash
   mkdir whoopee
   ```

1. Next, use the following command to enter the folder you have just created:

   ``` bash
   cd whoopee
   ```

   We're going to need a sample sound file for this project so we'll use one from Sonic Pi.

1. Download a burp sample using the following command:

   ``` bash
   wget http://rpf.io/burp -O burp.wav
   ```

1. Now test that you can play the sound file using `aplay` by typing:

   ``` bash
   aplay burp.wav
   ```

   You should hear it from the speakers or headphones connected to your Pi. If you can’t hear anything, make sure that your speakers are connected correctly. If this still doesn’t work, you'll need to change your audio configuration.

   To switch audio to the headphone jack, return to the terminal window and type the following command:

   ``` bash
   amixer cset numid=3 1
   ```

1. If your Raspberry Pi is connected to the internet you could search for some suitable trumping sounds. They need to be in ‘wav’ format to work. Alternatively, you can [download our example sounds here](http://rpf.io/farts).
