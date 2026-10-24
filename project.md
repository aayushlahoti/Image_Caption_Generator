THIS FILE CONTAINS ALL THE RELATED INFO ABOUT THE PROJECT
IMAGE CAPTION GENERATOR 


PROJECT STRUCTURE 


image-caption-generator/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── config/
│   ├── __init__.py
│   └── config.py
│
├── models/
│   ├── __init__.py
│   └── caption_model.py
│
├── preprocessing/
│   ├── __init__.py
│   └── image_processor.py
│
├── services/
│   ├── __init__.py
│   └── caption_service.py
│
├── utils/
│   ├── __init__.py
│   ├── file_handler.py
│   └── validators.py
│
├── tests/
│   ├── test_preprocessing.py
│   ├── test_caption_service.py
│   └── test_validators.py
│
├── assets/
│   └── sample_images/
│
└── outputs/
    └── captions/

last two folders are for local storage purpose 