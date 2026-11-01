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


Streamlit is an open-source Python framework that lets you build interactive web applications for data science, machine learning, and AI projects using only Python. You don't need to know HTML, CSS, or JavaScript to create a web interface.

As a Data Science student, you can think of Streamlit as a way to turn your Python scripts into a website with buttons, text boxes, charts, and file uploads.