# Import OS
import os
# Import PIL library
from PIL import Image


# Open and read InvokeAI log file
fichier = open("invoke_log.txt", "r")
contenu = fichier.read()

# Delete CR
contenu_sans_retours_a_la_ligne = contenu.replace("\n", "")

# Create new lines on "[...]"
contenu_final = contenu_sans_retours_a_la_ligne.replace("[Generated]", "\n[Generated]").replace("[Postprocessed]", "\n[Postprocessed]")

# Write a copy of the log to process
fichier_copy = open("invoke_log_copy.txt", "w")
contenu_final = contenu_final.split("\n", 1)[1]
fichier_copy.write(contenu_final)

# Close both files
fichier.close()
fichier_copy.close()


#########################
# Delete or keep PNG
#########################
del_PNG = input("Do you want to Delete (D) or Keep (K) PNG original files ? (default is 'K')")

# Open the copy of the log file
fichier = open("invoke_log_copy.txt", "r")

# Read lines
lignes = fichier.readlines()

# Close
fichier.close()

# Process each line
for ligne in lignes:

    # Get informations...
    info = ligne.split('"')
    fichier_png = info[1]

    # ...filename
    fichier_png = fichier_png.split("\\")[-1]

    if ligne.startswith("[Generated]"):
        # processing info (Sampler, steps...)
        autres_infos = info[3].replace('"', '') + info[4].replace('\n','') 
    else:
        autres_infos = info[4][2:].replace('\n','') 
    
    # To convert as JPG
    fichier_jpg = fichier_png[:-3] + "jpg"

    # ...only if PNG exists
    if os.path.isfile(fichier_png):     
        # converts PNG to JPG with PIL
        image = Image.open(fichier_png)
        image.save(fichier_jpg)
        # Adds meta with ExifTool
        print("exiftool -overwrite_original -P -comment=\"" + autres_infos + "\" " + fichier_jpg)
        os.system("exiftool -overwrite_original -P -comment=\"" + autres_infos + "\" " + fichier_jpg)

        # deletes PNG if asked
        if del_PNG == 'D':
            os.remove(fichier_png)
        
    else:
        print("Error : " + fichier_png)
        
# Delete work log
os.remove("invoke_log_copy.txt")
