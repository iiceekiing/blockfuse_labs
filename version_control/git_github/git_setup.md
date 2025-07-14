
# 🧰 How I Set Up Git and GitHub on My Laptop (setting up)

>  I want to share how I set up my Git and GitHub, generated SSH key, and connected everything. I also faced some errors but I fixed them. This is how I did everything step by step:

---

## 🧱 Step 1: I Installed Git

First, I opened my terminal (I’m using Ubuntu on WSL or Linux), and tried to install Git using:

```bash
sudo apt install git
```

### ❌ Error I saw:

```
E: Unable to locate package git
```

### ✅ How I solved it:


I found out I was supposed to **update my package manager first**. So I ran:


```bash
sudo apt-get update
```

Then after that, I installed Git again:

```bash
sudo apt install git
```

And it worked! I confirmed that Git was installed by checking the version:

```bash
git --version
```

It showed something like:

```
git version 2.34.1
```

---

## 🧑‍💻 Step 2: I Set My Git Name and Email

After installing Git, I configured my name and email (these are the details that will show on my GitHub commits):

```bash
git config --global user.name "iiceekiing"

git config --global user.email "myemail@example.com" #please use your email in the quotation placeholder
```

To confirm what I entered, I ran:

```bash
git config --list
```

---

## 🐙 Step 3: I Created a GitHub Account

1. I went to [https://github.com](https://github.com).

2. Clicked on **Sign Up**.

3. Entered my email, username, and password.

4. Verified my email and logged into my dashboard.

✅ Done! My GitHub account was ready.

---

## 🔐 Step 4: I Created SSH Key (To Link My GitHub and My Laptop)


This SSH key allows me to push code without entering my password every time.


In terminal, I ran:

```bash
ssh-keygen -t ed25519 -C "myemail@example.com"
```

When it asked for a location to save, I pressed **Enter** to use the default.

It created a key file at:

```
~/.ssh/id_ed25519
```


I added the SSH key to the SSH agent:


```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

---

## 📝 Step 5: I Added My SSH Key to GitHub


1. I copied the SSH key with:

```bash
cat ~/.ssh/id_ed25519.pub
```

2. I copied everything it showed (starts with `ssh-ed25519...`)

3. I went to GitHub:

   	* Clicked my profile picture > **Settings**
   	
	* On the left, clicked **SSH and GPG keys**
   
	* Clicked **New SSH key**
   
	* Gave it a name (e.g., "My Laptop") and pasted the key

4. Clicked **Add SSH key**

---

## 🌐 Step 6: I Tested the SSH Connection


I ran:


```bash
ssh -T git@github.com
```

It asked me:

```
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

I typed:

```
yes
```

Then it showed:

```
Hi iiceekiing! You've successfully authenticated...
```

✅ SSH was working!

---

## 🛠️ Another Error I Faced


### ❌ Error:


After creating my GitHub repo and cloning it, I got this error when I tried to push:


```
Permission denied (publickey).
fatal: Could not read from remote repository.
```

### ✅ How I solved it:


I found out I cloned the repo using **HTTPS** link instead of **SSH**.


So I deleted the folder and cloned again, this time using the SSH link:



```bash
git clone git@github.com:iiceekiing/my-repo.git
```


Then push worked perfectly.


---


## ✅ Summary of All Steps


1. Installed Git with `sudo apt update && sudo apt install git`

2. Configured my Git name and email

3. Created a GitHub account

4. Generated SSH key with `ssh-keygen`

5. Added SSH key to GitHub

6. Tested with `ssh -T git@github.com`

7. Cloned repo using SSH

8. Fixed two common errors:


   	* *"Unable to locate package git"* (solved by updating first)
  
	 * *"Permission denied (publickey)"* (solved by using SSH instead of HTTPS)

---

# If you’re a beginner like me from Nigeria, I hope this helps you set up your Git and GitHub without fear.

