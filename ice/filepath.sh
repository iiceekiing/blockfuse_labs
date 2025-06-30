read -p "please enter file path: " path


read -p "please enter a file name you wish to delete (note: file must exist in $path: " file

echo " "

echo "deleting file......"

echo " "

rm $path/$file

echo "$file deleted successfuly!"
