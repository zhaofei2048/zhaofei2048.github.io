Title: How to activate a conda environment in Python code?
Tags: python; conda; shell

# Introduction & Method
We can control the flow of execution of shell commands/scripts with Python. If we want to use `gdalwarp`, `mrf2isis` (USGS/ISIS software), etc. in the shell script, the related conda environment should be activated first. The `subprocess` module of Python and the following codes can be used:
```python
import subprocess

# activate conda environment
subprocess.run(". ~/anaconda3/etc/profile.d/conda.sh && conda activate <env_name>",
    shell=True, check=True)

# Other shell command goes here, e.g.:
subprocess.run("gdalwarp --help",
    shell=True, check=True)

```

# Exceptional Case
The story here can be ended. However, some errors might occur:
```shell
/bin/sh: 6: /home/zhaofei/anaconda3/envs/isis/etc/conda/activate.d/geotiff-activate.sh: [[: not found
``` 
This is because the version of Python in the conda base environment is `3.11`. The version of Python in the <env_name> is `3.9`. The `...activate.d/geotiff-activate.sh` is too old for `...profile.d/conda.sh` in the base. Therefore, I modified the problematical line:
```shell
if [[ -n "$GEOTIFF_CSV" ]]; then
    export _CONDA_SET_GEOTIFF_CSV=$GEOTIFF_CSV"
fi
```
to:
```shell
if [ -n "${GEOTIFF_CSV:-}" ]; then
    export _CONDA_SET_GEOTIFF_CSV=$GEOTIFF_CSV"
fi
```