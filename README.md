##

Abstract:

---------
## How to replicate the experiment

#### Setup and requirements
The standard setup uses [Docker](https://docs.docker.com/get-docker/). Once installed follow the steps:
1. create a folder (`mkdir v_mnt`), which will be mounted to the container
2. inside of this folder create a directory called Git `mkdir Git`
3. clone this repository inside of the Git directory `git clone <repo_path_here> .` (note: don't forget the dot in the end ;)
4. navigate to the cloned repository `cd Git`. The Dockerfile and requirements.txt are located there.
5. build the docker image `sudo docker build -t ner .`
6. run container with the mounted volume (any of the following works):
* directly from the command line `docker container run -v <path to  folder>/v_mnt:/mnt -it ner /bin/bash`
* (preffered by me) mount a volume to the container when running (`docker container run -v <path to folder>/v_mnt:/mnt -it ner /bin/bash`) and develop over VSCode (if working on a remote server, [connect to remote server over SSH ](https://code.visualstudio.com/docs/remote/ssh) ) (push and pull from the same local folder)

#### Next steps:
The following steps are available in the `get_setup.sh`. Those should be executed within the container. You can run all in one by calling the script itself.
* We use *annotated data* from
    * [Litbank](https://github.com/dbamman/litbank) Last commit: *a371cd678701fc98371355b328a1a6c4b58508a3*
    * [Dekker et al.](https://github.com/Niels-Dekker/Out-with-the-Old-and-in-with-the-Novel) Last commit *ad31ce1fa515dceabb8febbaa7aa235f3de47ebd*
    * Two additional annotated datasets created for this work, which can be found in the folder `annotation`
* Tools:
    * [BookNLP](https://github.com/dbamman/book-nlp) Last commit: *f58fbdbb018ba8bf2d836b764d0426afa0f7bc8c*. This version of BookNLP uses Stanford CoreNLP v.4.1.0 . 
    * [Flair](https://github.com/flairNLP/flair) *version 0.8*

