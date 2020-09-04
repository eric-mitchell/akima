# Akima
![Titan AE](img/titan-ae.jpg)

Article extraction and annotation.

## Install
```
virtualenv venv
. ./venv/bin/activate
pip install -r requirements.txt
pre-commit install
```

Need to run this once to initialize nltk for smart article extraction:

```python
import nltk
nltk.download('punkt')
```

Start the application

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

1. Login to http://localhost:8000/admin
2. Create a new Article, just need to give it a URL, Akima will do the rest.
3. Now to go http://localhost:8000/a/<uuid>
4. Profit!
