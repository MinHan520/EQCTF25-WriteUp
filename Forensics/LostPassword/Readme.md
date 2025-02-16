# Lost Password
I've already set up my web server, but I accidentally lost a Russian roulette from a Python script which then executed rm -rf / --no-preserve-root with root privileges. By the way, I also had a short-term lapse in memory and put my cloud account password inside the web folder. The last thing I remember is that I had a backup of my web folder and it was running a fresh installation of Nginx with no modifications yet. Please help me recover the password.

Author: vicevirus

## Solutions
ZIP File is provided, los.txt file is my solution file

<img width="380" alt="image" src="https://github.com/user-attachments/assets/ab77cb42-5247-4923-b8c4-1785a8fec827" />

The .zip file is locked and encrypted 

Using <b>bkcrack -L html.zip</b>

<img width="674" alt="image" src="https://github.com/user-attachments/assets/49aa3b82-7486-4948-8b70-116e9a896548" />

We can identify 2 types of files available in this ZIP file. It seems it is obvious where is the Flag. 

We will have to identify which type of method to use to decrypt the ZIP file. 

Enter the <b>zipinfo</b> function : 

<b>zipinfo -v html.zip</b>

<img width="651" alt="image" src="https://github.com/user-attachments/assets/fe2b3fdd-f7ac-4281-b20a-1a315c9f6c7d" />

It is encrypted so we are able to use bkcrack to crack the zip file.

Firstly, let's find the Key to decrypt the folder. By doing it we need to estimate what the index.html contains. So, let's create a plain.txt file

<img width="382" alt="image" src="https://github.com/user-attachments/assets/6eafa7ac-f3d4-4bb9-bf45-b7dd085bfdef" />


A plain text named <b>los.txt</b> is created and let's start to decrypt it.

Type : <b>bkcrack -C html.zip -c index.html -p los.txt</b>

<img width="700" alt="image" src="https://github.com/user-attachments/assets/456b8ea5-1f13-45fb-bffc-4b6149c8b05e" />

The keys are obtain <b>1d63e85a b3b66126 33619315</b> and we can start to retrive what we want by copy the whole zip file with our own set password

Type :  <b>bkcrack -C html.zip -k 1d63e85a b3b66126 33619315 -U flag.zip 1234</b>

Afterthat you will able to retrive the file with the password you set.

Flag : <b>EQCTF{bkkkkkcracckkkk_issss_useffulll_for_known_plaintextt}</b>

