Are you tired of tedious sequence uploads when comparing two sequences using Blast's web interface? A local installation of the Blast program can also compare two sequences, but it lacks the practicality of a web interface. Here is a simple GUI to use blastn locally. Installation of ncbi-blast+, Python, and Tkinter is required for functionality.

1. install blast locally

for Ubuntu and Debian users

sudo apt install ncbi-blast+

2. install python and tkinter

sudo apt install python3-tk

3. put bl2seq and blast2seq.py in a folder in your $HOME directory

To ensure proper pasting of query and subject sequences, the bl2seq script must be run from a folder to which you have write permission.

4. edit line 3 of bl2seq script to locate blast2seq.py in your correct path (for example /home/$HOME/bl2seq/ or /usr/local/bin/) and make the script executable

chmod +x bl2seq

5. run by typing in the console

python3 blast2seq.py

or

./bl2seq

Alternatively, you can use bl2seq to create an application launcher on your desktop.

![blast2seq GUI](https://github.com/matiajan/blast2seq-frontend/blob/main/blast2seq.png)
