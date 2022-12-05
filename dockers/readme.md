

Build are located here:
```

https://github.com/arita37/zbuild/tree/abuild


1) Create folder in dockers/mydocker  and all the docker files

2) Modify the github action
   https://github.com/arita37/myutil/actions/workflows/docker_build_zdocker1.yml


3) Comments the Docker you dont want to build.
   Add the ones you have and write bash code

         - name: Build and push
        run: |
          cd dockers/spark
          docker buildx build -f ./Dockerfile --tag artia37/spark243-hdp27:v1 --push .


4) Commit and push


5) In Github Actions, Trigger manually the github action
   by choosing the 
      Branch:   zdocker2

      Action:  docker_build_zdocker1.yml











#### Build Command :     https://github.com/arita37/myutil/actions/workflows/docker_build_zdocker1.yml


#### Docker definiton:     https://github.com/arita37/myutil/tree/zdocker2/dockers


##### Publish Registry:     https://hub.docker.com/u/artia37





```


