# MICP-L GPU


Just repeat the overview examples in [`rmcl_examples_micpl`](/rmcl_examples_micpl/) but replace the package name with this one; `rmcl_examples_micpl_gpu`.
All examples are the same, but using NVIDIA OptiX for hardware-accelerated correspondence search and CUDA kernels for GPU accelerated coveriance reduction.
The only part that differs from the config is setting `optix` as the backend everywhere `embree` was used before.

**Note**: Make sure [rmagine](https://github.com/uos/rmagine) was build with OptiX support.

