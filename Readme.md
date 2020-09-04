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

Also need run this once to initialize:

```python
import nltk
nltk.download('punkt')
```
