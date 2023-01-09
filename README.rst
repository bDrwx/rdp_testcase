============
rdp_testcase
============


.. image:: https://img.shields.io/pypi/v/rdp_testcase.svg
        :target: https://pypi.python.org/pypi/rdp_testcase

.. image:: https://img.shields.io/travis/bDrwx/rdp_testcase.svg
        :target: https://travis-ci.com/bDrwx/rdp_testcase

.. image:: https://readthedocs.org/projects/rdp-testcase/badge/?version=latest
        :target: https://rdp-testcase.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Task for pass interview to RDP.RU company
* Testcase1
  Реализован алгоритм быстрой сортировки с одним опортным элементом и тесты к нему.

- Testcase2
-- В корне проекта подготовлен Dockerfile для сборки образа и запуска контейнера
        ```
        docker build -t static:latest .
	docker run -it --rm --init -p 9191:9191 static:latest
        ```
        Запуститься контейнер который будет принимать соединения на порт TCP 9191
        и пересылать их WEB серверу, при этом ответы с MIME `text/http` будут проверяться
        на наличее нецензурной лексики и последующей замены на `***`.
        Я сознательно отступил от требований задяния потому что, звездочкии более явно показывают
        измененные части стрницы.

        Для перенаправления всего HTTP трафика на обработку прокси сервером на хостовой машине необходимо
        задать следующие параметры фаервола:
        ```shell
	sysctl -w net.ipv4.ip_forward=1
	iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 9191
	iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -j REDIRECT --to-port 9191
	```
        Обработка TLS не реализована так-как это потребует установку SSL сертификатов на клиентских машинах.

* Free software: MIT license
* Documentation: https://rdp-testcase.readthedocs.io.


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
