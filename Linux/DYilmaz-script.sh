#!/bin/bash

# Start of script
# Script for archive folder

printf '\n\n'
printf "Script d\'archivage \n\n"

function archive_dir
{
	while(true); do
		# Saisie du chemin du dossier
		printf '\nEntrer le chemin du dossier à archiver : '
		read folder

		# Test si l'utilisateur veut sortir de la fonction
		if [ $folder == 'exit' ]; then
			break;
		fi

		# Test si le dossier existe
		if [ -d "$folder" ]; then
			if [ ! -d "./archive" ]; then
				mkdir archive
			fi

			# Definie le nom de l'archive
			archive_name=${folder##*/}"-archive"
			archive_path="./archive/"$archive_name".tar"
			itt=1
			
			flagarch=true
			
			# Boucle pour verifier le nom
			while($flagarch); do
				if [ -f $archive_path ] ; then
					echo 'file exist';
					archive_path="./archive/"$archive_name"-"$itt".tar"
					itt=$(( $itt + 1 ))
				else
					flagarch=false
				fi
			done
			
			tar -cvf $archive_path $folder
			
			if (( $? == 0 )); then
				printf "\nVotre achive a était dans : "$archive_path"\n"
			else
				printf "\nErreur creation archive\n"
				break;
			fi
			
			printf "\nVoulez-vous compresser l\'archive ? (1: Oui, 2: Non) : "
			read choice2
			
			if (( $choice2 == 1 )); then
				gzip $archive_path
				
				if (( $? == 0)); then
					printf "\nCompréssion réussi\n"
				else
					printf "\nErreur compréssion\n"
				fi
			fi
			
			
			break;
		else
			printf "\nLe dossier n\'existe. Try again or type exit.\n"
		fi
	done
}


while (true) ; do

	printf "Menu :\n"
	printf "\t1) Archiver un dossier\n"
	printf "\t2) Désarchiver\n"
	printf "\t3) Sortir\n"

	printf 'Faite votre choix : '
	read choice

	case $choice in
		1)  archive_dir
			;;
		2)  echo 'unarchive'
			;;
		3)  echo 'Exit'
			break
			;;
	esac
	printf '\n\n'
done

