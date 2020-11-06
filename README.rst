Using `Jupyter Docker Stacks <https://jupyter-docker-stacks.readthedocs.io/en/latest/>`_.

Base notebook.


.. code-block:: bash

  $ docker run --rm -v $PWD:/home/jovyan/work -p 8888:8888 --name jp-base jupyter/base-notebook:python-3.7.6 

Using packages from the scientific Python ecosystem.

.. code-block:: bash

  $ docker run --rm -v $PWD:/home/jovyan/work -p 8888:8888 --name jp-scipy jupyter/scipy-notebook:feacdbfc2e89

Use `start-notebook.sh <https://jupyter-docker-stacks.readthedocs.io/en/latest/using/common.html#notebook-options>`_ with a `hashed password <https://jupyter-notebook.readthedocs.io/en/stable/public_server.html#preparing-a-hashed-password>`_.

.. code-block:: bash

  $ docker run --rm -v $PWD:/home/jovyan/work -p 8888:8888 --name jp-scipy jupyter/scipy-notebook:54462805efcb start-notebook.sh --NotebookApp.password='sha1:eb6bc651d99d:0f5a00b980a89650612f550ba50f472e7616cf03'

