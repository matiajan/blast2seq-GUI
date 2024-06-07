Are you tired of the tedious process of uploading sequences one by one when using BLAST's web interface for sequence comparison? While a local installation of the BLAST program can compare two sequences, it lacks the convenience of a web interface. Here is a simple GUI to use BLAST locally with ease. To get started, you'll need to install NCBI-BLAST+, Python, and Tkinter.

1. Install BLAST locally:

For Ubuntu and Debian users:

sudo apt install ncbi-blast+

2. Install Python and Tkinter:

sudo apt install python3-tk

3. Place the bl2seq and blast2seq.py files in a folder within your $HOME directory.

To ensure the bl2seq script will work correctly when pasting query and subject sequences, it must be run from a folder where you have write permissions.

4. Edit line 3 of the bl2seq script to specify the correct path to blast2seq.py (e.g., /home/$HOME/bl2seq/) and make the script executable:

chmod +x bl2seq

5. Run the script:

./bl2seq
