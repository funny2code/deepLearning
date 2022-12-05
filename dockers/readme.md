
Build And publish from Github Actions
```

0) Go on online editor  (  zdocker2 branch)

    https://github.dev/arita37/myutil/tree/zdocker2/dockers


1) Create folder in dockers/mydockerXXXX  and all the docker files


2) Go to github action
   https://github.com/arita37/myutil/actions/workflows/docker_build_zdocker1.yml


3) In the github action, Comments the Docker you do NOT want to build.
   Add the ones you have and write bash code

         - name: Build and push
        run: |
          cd dockers/spark
          docker buildx build -f ./Dockerfile --tag artia37/spark243-hdp27:v1 --push .



4) Commit and push



5) Go to gihub action page:
    https://github.com/arita37/myutil/actions?query=branch%3Azdocker2



5) In Github Actions,
   Trigger manually the github action
   by choosing the 

      Branch:   zdocker2
      Action:  docker_build_zdocker1.yml






```

![image](https://user-images.githubusercontent.com/18707623/205652005-831bed7b-5342-4a9c-a411-7dff9521067d.png)







#### Infos
```


     Build Command :     https://github.com/arita37/myutil/actions/workflows/docker_build_zdocker1.yml

     Publish Registry:     https://hub.docker.com/u/artia37

     Docker definiton:     https://github.com/arita37/myutil/tree/zdocker2/dockers

    
                            https://github.com/arita37/zbuild/tree/abuild

```