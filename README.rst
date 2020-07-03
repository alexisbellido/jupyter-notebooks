Using `Jupyter Docker Stacks <https://jupyter-docker-stacks.readthedocs.io/en/latest/>`_.

Base notebook.


.. code-block:: bash

  $ docker run --rm -v $PWD:/home/jovyan/work -p 8888:8888 --name jp-base jupyter/base-notebook:python-3.7.6 

Using packages from the scientific Python ecosystem.

.. code-block:: bash

  $ docker run --rm -v $PWD:/home/jovyan/work -p 8888:8888 --name jp-scipy jupyter/scipy-notebook:54462805efcb
