# AuRo_evolving_sobot_data
## Naming convention:
- `Pink` refers to the low accuracy model
- `Red` refers to the high accuracy model
- `s18` in the naming refers to the training jobs ran using seed18
- `s0` in the naming refers to the training jobs ran using seed0. **If a dirctory does not have any info related to seed (e.g. does not say s0 or s18) it will be defauted as a training job initated using seed0**
- `SM` or `SiliconeM` refers to the *surface* silicone mat.
- `CB` refers to the *surface* cardboard
- `TB` refers to the *surface* table

##Pressure logs info
- `pressure_logs` folder stores all the pressure profiles recorded from sim-to-real transfer experiments. Logs involve pressure recorded from built-in sensors of the pressure regulator, a upstream honeywell sensor, and commanded pressure input. 

- The logs decoder are included in the folder for analysis.

- A `knock down factor` is applied to some specific pressure profiles together with the calibrated pressure regulator profile to avoid overshooting, which will result in a disagreement between commended pressure recorded from logs and input pressure. In this case, please refer to the input pressure profile.

