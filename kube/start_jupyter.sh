#! /usr/bin/env bash
mkdir -p ~/.jupyter
cp kube/jupyter_notebook_config.py ~/.jupyter/jupyter_notebook_config.py
jupyter-notebook --port=8840 --no-browser
