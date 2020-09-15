# blog_django

## Create project
```python
python3 -m django startproject blog_django
```

## Make migration
1. ```python 
    python3 manage.py makemigrations
    ```
2. ```python
    python3 manage.py sqlmigrate pages 0001
    ```
3. ```python
    python3 manage.py migrate
    ```

## Create app [mainapp]
```python
python3 manage.py startapp mainapp
```

## Run
```python
python3 manage.py runserver
```