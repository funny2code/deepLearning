# Collection of bash scripts
```bash

### Usage
 1) Copy the folder mybash/ where you want


 2) in your bashrc or zshrc,  add
     export PATH="../mybash/:$PATH"


 3) Initlize all alias,vars,...
     source init/init_all.sh


#### Example
     folder size        ~/mypathXYZ             #### Print folder size in Gb
     folder topfile     mypathXYZ/    20        #### Print 20 biggest size files
     folder recentifle  ~/mypathXYZ   10        #### Print recently modified files   


     folder backup   mypathXYZ/                           #### copied into default path ~/zarchive/mypath_suffix_20230202/
     folder backup   ~/mypathXYZ   ~/mypath_target/


```



##### Template of all script
```bash
#!/bin/bash
USAGE=$(cat <<-END

         SOME USAGE DOCS

     

END
)

#### Global Config. #################################
# set -x  # Output commands being run.
set -e  # Exit on error.


#### Global vars ###################################
FUNAME=`basename "$0"`
YMD=$(date '+%Y%m%d')



### Input Params ##################################
[ $# -eq 0 ] &&    echo $UUSAGE && exit    #### No input print doc
task="size"  &&  [ -z $1 ] &&     task=$1
ppath="~/"  &&  [ -z $2 ] &&     ppath=$2


### Core ###########################################
if [[ "$task" = taskXXXx ]]; then

       ### DO SOMTHING


exit 0
elif [[ "$task" = taskYYY ]]; then


       ### DO SOMETHING



exit 0
elif [[ "$task" =  taskZZZZ ]]; then


       ### DO SOMETHING


else
   echo $USAGE
fi
















```




#### Helpers
```bash

cconfig="$1"
if [[ -z $1 ]]; then 
   cconfig="config/prd/config_prd_real.yaml"
fi 






grepall () {
grep -r "$1" .
}



countlines () {
wc -l "$1"
}



countwords () {
wc -w "$1"
}



countcharacters () {
wc -c "$1"
}

modified24hrs () {
find . -mtime 0
}



replaceall () {
grep -rl "$1" . | xargs sed -i "s/$1/$2/g"
}



largerthan100mb () {
find . -type f -size +100M
}



```