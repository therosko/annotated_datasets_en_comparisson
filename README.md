## Comparing Annotated Datasets for Named Entity Recognition in English Literature

Should you stumble upon an issue or have questions, please contact [rivanova@wu.ac.at](mailto:rivanova@wu.ac.at).

Abstract:

The growing interest in named entity recognition (NER) in various domains has led to the creation of different benchmark datasets, often with slightly different annotation guidelines. To better understand the different NER benchmark datasets for the domain of English literature and their impact on the evaluation of NER tools, we analyse two existing annotated datasets and create two additional gold standard datasets. Following on from this, we evaluate the performance of two NER tools, one domain-specific and one general-purpose NER tool, using the four gold standards, and analyse the sources for the differences in the measured performance. Our results show that the performance of the two tools varies significantly depending on the gold standard used for the individual evaluations. 

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
* mount a volume to the container when running (`docker container run -v <path to folder>/v_mnt:/mnt -it ner /bin/bash`) and develop over VSCode (if working on a remote server, [connect to remote server over SSH ](https://code.visualstudio.com/docs/remote/ssh) ) (push and pull from the same local folder)

#### Next steps:
The following steps are available in the `get_setup.sh`. Those should be executed within the container. You can run all in one by calling the script itself.
* We use *annotated data* from
    * [Litbank](https://github.com/dbamman/litbank) Last commit: *a371cd678701fc98371355b328a1a6c4b58508a3*
    * [Dekker et al.](https://github.com/Niels-Dekker/Out-with-the-Old-and-in-with-the-Novel) Last commit *ad31ce1fa515dceabb8febbaa7aa235f3de47ebd*
    * Two additional annotated datasets created for this work, which can be found in the folder `annotation`
* Tools:
    * [BookNLP](https://github.com/dbamman/book-nlp) Last commit: *f58fbdbb018ba8bf2d836b764d0426afa0f7bc8c*. This version of BookNLP uses Stanford CoreNLP v.4.1.0 . 
    * [Flair](https://github.com/flairNLP/flair) *version 0.8*

#### Further info:
The evaluation of the tools was done using the [CoNLL evaluation script](https://www.clips.uantwerpen.be/conll2003/ner/bin/conlleval). Due to the various types of token labels within the tools and the gold standards, the published evaluation are calculated without considering prefixes. The folder `results` offers additional results for the tool Flair, which also consider prefixes. Such evaluation is not possible for BookNLP, as the tool does not use prefixes.