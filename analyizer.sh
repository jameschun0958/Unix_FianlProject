#! /bin/sh

source_path=`pwd`
usr=`whoami`
dir="/home/$usr/text_Analyizer"



option_help() {
	
	echo "usage: analyizer.sh "
	echo "analyizer [Option] <name>"
	echo
	echo "Option: "
	echo "-f, --file		      Analysis a file and search."
	echo "-k, --key sentences	  show the result of possible topic of the article."
	echo "-h, --help	          Show this help message."
	echo "\n"
}

if [ $1 = "-f" ];then
	#echo "you type -f"
	if [ $3 = "-k" ];then
		echo "================== The key sentences in article of $2 =================="
		python3 $dir/text_analyizer.py "$2" "$4"
		echo
	else
		echo "================== The seraching result of $2 ================="	
		python3 $dir/text_analyizer.py "$2" 1 | googler
		echo
	fi
	
elif [ $1 = "-h" ];then
	option_help
else
	echo "\nanalyizer: error: unrecognized arguments: $*\n\n"
	option_help
fi