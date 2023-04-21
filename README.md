# invokeai_jpg_meta
Python script for InvokeAI, converts output PNG to JPEG and adds metadata from invoke_log.txt.

Requirements:
- PIL Python library
- exiftool in the %PATH% or in the current directory (https://exiftool.org/)

Usage:
meta_jpg.py must be run from the 'outputs' directory of InvokeAI ("py meta_jpg.py").
invoke_log.txt will be read, PNG converted as JPG and metadata added from invoke_log.txt
You will prompted to keep or delete PNG original files.

Code is under MIT licence.

To contact me about this tool : contact@jnss.eu
