# MICP-L Segmentation

In SLAM, a robot continuously gathers environmental data to build a map.
Once a map exists, it serves as a prior: the robot can predict expected sensor readings at known locations.
By comparing these predictions with actual measurements, the robot can identify unexpected data and infer which parts of the map are implausible.
This enables segmentation of both unexpected observations and inconsistent regions of the map.

This package gives an overview over nodes that are implemented the beforementioned segmention procedure.


Start the robot by 

```console
ros2 launch 
```


