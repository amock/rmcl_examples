# rmcl_examples_sim

This package contains all simulation environments for [rmcl_examples](/).

All environments are designed to benchmark localization algorithms, each posing a unique and challenging problem.
Most of these environments are intentionally constructed to prevent unique localization solutions.
Instead, the objective is to achieve the best possible reduction of the belief state informed by the sensor data.
A localization method is considered to fail if it produces a single definitive solution when multiple locations are equally probable.
The following table briefly summarize the best possible localization outcome for a robot equipped with motor encoders, an IMU and a 3D LiDAR:


|  World Name | Best possible localization |
|:------------|:-------------------------------------------------------|
|  `cube`     | 4 modes in your belief state probability distribution  |
|  `sphere`   | Equal probabilty for every pose located on the surface |
|  `cylinder` | Circular probability distribution |
|  `tray`     | Similar to cube but rectengular: 2 most probable modes. Dependent on the system and sensor noise, two more slightly less probable modes could exist. |
|  `corridor` | State: anywhere in the center of the corridor. Belief state: same probability everywhere in the center of the corridor |
|  `trays`    | 3x3 grid of `tray` model. Same most probable modes as for the `tray` environment but symmetrically distributed over a 3x3 grid. |
|  `avz`      | Old office floor of Osnabrück University in the AVZ building. Real world sample, still many ambiguities such as same sized rooms. |
