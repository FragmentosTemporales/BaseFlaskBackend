# Python Flask Backend 


## 1. Instalación

Para descargar la aplicación del repo, se debe escribir el siguiente comando:

```
$ git clone https://github.com/FragmentosTemporales/BaseFlaskBackend.git
```

### Variables de entorno

Al interior de la carpeta /Sripts debes crear un documento env.env el cual debe contener las siguiente variables, puedes guiarte con el documento example.env :

```
FLASK_ENV=dev

JWT_SECRET_KEY=
JWT_ACCESS_TOKEN_EXPIRES_HOURS=
JWT_ACCESS_TOKEN_EXPIRES_DAYS=
SECRET_KEY=

```

## 2. Ejecución

Para ejecutar la aplicación debes ingresar el siguiente comando:

```
$ flask run
```

## 3.- ¿Qué podemos ejecutar?

En el archivo *manage.py* podrás encontrar comandos por consola. Una vez hayas iniciado la aplicación deberás vincularla a la base de datos:

```
$ python manage.py db init
```

Luego deberás migrar:

```
$ python manage.py db migrate
```

Para finalmente upgradear:

```
$ python manage.py db upgrade
```



En estos momentos debes tener tu base de datos enlazada a tu aplicación, si es que quieres probar esto puedes ejecutar el siguiente comando:

```
$ python manage.py create-user --email example@mail.com --password 123456
```

En caso de estar funcionando todo correctamente debería retornar un mensaje tipo:

*"Usuario guardado correctamente"*


### ¿Y los testeos?

Si ya llegaste a este punto, podemos hablar de testeos.
Esta aplicación tiene desarrollados testeos para ciertos modelos, los cuales puedes ejecutar a través de la consola con el siguiente comando:

```
$ python manage.py test
```

*IMPORTANTE*

No sólo podrás ejecutar los testeos, esta función también incluye flake8, un corrector de sintáxis diseñado para python, podrás ejecutarlo con el siguiente código:

```
$ python manage.py test && flake8
```

<hr/>

## 4.- Bibliografía

A continuación te dejo el link con la documentación de Flask, específicamente la versión utilizada en este repositorio.

```
https://flask.palletsprojects.com/en/2.3.x/
```
