#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels_hints.py
#                                                                             
# PROGRAMMER:alaa emad faraj 
# DATE CREATED:13/3/2025                                  
# REVISED DATE:13/3/2025 
# PURPOSE: This is a *hints* file to help guide students in creating the 
#          function get_pet_labels that creates the pet labels from the image's
#          filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: EDIT and ADD code BELOW to do the following that's stated in the 
#       comments below that start with "TODO: 2" for the get_pet_labels function 
#       Please be certain to replace None in the return statement with 
#       results_dic dictionary that you create with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """

    in_files = listdir(image_dir)

    results_dic = dict()

    for idx in range(0, len(in_files), 1):

       if in_files[idx][0] != ".":
           pet_label = in_files[idx]
           pet_label = pet_label.split('.')[0]
           pet_label = pet_label.lower()
           pet_label_list = pet_label.split('_')
           pet_label_word=""
           for word in pet_label_list:
            if word.isalpha():
               pet_label_word+=word +" "
           pet_label_word = pet_label_word.strip()

           if in_files[idx] not in results_dic:
              results_dic[in_files[idx]] = [pet_label_word]
              
           else:
               print("** Warning: Duplicate files exist in directory:", 
                     in_files[idx])
 
    return results_dic
