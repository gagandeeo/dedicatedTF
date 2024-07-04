## This Documentation is related with GCP kubernetes deployment
# MobilenetV2 serving API

##  About
- API for object detection using mobilenetV2 model.
- Interactive [Documentation](https://dedicated-tensor.herokuapp.com/docs)

## Development
- For developing locally use following steps:
    - clone the repo
    - In root folder run
        - uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 5000
    - visit http://localhost:5000/docs for interactive documents