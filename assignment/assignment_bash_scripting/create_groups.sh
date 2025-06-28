#!/bin/bash


# Step 1: Create a new group name it cohort-3-web2

sudo groupadd cohort-3-web2




# Step 2: Create users ali and bob if they don't already exist

sudo useradd -m ali
 echo  "Please enter password for ali: "
passwd ali


sudo useradd -m bob
 echo "Please enter password for bob:  "
passwd bob




# Step 3: Add ali and bob to cohort-3-web2 group

sudo usermod -aG cohort-3-web2 ali
sudo usermod -aG cohort-3-web2 bob



# Step 4: Create the folder ~/documents/web2/cohort3 (for current user)
mkdir -p ~/documents/web2/cohort3



# Step 5: Change the group of the cohort3 folder to cohort-3-web2
sudo chgrp -R cohort-3-web2 ~/documents/web2/cohort3




# Step 6: Give read & write permission to group
sudo chmod -R 770 ~/documents/web2/cohort3




# Step 7: Create another group cohort-2 and user ola

sudo groupadd cohort-2

sudo useradd -m ola
echo "Please enter password for ola: "
passwd ola

sudo usermod -aG cohort-2 ola


# Step 8: Verify ola has no access (manually test or explain below)
