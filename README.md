# DataStream Plotter

The Datastream plotter is a debugging tool for standing die [SD] testing on the HDMT. It addresses the issue of matching test instances with anomalies/points of interest observed while performing SD tests.

It also provides autonomous joining and plotting of data from all pins selected on the datastream. Channels such as TDAU's [Temperature readings], VCC [Power Supply voltages, currents, power draw & resistance] and Test Instances can be recorded. To use the Datastream Plotter you will need to stream to file when testing on the HDMT. Further information provided below.

For example the sample Datastream output below\
![image](https://gitlab.devtools.intel.com/ianimash/datastream-plotter/-/wikis/uploads/87d61e99a7cbc017c022287f7e25d346/image.png)

This will be joined into a single JMP table & variables will be renamed appropriately\
![image](https://gitlab.devtools.intel.com/ianimash/datastream-plotter/-/wikis/uploads/1a36d3e194f0df0df51f68bc4055014d/image.png)

An interactive JMP graph will be generated that will allow you to correlate events with test instances\
![image](https://gitlab.devtools.intel.com/ianimash/datastream-plotter/-/wikis/uploads/a0fce5a86b0a89d01be5c3f0630a215c/image.png)

Note# It is advised that you save a local copy of the datastream files you wish to analyse to ensure best performance.

### How to use:

#### Step 1
Download the tool from here: https://goto/datastreamexe

#### Step 2
Open the DataStream Plotter.exe then press "y" and enter to install tool\
![image](https://gitlab.devtools.intel.com/ianimash/datastream-plotter/-/wikis/uploads/58acf715b1d1704ab3bf0be4d055d86e/image.png)
![image](https://gitlab.devtools.intel.com/ianimash/datastream-plotter/-/wikis/uploads/d2a7038e9e203d193ef811d50da957cf/image.png)

After installation there will be new folders generated in the same file location as the exe\
![image](https://gitlab.devtools.intel.com/ianimash/datastream-plotter/-/wikis/uploads/4529356ab4a73232073c1c9ba7e74627/image.png)

The Datastream Plotter will automatically open after installation\
![image](https://gitlab.devtools.intel.com/ianimash/datastream-plotter/-/wikis/uploads/2e56f4eb22bbd4a2f116ee099f7584da/image.png)

#### Step 3
Click on the "Select DataStream Folder" and navigate to the file location where the datastream output files are stored then click select folder.
![image](https://gitlab.devtools.intel.com/ianimash/datastream-plotter/-/wikis/uploads/90fa86f0bb4ff1d3f0018eec3fc3c774/image.png)

A pop-up window will appear the inform you of the selected folder, click ok\
![image](https://gitlab.devtools.intel.com/ianimash/datastream-plotter/-/wikis/uploads/a5de00618fed8a507aa4c41c7916b587/image.png)

#### Step 4
Now click the "plot DataStream" button and wait for the JMP table and graph to appear [generally ~1min]
![image](https://gitlab.devtools.intel.com/ianimash/datastream-plotter/-/wikis/uploads/55127d459627d9f195913f9b4d98aa71/image.png)

#### Step 5
Using "Test Instance Interactive Graph", drag the variables of interest onto the Y axis.
![image](https://gitlab.devtools.intel.com/ianimash/datastream-plotter/-/wikis/uploads/6634910b285d8ef8b97b3d55d82c231d/image.png)

Zoom into the area of interest and hover over points using mouse to get details
![image](https://gitlab.devtools.intel.com/ianimash/datastream-plotter/-/wikis/uploads/c14fa39fd014a13a42f3062da1a27350/image.png)

### How to get datastream data:

#### Step 1
First load and init the test program

#### Step 2
Select "DataStream" on the HDMT Site Controller
![image](https://gitlab.devtools.intel.com/ianimash/datastream-plotter/-/wikis/uploads/d286281d6b87eb77d182dc6a8e3fbc87/image.png)
![image](https://gitlab.devtools.intel.com/ianimash/datastream-plotter/-/wikis/uploads/926d0309a88382ef52ba4b7b3e2d2422/image.png)

#### Step 3
Once open click select pins and select up to 10 pins you would like to monitor and click ok.
![image](https://gitlab.devtools.intel.com/ianimash/datastream-plotter/-/wikis/uploads/b933890c7f9a0113d0304587d04f890d/image.png)

#### Step 4
Now click "Stream to File" and navigate to the folder where you wish to store the data\
![image](https://gitlab.devtools.intel.com/ianimash/datastream-plotter/-/wikis/uploads/f04420e4085ef3a5715fe49e5eaed007/image.png)

#### Step 5
Next press start all and return to the Site Controller to begin the test
![image](https://gitlab.devtools.intel.com/ianimash/datastream-plotter/-/wikis/uploads/81ea42c55a94ac42376dc99e9aeb46b9/image.png)
![image](https://gitlab.devtools.intel.com/ianimash/datastream-plotter/-/wikis/uploads/f1dd007ca3cb8b83c2297cfdf74d65a8/image.png)

#### Step 6
Finally when testing has completed return to the datastream and click "Stop All"

![image](https://gitlab.devtools.intel.com/ianimash/datastream-plotter/-/wikis/uploads/1b0b8c7a32b5eb5bc395d1f4cb0af567/image.png)

![image](https://gitlab.devtools.intel.com/ianimash/datastream-plotter/-/wikis/uploads/bf40c6ca1e4245d91e345c8fc026eee2/image.png)

