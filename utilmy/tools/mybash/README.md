# Collection of bash scripts
```bash

### Usage
 1) Copy the folder mybash/ where you want

 2) in your bashrc or zshrc,  add
     export PATH="../mybash/:$PATH"

 3) Initlize all alias,vars,...
     source init/init_all.sh


### Naming Convention:
   folder  size      ~/
   folder  topfile   ~/

   ### Custom alias in init/alias_init.sh 
   ddir size   ~/
   ddir topfile. ~/ 20




```





#### Helpers
```bash

cconfig="$1"
if [[ -z $1 ]]; then 
   cconfig="config/prd/config_prd_real.yaml"
fi 


navigatehome () {
cd ~
}



tail10 () {
tail -n 10 "$1"
}



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