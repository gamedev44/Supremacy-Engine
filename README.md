# 🎮 Supremacy Engine 🛠️

Supremacy Engine is an open-source **Python 3D engine** built on the **PyOpenGL** API. It uses **Pygame** and **Pyglet** as its game backends.

-----

## 📖 Table of Contents

  - [System Requirements](https://www.google.com/search?q=%23-system-requirements)
  - [Troubleshooting Anaconda Crash](https://www.google.com/search?q=%23-troubleshooting-anaconda-crash)
  - [Features](https://www.google.com/search?q=%23-features)
      - [Importers](https://www.google.com/search?q=%23importers)
      - [Lighting](https://www.google.com/search?q=%23lighting)
      - [Particle System](https://www.google.com/search?q=%23particle-system)
      - [Objects](https://www.google.com/search?q=%23objects)
      - [Rendering](https://www.google.com/search?q=%23rendering)
      - [Resource Management](https://www.google.com/search?q=%23resource-management)
      - [In-Game GUI](https://www.google.com/search?q=%23in-game-gui)
      - [Optimizations](https://www.google.com/search?q=%23optimizations)
  - [Coming Soon / Planned](https://www.google.com/search?q=%23-coming-soon--planned)

-----

## 💻 System Requirements

To get started, make sure you have the following installed:

  * **OpenGL 4.3** (Shading language 430)
  * `numpy`
  * `pillow`
  * `pyglet` or `pygame`
  * `PyOpenGL`
  * `PyOpenGL-accelerate` (optional)

It currently supports **Windows** and **Linux**, with Mac support not yet tested.

-----

## 🛠️ Troubleshooting Anaconda Crash

If you're experiencing an `ImportError: DLL load failed` when using Anaconda, it's often due to a conflict with the `Pillow` library. Here are three solutions you can try, starting with the most straightforward.

```
Traceback (most recent call last):
  File "main.py", line 44, in <module>
    from SupremacyEngine.Common import CustomQueue, CustomPipe
...
  File "...\Anaconda3\lib\site-packages\PIL\Image.py", line 90, in <module>
    from . import _imaging as core
ImportError: DLL load failed
```

  * **Solution 1: Install from the Anaconda channel**
    ```bash
    conda install -c anaconda pillow
    ```
  * **Solution 2: Install a specific version from conda-forge**
    ```bash
    conda install --channel conda-forge pillow=5
    ```
  * **Solution 3: Reinstall using pip**
    ```bash
    conda remove pillow
    pip install pillow
    ```

-----

## 🚀 Features

### Importers

  * **Mesh**: Supports `.obj` and `.dae` (Collada). Planned support includes `.fbx`, `.gltf`, and `.blend`.
  * **Texture**: Supports common formats like `.png`, `.tga`, `.bmp`, and `.jpeg`. Compressed texture support (ETC, DDS) is planned.

### Lighting

  * [x] **Directional Light** & **Shadow mapping**
  * [ ] Spot Light
  * [ ] Area Light
  * [x] **Point Light**

### Particle System

  * [x] **CPU-Based Particle**
  * [x] **GPU-Based Particle**
  <img width="1257" height="704" alt="image" src="https://github.com/user-attachments/assets/7740af2a-e6cf-48cc-8558-2686519597a1" />
  * [x] **Vector Field**
  * [ ] Particle spawn on polygon surface
  * [ ] Bitonic Sorting
  * [ ] Memory Pool
  * [ ] Attractor
  * [ ] Noise
  * [ ] Curl Noise

### Objects

  * [ ] Select, Move, Modify
  * [ ] Gizmo
  * [x] **Skeleton Mesh**
  * [x] **Static Mesh**
  * [ ] Tree, Foliage, Grass
  * [x] **Terrain**
<img width="1261" height="704" alt="image" src="https://github.com/user-attachments/assets/c009ec2e-e137-4c70-8b14-87269452eb27" />
  * [x] **Atmosphere & Sky**
<img width="3033" height="3156" alt="image" src="https://github.com/user-attachments/assets/129a1715-3cee-4182-986e-9cea3f77834b" />
  * [ ] Road
  * [ ] Wind
  * [x] **FFT Ocean**
<img width="2622" height="727" alt="image" src="https://github.com/user-attachments/assets/6d75d5e6-e03e-477e-b033-fe233beff669" />
  * [ ] River

### Rendering

  * **Culling**
      * [ ] Occlusion Culling
      * [ ] Distance Culling
      * [x] **View Frustum Culling**
  * [ ] VTF Skinning
  * [ ] Calculate animation on GPU
  * [ ] Distance Field Font
  * [x] **Real-time Light Probe**
  * [x] **PBR** (Physically Based Rendering)
  <img width="3905" height="730" alt="image" src="https://github.com/user-attachments/assets/07f343ec-4d4d-48a0-81d9-9aa5919568ae" />
  * [x] **Temporal AA**
  * [x] **SSAA**
  * [x] **MSAA**
  * [ ] Temporal Upscale
  * [x] **Screen Space Reflection** 
  * [x] **Screen Space Ambient Occlusion**
  * [ ] Screen Space Bevel
  * [ ] Screen Space SSS
  * [x] **Depth Of Field**
      * [ ] Bokeh
  * [x] **Bloom** 
  * [x] **Tone Mapping**
  * [ ] Glare
  * [ ] Film Grain
  * [ ] Color Correction
  * [ ] Color Grading
  * [x] **Light Shaft**
<img width="1262" height="700" alt="image" src="https://github.com/user-attachments/assets/2bc3935d-ee7d-492e-81f8-7a26b175e4dc" />
  * [x] **Motion Blur**
      * [ ] Recursive Velocity
  * [ ] Parallax Occlusion Rendering
  * [ ] Paraboloid environment map
  * [ ] Voxel Based GI
  * [ ] Volumetric Scattering
  * [ ] Fur Rendering

### Resource Management

  * [x] **Load / Save / Import / Export**
  * [ ] Unload / Reload system
  * [ ] Duplicate resource
  * [ ] Sound Manager
  * [x] **Script Manager**

### GUI
<img width="1273" height="748" alt="image" src="https://github.com/user-attachments/assets/a44ba44b-c801-4b93-8cf0-2fc8c1dc4cc5" />
  * [ ] Input / Output
  * [ ] Progress Bars
  * [ ] Buttons

### Optimizations

  * [ ] Only dynamic shadows are updated every frame; static shadows are not.
  * [ ] SSR ray reuse in compute shader
  * [ ] Post-processing in compute shader
  * [ ] FFT in compute shader
  * [ ] Precomputed atmosphere in compute shader

-----

## 🔮 Coming Soon / Planned

  * **Blender3D Plugin**: A plugin to transfer geometry, animation, and scene data between Blender and the engine.
  * **Bullet Physics**: Integration with the Bullet Physics library for realistic physics simulations.
