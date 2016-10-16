# Interactive Parallel Computing

## Overview

1. Architecture
1. Installation & Setup

## Architecture

Cluster, Controller, Engine, Client

## Installation & Setup

1. Create virtualenv
2. install using `requirements.in`
3. Enable extensions (differences between `--user`, `--sys-prefix`, or nothing)
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
