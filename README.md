**pcf-memory-calculator
**

**Simple Python Script that takes in a file as input which is derived from a Cloud Foundry cf command set.**


Pull the container from  dockerhub:

`docker pull leepereira/pcf-mem-usage:v1` 

Run the Docker container. Make sure that the mount for the container has the same file name as shown in the example below : /app/abc.csv

`docker run -v filenamefromcf.csv:/app/abcd.csv leepereira/pcf-mem-usage:v1 `

