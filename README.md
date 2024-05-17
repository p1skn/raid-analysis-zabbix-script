# raid-analysis-zabbix-script
Scripts for Zabbix for analyzing raid controllers. 
Made for 3 vendors: 
megaraid (storcli), 
adaptec (arcconf), 
intel (IntelVROCli). 

Return 1 if there is an error or 0 if there are no errors.

The scripts collect data by words, that is, the data will be correct for different versions of the cli.
