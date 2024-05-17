# RAID Analysis Zabbix Script

Scripts for Zabbix for analyzing RAID controllers.  
Made for 3 RAID controller vendors: MegaRAID, Adaptec, Intel. 

Returns 1 if there is an error or 0 if there are no errors.

The scripts collect data by words, ensuring the data is correct for different versions of the CLI.

# Installation
1. Download the latest Python version.
2. Download the vendor CLI:
   - MegaRAID -> storcli
   - Adaptec -> arcconf
   - Intel -> IntelVROCli
   
   Check the version on the vendor's site.
3. Git clone the repository.
4. Change the path to the CLI in the file.
5. Change Zabbix configuration:
   - UserParameter=<vendor>, python path_to_python_script
6. Add a Zabbix item.
7. Add a trigger:
   - last(<path_raid>)>0
8. Use it!
