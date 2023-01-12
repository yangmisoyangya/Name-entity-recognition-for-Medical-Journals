
# Name Entity Recognition for Medical journals

  This project aims to streamline and helps to properly  identify the information needed in medical texts and help medical staff make clinical decision-making, evidence-based medicine, and epidemic disease monitoring.

Named entity recognition (NER) helps you easily identify the key elements in a text, like names of people, places, brands, monetary values, and more. Extracting the main entities in a text helps sort unstructured data and detect important information, which is crucial if you have to deal with large datasets.

We provide pre-trained  model for Name Entity Recognition for Medical journals. The model was trained on medical journals datatasets and annotated using NER Text Annotator
- [Annotator for NER](https://tecoholic.github.io/ner-annotator/)

We use Spacy library to train our model(https://spacy.io/models)
and also scispacy where scispaCy is a Python package containing spaCy models for processing biomedical, scientific or clinical text.

The pre-trained model can recognize such entities as:
- Disease and Chemicals
- AMINO_ACID, ANATOMICAL_SYSTEM, CANCER, CELL, CELLULAR_COMPONENT, DEVELOPING_ANATOMICAL_STRUCTURE, GENE_OR_GENE_PRODUCT, IMMATERIAL_ANATOMICAL_ENTITY, MULTI-TISSUE_STRUCTURE, ORGAN, ORGANISM, ORGANISM_SUBDIVISION, ORGANISM_SUBSTANCE, PATHOLOGICAL_FORMATION, SIMPLE_CHEMICAL, TISSUE

## PERFORMANCE of the Model
Our models achieve performance within 3% of published state of the art dependency parsers and within 0.4% accuracy of state of the art biomedical POS taggers.

![performance](https://github.com/yangmisoyangya/Name-entity-recognition-for-Medical-Journals/blob/main/screenshots/performance.png?raw=true)

After we use the pre-trained Model with the dataset we have ,we can update the pre-trained model and customize it according to our prefferences.
### Reference for updating the model
https://www.machinelearningplus.com/nlp/training-custom-ner-model-in-spacy/

## Usage
Installing

- The toolkit is implemented in Python 3 and requires a number of packages. To install all needed packages use:
```bash
$ pip3 install -r requirements.txt
```
## Deployment

To deploy this project in your local server run in your 
cmd with current directory

```bash
  python app.py
```


## Interface

![interface](https://github.com/yangmisoyangya/Name-entity-recognition-for-Medical-Journals/blob/main/screenshots/interface.jpg?raw=true)

## output Result

![result1](https://github.com/yangmisoyangya/Name-entity-recognition-for-Medical-Journals/blob/main/screenshots/result1.png?raw=true)

## original

![original](https://github.com/yangmisoyangya/Name-entity-recognition-for-Medical-Journals/blob/main/screenshots/original.png?raw=true)

## output Result

![result](https://github.com/yangmisoyangya/Name-entity-recognition-for-Medical-Journals/blob/main/screenshots/result.png?raw=true)


## Author

- [@yangmisoyangya](https://github.com/yangmisoyangya)


## Acknowledgement 

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
- https://allenai.github.io/scispacy/
- https://tecoholic.github.io/ner-annotator/
- https://spacy.io/models
- https://www.machinelearningplus.com/nlp/training-custom-ner-model-in-spacy/
