# Interactive Parallel Computing

How to set up `ipyparallel` and test the notebooks from the Python Users Berlin
meetup.

## Installation & Setup

1. Create virtualenv
2. install `pip -r requirements.in`
3. Enable install & extensions:
    * with no flag, this will attempt to install to system space (will
      require root privileges)
    * `--user` will install into user space
    * `--sys-prefix` will install into the environment (my preferred choice)
   ```
   jupyter nbextension enable --py widgetsnbextension --sys-prefix
   jupyter nbextension install --py ipyparallel --sys-prefix
   jupyter nbextension enable --py ipyparallel --sys-prefix
   jupyter serverextension enable --py ipyparallel --sys-prefix
   ```
4. Create a profile
   ```
   ipython profile create --parallel --profile=mylocal
   ```
5. Start the notebooks `jupyter notebook`
6. Start a cluster either through the cluster tab in Jupyter or with `ipcluster
   start`.

The material covered in the meetup is introductory. Please delve into [the
documentation](https://ipyparallel.readthedocs.io/en/latest/) for more in-depth
descriptions and further topics.
